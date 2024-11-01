# Generador de Código QR con Python
=====================================

![](https://img.freepik.com/vector-gratis/concepto-escaneo-codigo-qr-caracteres-ilustrados_23-2148633631.jpg?t=st=1730499730~exp=1730503330~hmac=581b6c441a3b7cafbc89a4ac979cfaff3a768ec931b3ee33e0dfe40251d124bb&w=740)

Importar paquetes
Python
```py
import qrcode
import qrcode.constants
```

## Configuración del código QR

Datos del código QR
```py
data = ""  # URL o texto para el código QR
```

## Crear objeto QR

```py
qr = qrcode.QRCode(
    version=1,  # Tamaño del QR (pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Manejador de errores
    box_size=5,  # Tamaño de cada "cuadrado" en el QR
    border=4  # Grosor del borde (mínimo 4)
)
```

## Agregar datos y generar código QR

```py
qr.add_data(data)
qr.make(fit=True)
```

## Generar imagen del código QR

```py
img = qr.make_image(
    fill='black',  # Color de los cuadrados
    back_color='white'  # Color de fondo
)
```

## Guardar la imagen

```py
img.save("codigo.png")
```

## Documentación
Ejemplo de uso

Para generar un código QR para una URL específica, reemplaza data con la URL deseada:

```py
data = "https://www.ejemplo.com"
```

Luego, ejecuta el código para generar el archivo codigo.png en el directorio actual.

## Parámetros del objeto QR

- version: Tamaño del código QR (1-40).
- error_correction: Nivel de corrección de errores.
- ERROR_CORRECT_L: Nivel bajo (aproximadamente 7% o menos errores).
    - ERROR_CORRECT_M: Nivel medio (aproximadamente 15% o menos errores).
    - ERROR_CORRECT_Q: Nivel alto (aproximadamente 25% o menos errores).
    - ERROR_CORRECT_H: Nivel muy alto (aproximadamente 30% o menos errores).
- box_size: Tamaño de cada cuadrado en el código QR.
- border: Grosor del borde del código QR.

## Documentacion del paquete

\[](https://pypi.org/project/qrcode/)
