try:
    import os
    import platform
    import tkinter as tk
    from pytube import YouTube
    from tkinter import ttk
    from tkinter import filedialog
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

folderName= ""

def commandSOShell():
    sistema= platform.system()

    if sistema== "Windows":
        return "cls", sistema
    else:
        return "clear", sistema

def cambiarLabelTrue(*args):
    url= ytEntry.get()
    
    if url!= "" and "https://www.youtube.com/" in url:
        texto= "URL ingresada con éxito"
        color= "green"
    
    elif (("https://www.youtube.com/" not in url) and url!= ""):
        texto= "Ingresa una URL válida"
        color= "red"

    elif url== "":
        texto= "Ingresa la URL del video"
        color= "red"
    
    return ytError.config(text= texto, fg= color, font= ("jost", 15))

def abrirRuta():
    global folderName

    folderName= filedialog.askdirectory()
    if len(folderName) > 1:
        rutaError.config(text= folderName, fg= "green")
    else:
        rutaError.config(text= "Por favor elije una ruta", fg= "red")

def DescargarVideo():
    eleccion= ytElec.get()
    url= ytEntry.get()

    if len(url) > 1:
        ytError.config(text= "")
        yt= YouTube(url)

        if eleccion== elec[0]:
            video= yt.streams.get_highest_resolution()
        elif eleccion== elec[1]:
            video= yt.streams.get_lowest_resolution()
        elif eleccion== elec[2]:
            video= yt.streams.filter(only_audio= True).first()
        else:
            ytError.config(text= "Pon el enlace de nuevo del video", fg= "red")

    video.download(folderName)
    ytError.config(text= "Descarga completada", fg= "green")

raiz= tk.Tk()
comando, sis= commandSOShell()
os.system(comando)
raiz.title("Descargar videos youtube")
raiz.columnconfigure(0, weight= 1)
raiz.resizable(width= False, height= False)
raiz.iconbitmap("./descargaryt.ico")
screenWidth = raiz.winfo_screenwidth()# Ancho del área de visualización
screenHeight = raiz.winfo_screenheight()# Alto del área de visualización
if sis== "Windows":
    width= 400
    height= 450
else:
    width= 1000
    height= 1050
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
raiz.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")

# Label de enlace youtube
ytdlabel= tk.Label(raiz, text= "Ingresa la URL del video", font= ("jost", 15))
ytdlabel.grid()

# Caja de entrada de texto
ytEntryText= tk.StringVar()
ytEntry= tk.Entry(raiz, width= 50, textvariable= ytEntryText)
ytEntry.grid()
ytEntryText.trace_add("write", cambiarLabelTrue)

# Error mensaje
ytError= tk.Label(raiz, text= "Ingresa ruta", fg= "red", font= ("jost", 15))
ytError.grid()

# Etiqueta de solicitación de ruta donde guardar archivo.
saveLabel= tk.Label(raiz, text= "Guarda el video", font= ("jost", 15))
saveLabel.grid()

# Botón para guardar archivo
saveEntry= tk.Button(raiz, width= 10, bg= "red", fg= "white", text= "Ruta", command= abrirRuta)
saveEntry.grid()

# Error de ruta
rutaError= tk.Label(raiz, text= "Error en la ruta", fg= "red", font= ("jost", 15))
rutaError.grid()

# Resolución de descarga
ytRes= tk.Label(raiz, text= "Selecciona calidad", font= ("jost", 15))
ytRes.grid()

# Combobox de opciones
elec= ["Alta definición", "Baja definición", "Solo audio"]
ytElec= ttk.Combobox(raiz, values= elec, state= "readonly")
ytElec.grid()

# Botón descargar video/audio
downBot= tk.Button(raiz, text= "Descargar", width= 10, bg= "red", fg= "white", command= DescargarVideo)
downBot.grid()

# Cadena marca desarrollador
devLabel= tk.Label(raiz, text= "Diego", font= ("jost", 15))
devLabel.grid()

raiz.mainloop()