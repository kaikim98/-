import pyqrcode
import url_shorter
url = input("줄일 url 입력\n")
msg = url_shorter.shorter(url)
qrcode = pyqrcode.create(msg)
qrcode.png("my_qrcode.png", scale=7)
print("QR코드가 생성되었습니다")
