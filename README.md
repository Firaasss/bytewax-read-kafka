## Bytewax with Kafka input
To create a Kafka stream and push data into it from a static json file consisting of tweets. The Kafka server is initialized using Kafka-Python and can be installed with Homebrew using ``brew install kafka``
Zookeeper as well is required to instantiate the Kafka server and also installed with Homebrew using ``brew install zookeeper``

Both services can be started simply with ``brew start kafka`` and ``brew start zookeeper``. Verify they are running with ``brew services``.

Kafka server should be running on ``localhost:9092``, if not, check your kafka.properties located in ``your-kafka-installation-path/bin/kafka.properties``

### Kafka_tweets_producer.py
Load the tweets from data.json. Send data using KafkaProducer to the Kafka Server listening on port 9092. 

run ``python3 kafka_tweets_producer.py``

### Kafka_tweets_consumer.py
Read the messages published to the "my-topic" topic produced by kafka_tweets_producer.py and output to terminal.
Note: this is not related to the functionality of injesting the data in Bytewax. This is solely to prove that the KafkaProducer works before moving on.

run ``python3 kafka_tweets_consumer.py``

### twitter_bytewax
Lots of imports.. don't need them all (in process of testing)
Initialize the dataflow object, read directly from the kafka topic that was created when sending messages in kafka_tweets_producer.py.
Output to terminal using the BW output connector StdOutSink()

run ``python3 -m bytewax.run twitter_bytewax``

To watch bytewax digest the data in action, run the producer in a split screen.
