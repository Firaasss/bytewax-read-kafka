from bytewax.connectors.kafka import KafkaSource, KafkaSink, KafkaSinkMessage
from bytewax.connectors.stdio import StdOutSink
from bytewax import operators as op
from bytewax.dataflow import Dataflow

import json
import re
import string
import codecs

flow = Dataflow("twitter stream")
stream = op.input("inp", flow, KafkaSource(["localhost:9092"], ["my-topic"]))
processed = op.map("map", stream, lambda x: (x.key, x.value))

op.output("out", processed, StdOutSink())

