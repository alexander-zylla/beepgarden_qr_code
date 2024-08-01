# beep.garden QR Code Generator

## Summary 

This is used to generate WiFi Qrcodes for beep.garden. These QrCodes are required by the app inorder to connect to the WiFi of the gateway.

## Usage

```bash
python3 create-encrypted-qrcode.py
```

You then get promted to enter the ssid and password.
The generated QRCode will be stored under ./qrcodes/(ssid).png