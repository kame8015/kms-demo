import base64
import os

import boto3

aws_region = os.getenv("AWS_REGION", "ap-northeast-1")
key_id = os.getenv("KEY_ID", "dummy_key_id")
kms = boto3.client(service_name="kms", region_name=aws_region)


def encrypt_plain_text(plain_text: str) -> str:
    """plain_textを暗号化する"""
    enc_bin = kms.encrypt(KeyId=key_id, Plaintext=plain_text)["CiphertextBlob"]
    enc = base64.b64encode(enc_bin).decode("utf-8")

    return enc


def decrypt_plain_text(plain_text: str) -> str:
    """plain_textを復号化する"""
    enc_bin = base64.b64decode(plain_text)
    dec = kms.decrypt(CiphertextBlob=enc_bin)["Plaintext"].decode("utf-8")

    return dec
