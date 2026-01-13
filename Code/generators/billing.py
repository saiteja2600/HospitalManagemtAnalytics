import random
import uuid
from datetime import datetime
from registries import PATIENT_REGISTRY, TREATMENT_REGISTRY
from dirty_data import inject_dirty_data

PAYMENT_METHODS = ["Credit Card", "Cash", "Insurance"]

def generate_billing_event():
    if not PATIENT_REGISTRY or not TREATMENT_REGISTRY:
        return None

    record = {
        "event_type": "billing",
        "billing_id": f"B{uuid.uuid4().hex[:8]}",
        "patient_id": random.choice(list(PATIENT_REGISTRY)),
        "treatment_id": random.choice(TREATMENT_REGISTRY),
        "amount": round(random.uniform(100.0, 5000.0), 2),
        "billing_date": datetime.utcnow().isoformat(),
        "payment_method": random.choice(PAYMENT_METHODS),
        "event_time": datetime.utcnow().isoformat()
    }
    return inject_dirty_data(record)
