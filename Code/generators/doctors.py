import random
import string
from datetime import datetime
from registries import DOCTOR_REGISTRY
from dirty_data import inject_dirty_data

HOSPITAL_SPECIALIZATION_MAP = {
    "Central Hospital": ["Pediatrics", "Oncology", "Cardiology"],
    "Westside Clinic": ["Dermatology", "Oncology"],
    "Eastside Clinic": ["Pediatrics", "Neurology"]
}

def generate_doctor_event():
    doctor_id = f"D{random.randint(1, 50):03}"

    if doctor_id not in DOCTOR_REGISTRY:
        hospital = random.choice(list(HOSPITAL_SPECIALIZATION_MAP))
        DOCTOR_REGISTRY[doctor_id] = {
            "hospital": hospital,
            "specialization": random.choice(HOSPITAL_SPECIALIZATION_MAP[hospital])
        }

    record = {
        "event_type": "doctor",
        "doctor_id": doctor_id,
        "first_name": ''.join(random.choices(string.ascii_uppercase, k=5)),
        "last_name": ''.join(random.choices(string.ascii_uppercase, k=7)),
        "specialization": DOCTOR_REGISTRY[doctor_id]["specialization"],
        "hospital_branch": DOCTOR_REGISTRY[doctor_id]["hospital"],
        "years_of_experience": random.randint(1, 40),
        "email": f"{doctor_id.lower()}@hospital.com",
        "phone_number": f"+1{random.randint(1000000000,9999999999)}",
        "event_time": datetime.utcnow().isoformat()
    }
    return inject_dirty_data(record)
