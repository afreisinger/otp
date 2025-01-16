import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# Creo el codigo de prueba
data = "Adrian Freisinger 0123456789 :)"
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Guardo el código QR como imagen
qr_image = qr.make_image(fill="black", back_color="white")
qr_image.save("qr.png")

# Decodificar el código QR
decoded_data = decode(Image.open("qr.png"))

# Extraer el contenido del QR
if decoded_data:
    print("Contenido del QR:", decoded_data[0].data.decode("utf-8"))
else:
    print("No se pudo decodificar el QR.")