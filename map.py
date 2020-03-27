from flask import Flask, request, render_template
import tweepy

# Global Variables
app = Flask(__name__)
consumer_key = 'API key'
consumer_secret = 'API secret key'
token_key = 'Access token:'
token_secret = 'Access token secret'


@app.route('/', methods=['POST', 'GET'])
def index():
    title = 'Tweeter Maps'
    keyphrase = request.form.get('trend')  # term to be searched for
    if keyphrase and len(keyphrase) <= 500:  # input keyphrase if None or too long
        data = search_tweets(keyphrase)  # generates a list of strings containing coordinates/floats
    else:
        data = []  # invalid input -> generate an empty list
    return render_template("index.html", title=title, data=data, len=len(data))


# return list of coordinates for tweets containing location data and matching keyphrase
def search_tweets(keyphrase):
    # Authentication for Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token_key, token_secret)
    api = tweepy.API(auth)
    # resulting list of coordinates
    result = []
    # retrieve the most recent tweets containing the keyphrase
    for tweet in api.search(q=keyphrase, result_type='recent'):
        if tweet.place:  # only check tweets containing location data
            lat_lon = parse(tweet.place)  # tuple of coordinate pairs
            result.append(lat_lon[0])  # append latitude to result
            result.append(lat_lon[1])  # append longitude to result
    return result


# parse out the center of the bounding box
# return the longitude and latitude in string form
def parse(place):
    lat = 0
    lon = 0
    # Retrieve array of coordinates
    coordinates_set = place.bounding_box.coordinates[0]
    # Calculate center of bounding_box
    for coord in coordinates_set:
        lat += coord[1]
        lon += coord[0]
    # return latitude and longitude of the given place
    result = (str(lat / 4), str(lon / 4))
    return result
