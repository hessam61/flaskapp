from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

import geocoder
import urllib2
import json

#usable instance of SQLAlchemy class
db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	email = db.Column(db.String(120), unique=True)
	pwdhash = db.Column(db.String(54))

	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		#use lower to make sure we can match regardless of how its typed
		self.email = email.lower()
		self.set_password(password)

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

# p = Place()
# places = p.query("1501 walnut st., Philadelphia, PA")
class Place(object):
	def meters_to_walking_time(self, meters):
		# 1 min in roughly 80 meter
		return int(meters / 80)

	def wiki_path(self, slug):
		return urllib2.urlparse.urljoin("http://en.wikipedia.org/wiki/", slug.replace(' ', '_'))

	def address_to_latlng(self, address):
		g = geocoder.google(address)
		return (g.lat, g.lng)

	def query(self, address):
		lat, lng = self.address_to_latlng(address)

		query_url = 'https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=5000&gscoord={0}%7C{1}&gslimit=20&format=json'.format(lat, lng)
		g = urllib2.urlopen(query_url)
		results = g.read()
		g.close()

		data = json.loads(results)

		places = []

		for place in data['query']['geosearch']:
			name = place['title']
			meters = place['dist']
			lat = place['lat']
			lng = place['lon']

			wiki_url = self.wiki_path(name)
			walking_time = self.meters_to_walking_time(meters)

			d = {
				'name': name,
				'url': wiki_url,
				'time': walking_time,
				'lat': lat,
				'lng': lng
			}

			places.append(d)

		return places