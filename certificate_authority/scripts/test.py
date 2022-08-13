from scripts.deploy import deploy_certification, create_certificate, get_certificate
from scripts.verification import verify_signature
from scripts.keyGeneration import generate_CA_key_pairs


def main():
    CA_public_key, CA_private_key = generate_CA_key_pairs()
    print(CA_public_key, CA_private_key)
    deploy_certification()
    create_certificate("Alice", 123)
    get_certificate()
    verify_signature(123, 30)