from kafka import KafkaConsumer
from rich import print

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['localhost:9092'],
    group_id = "my-group",
)

#loop
for msg in consumer:
    print(msg.value)