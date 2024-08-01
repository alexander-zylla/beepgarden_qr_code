from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import qrcode
import base64
import json

import qrcode.main

# Dont lose that or terrible things will happen!!
secret_key = b'qZwHgXyTD4I0yN0eryhoSQZiLZVhCNXQ'
version = 1

def encrypt_json(json_data, secret_key):
    cipher = AES.new(secret_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(
        pad(json_data.encode(), AES.block_size)
    )
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return json.dumps({'iv': iv, 'ciphertext': ct})

ssid = input("Enter the SSID: ")
password = input("Enter the password: ")

json_data = json.dumps({
    "ssid": ssid,
    "password": password,
    "version": version
})

encrypted_data = encrypt_json(json_data, secret_key)
qr = qrcode.main.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(encrypted_data)
qr.make(fit=True)

# Save QR code as an image
path = './qrcodes/'
filename = ssid + '.png'
img = qr.make_image(fill='black', back_color='white')
img.save(path + filename)

print(encrypted_data)
