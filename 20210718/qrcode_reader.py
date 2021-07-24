from pyzbar.pyzbar import decode
from PIL import Image

print('QR코드 리더기')
qrcode_img = Image.open('my_qrcode.png')
decoded_qrcode = decode(qrcode_img)
print("QR 코드에 담긴 내용\n", decoded_qrcode[0].data.decode())