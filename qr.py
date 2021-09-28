# Importamos la biblioteca
import qrcode

# Creamos el código QR y entre comillas simples escribimos la cadena que se va a codificar, en este caso usamos la dirección de nuestro blog
img = qrcode.make('https://github.com/dmtzs/DownYoutube')

# Abrimos un archivo en modo escritura que es donde se guardará nuestro código.
img_file = open('smart.png', 'wb')

# Guardamos nuestro código en el archivo que creamos y lo cerramos
img.save(img_file)
img_file.close()
