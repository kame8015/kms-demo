from cryptography.fernet import Fernet
import base64

ENCRYPT_KEY = "AB123456789012345678901234567890"
text = "password"
f = Fernet(base64.b64encode(bytes(ENCRYPT_KEY, "utf-8")))

enc = f.encrypt(bytes(text, "utf-8")).decode("utf-8")
print("enc=" + enc)
dec = f.decrypt(bytes(enc, "utf-8")).decode("utf-8")
print("dec=" + dec)
