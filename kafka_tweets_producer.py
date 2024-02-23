import json
from time import sleep
from kafka import KafkaProducer
from json import dumps
from rich import print
from kafka.errors import KafkaError
import logging as log

##kafka server
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda K:dumps(K).encode('utf-8'))

# Define the path to the JSON file
json_file_path = 'data.json'
 
# Read the JSON file
with open(json_file_path, 'r') as file:
    for line in file:
        # Parse each line as a JSON object
        tweet_data = json.loads(line)
 
        cur_data={
        'id_str': tweet_data['id_str'],
        'username': tweet_data['username'],
        'tweet': tweet_data['tweet'],
        'location': tweet_data['location'],
        'created_at': tweet_data['created_at'],
        'retweet_count': tweet_data['retweet_count'],
        'favorite_count': tweet_data['favorite_count'],
        'followers_count': tweet_data['followers_count'],
        'lang': tweet_data['lang'],
        'coordinates': tweet_data['coordinates']
        }
 
        sleep(1)
        future = producer.send('my-topic', value=cur_data) 

        try:
            record_metadata = future.get(timeout=10)
        except KafkaError:
            # Decide what to do if produce request failed...
            log.exception()
            pass
        
        print(cur_data)