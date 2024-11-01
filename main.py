import qrcode
import qrcode.constants

# url
data = ""

# congigurar el qr
qr = qrcode.QRCode(
    version=1, # tamaño del QR ( pequeño )
    error_correction=qrcode.constants.ERROR_CORRECT_L, # manejador de errores
    box_size=5, # tamaño de cada "cuadrado" en el QR
    border=4, # grosor del border (minimo es 4)
)

# añadir los datos al ibjeto Qr
qr.add_data(data)
qr.make(fit=True) # ajusta automáticamente el tamaño del código QR según la cantidad de datos que estás ingresando.

# generar codigo QR
img = qr.make_image(fill='black', back_color='white')

# guardar imagen
img.save("codigo.png")