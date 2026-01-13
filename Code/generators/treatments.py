import random
import uuid
from datetime import datetime
from registries import DOCTOR_REGISTRY, PATIENT_REGISTRY, TREATMENT_REGISTRY
from dirty_data import inject_dirty_data

TREATMENT_TYPES = ["Chemotherapy", "MRI", "X-Ray", "ECG", "Physiotherapy"]

def generate_treatment_event():
    if not DOCTOR_REGISTRY or not PATIENT_REGISTRY:
        return None

    treatment_id = f"T{uuid.uuid4().hex[:8]}"
    TREATMENT_REGISTRY.append(treatment_id)

    record = {
        "event_type": "treatment",
        "treatment_id": treatment_id,
        "patient_id": random.choice(list(PATIENT_REGISTRY)),
        "doctor_id": random.choice(list(DOCTOR_REGISTRY)),
        "treatment_type": random.choice(TREATMENT_TYPES),
        "treatment_date": datetime.utcnow().isoformat(),
        "notes": "Patient responded well.",
        "event_time": datetime.utcnow().isoformat()
    }
    return inject_dirty_data(record)
