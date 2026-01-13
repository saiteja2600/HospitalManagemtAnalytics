import random

def inject_dirty_data(record: dict) -> dict:
    # Common dirty data
    if random.random() < 0.03:
        record["event_time"] = None

    if "email" in record and random.random() < 0.05:
        record["email"] = None

    if "phone_number" in record and random.random() < 0.05:
        record["phone_number"] = "INVALID_PHONE"

    # Entity-specific dirty data
    if "years_of_experience" in record and random.random() < 0.05:
        record["years_of_experience"] = "unknown"

    if "amount" in record and random.random() < 0.03:
        record["amount"] = -1

    return record
