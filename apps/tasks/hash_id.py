import hashlib
import secrets


def generate_hash_id():
    return hashlib.sha256(secrets.token_bytes(32)).hexdigest()