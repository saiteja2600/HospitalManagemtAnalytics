import random
import string
from datetime import datetime, timedelta
from registries import PATIENT_REGISTRY
from dirty_data import inject_dirty_data

GENDER = ["M", "F"]
INSURANCE_PROVIDERS = ["WellnessCorp", "MedCare Plus", "PulseSecure"]

def generate_patient_event():
    patient_id = f"P{random.randint(1, 200):03}"

    if patient_id not in PATIENT_REGISTRY:
        PATIENT_REGISTRY[patient_id] = f"INS{random.randint(100000,999999)}"

    record = {
        "event_type": "patient",
        "patient_id": patient_id,
        "first_name": ''.join(random.choices(string.ascii_uppercase, k=5)),
        "last_name": ''.join(random.choices(string.ascii_uppercase, k=7)),
        "date_of_birth": (
            datetime.now() - timedelta(days=random.randint(18*365, 80*365))
        ).strftime("%Y-%m-%d"),
        "gender": random.choice(GENDER),
        "email": f"{patient_id.lower()}@patient.com",
        "phone_number": f"+1{random.randint(1000000000,9999999999)}",
        "insurance_provider": random.choice(INSURANCE_PROVIDERS),
        "insurance_number": PATIENT_REGISTRY[patient_id],
        "event_time": datetime.utcnow().isoformat()
    }
    return inject_dirty_data(record)
