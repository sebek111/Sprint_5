import uuid

def generate_email():
    return f"user_{uuid.uuid4().hex[:8]}@example.com"