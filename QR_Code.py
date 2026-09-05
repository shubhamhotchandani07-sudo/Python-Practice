import qrcode


url = "https://www.youtube.com/@rohit_singh_chouhan143"


qr = qrcode.make(url)


qr.save("qrcode.png")

print("qr code created successfully")
