import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'consumer_key'
credentials['CONSUMER_SECRET'] = 'consumer_secret'
credentials['ACCESS_TOKEN'] = 'access_token'
credentials['ACCESS_SECRET'] = 'access_secret'

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
