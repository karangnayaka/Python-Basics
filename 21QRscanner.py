#qrcode scanner

import qrcode    #for to import qrcode scanner we should have to install [pip qrcode ]

data = input("Enter input>> ")

qr = qrcode.make(data)

qr.save("C:/Users/karan/Desktop/qrnew.png")  #the path u need to save it
print("QR code generated and saved successfully!")