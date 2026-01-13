import random
import uuid
from datetime import datetime, timedelta
from registries import DOCTOR_REGISTRY, PATIENT_REGISTRY
from dirty_data import inject_dirty_data

APPOINTMENT_STATUS = ["Scheduled", "Completed", "Cancelled", "No-Show"]

def generate_appointment_event():
    if not DOCTOR_REGISTRY or not PATIENT_REGISTRY:
        return None

    record = {
        "event_type": "appointment",
        "appointment_id": f"A{uuid.uuid4().hex[:8]}",
        "patient_id": random.choice(list(PATIENT_REGISTRY)),
        "doctor_id": random.choice(list(DOCTOR_REGISTRY)),
        "appointment_date": (
            datetime.now() + timedelta(days=random.randint(0, 7))
        ).strftime("%Y-%m-%d"),
        "appointment_time": f"{random.randint(8,18)}:{random.choice(['00','15','30','45'])}",
        "reason_for_visit": random.choice(
            ["Checkup", "Follow-up", "New Symptoms", "Prescription Refill"]
        ),
        "status": random.choice(APPOINTMENT_STATUS),
        "event_time": datetime.utcnow().isoformat()
    }
    return inject_dirty_data(record)
