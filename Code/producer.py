import json
from kafka import KafkaProducer
from config import BOOTSTRAP_SERVERS, CONNECTION_STRING, API_VERSION

def get_producer():
    return KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        security_protocol="SASL_SSL",
        sasl_mechanism="PLAIN",
        sasl_plain_username="$ConnectionString",
        sasl_plain_password=CONNECTION_STRING,
        
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
