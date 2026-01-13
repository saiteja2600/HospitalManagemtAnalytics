import random
import time
from producer import get_producer
from config import EVENTHUBS_NAME, SLEEP_SECONDS

from generators.doctors import generate_doctor_event
from generators.patients import generate_patient_event
from generators.appointments import generate_appointment_event
from generators.treatments import generate_treatment_event
from generators.billing import generate_billing_event

def main():
    producer = get_producer()

    generators = [
        generate_doctor_event,
        generate_patient_event,
        generate_appointment_event,
        generate_treatment_event,
        generate_billing_event
    ]

    while True:
        event = random.choice(generators)()
        if event:
            producer.send(EVENTHUBS_NAME, value=event)
            producer.flush()
            print(f"Sent {event['event_type']} event")
        time.sleep(SLEEP_SECONDS)

if __name__ == "__main__":
    main()
