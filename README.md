# Tweeter Earth
### Run it on your own
* Obtain your own API key for Google Maps and Twitter
#### Google API
* Go to Google's website to 
[obtain API key](https://console.cloud.google.com/getting-started)
* Then go to APIs & Services -> Library -> Maps JavaScript API -> enable
* Go to API Key Restrictions on the credentials page and allow Maps Javascript API
* On index.html put your API key where it says API_KEY_HERE
```
<script async defer src="https://maps.googleapis.com/maps/api/js?key=API_KEY_HERE&callback=initMap"
  type="text/javascript"></script>
```
#### Twitter API
* Apply for a Twitter Developer Account
[Twitter Developer Account](https://developer.twitter.com/)
* Create an app
* On app details go to keys & tokens
* Copy and paste keys and tokens into map.py
```python
# Global Variables
consumer_key = 'API key'
consumer_secret = 'API secret key'
token_key = 'Access token:'
token_secret = 'Access token secret'
```
#### Using Tweeter Maps
* Enter the phrase you would like to be searched for into the text box. This could be an @, #, or phrase
* On the Google Map it will display where these tweets were posted if they shared their location
* If your searches result in few markers I recommend you try #tweeterEarth as your search term to demonstrate how it works with plenty of location data

#### Limitations
* The amount of markers shown depends on the amount data your API key has access to. 
* If you are using the free version, most searches will result in few markers because Twitter will only grab the 100 most recent tweets with that phrase and only some tweets have location data.
* Try #tweeterEarth to see how it would work with a good amount of location data
