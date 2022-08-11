from scripts.deploy import deploy_certification, create_certificate, get_certificate
from scripts.verification import verify_signature


def main():
    deploy_certification()
    create_certificate("Alice", 123)
    get_certificate()
    verify_signature(123, 30)
