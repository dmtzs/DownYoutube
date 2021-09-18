try:
    import os
    os.environ["IMAGEIO_FFMPEG_EXE"]= "/usr/bin/ffmpeg"
    import time
    import sys
    import platform
    import tkinter as tk
    import moviepy.editor as mp
    from pytube import YouTube
    from tkinter import ttk
    from tkinter import filedialog
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

banderas= [0, 0]#URL, Ruta guardar
folderName= ""
fileName= ""

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def desbloqBoton():
    if ((banderas[0]== 1)and(banderas[1]== 1)):
        downBot.config(state= "normal", bg= "red")
    else:
        downBot.config(state= "disabled", bg= "#C8C1BF")

def commandSOShell():
    sistema= platform.system()

    if sistema== "Windows":
        return "cls", sistema
    else:
        return "clear", sistema

def cambiarLabelTrue(*args):
    url= ytEntry.get()
    
    if url!= "" and "https://www.youtube.com/" in url:
        texto= "URL ingresada correctamente"
        color= "green"
        banderas[0]= 1
    
    elif (("https://www.youtube.com/" not in url) and url!= ""):
        texto= "Ingresa una URL válida"
        color= "red"
        banderas[0]= 0

    elif url== "":
        texto= "Ingresa la URL del video"
        color= "red"
        banderas[0]= 0

    desbloqBoton()
    
    return ytError.config(text= texto, fg= color, font= ("jost", 15))

def abrirRuta():
    global folderName

    folderName= filedialog.askdirectory()
    if len(folderName) > 1:
        texto= folderName
        color= "green"
        banderas[1]= 1
    else:
        texto= "Por favor elije una ruta"
        color= "red"
        banderas[1]= 0

    desbloqBoton()
    rutaError.config(text= texto, fg= color)

def DescargarVideo():
    global fileName
    eleccion= ytElec.get()
    url= ytEntry.get()

    if len(url) > 1:
        yt= YouTube(url)

        if eleccion== elec[0] or eleccion== elec[2]:
            video= yt.streams.get_highest_resolution()
        elif eleccion== elec[1]:
            video= yt.streams.get_lowest_resolution()
        # elif eleccion== elec[2]:
            # video= yt.streams.filter(only_audio= True).first()
        else:
            ytError.config(text= "Pon el enlace de nuevo del video", fg= "red")

    video.download(folderName)
    fileName= yt.streams[0].title
    
    if eleccion== elec[2]:
        newFolderNameIn= VideoAudioConverter()
        time.sleep(2)
        print(newFolderNameIn)
        os.remove(newFolderNameIn)

    completeLabel.config(text= "Descarga completada", fg= "green")

def VideoAudioConverter():
    global folderName, fileName

    expresiones= [f"{chr(92)}", "/", ":", "*", "?", f"{chr(34)}", "<", ">", f"{chr(124)}"]

    for exp in expresiones:
        if exp in fileName:
            fileName= fileName.replace(exp, "")
    
    lenFolderName= len(folderName)
    folderNamePasrsedInput= folderName.replace("/", chr(92), lenFolderName+1)
    newFolderNameIn= f"{folderNamePasrsedInput}{chr(92)}{fileName}.mp4"
    newFolderNameOut= f"{folderNamePasrsedInput}{chr(92)}{fileName}.mp3"

    video= mp.VideoFileClip(newFolderNameIn)
    video.audio.write_audiofile(newFolderNameOut)
    video.close()

    return newFolderNameIn

raiz= tk.Tk()
comando, sis= commandSOShell()
os.system(comando)
raiz.title("Descargar videos youtube")
raiz.columnconfigure(0, weight= 1)
raiz.resizable(width= False, height= False)
iconImage= resource_path("descargaryt.ico")
raiz.iconbitmap(iconImage)
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
ytEntry.focus()
ytEntryText.trace_add("write", cambiarLabelTrue)

# Error mensaje
ytError= tk.Label(raiz, text= "Ingresa URL del video", fg= "red", font= ("jost", 15))
ytError.grid()

# Etiqueta de solicitación de ruta donde guardar archivo.
saveLabel= tk.Label(raiz, text= "Guarda el video", font= ("jost", 15))
saveLabel.grid()

# Botón para guardar archivo
saveEntry= tk.Button(raiz, width= 10, bg= "red", fg= "white", text= "Ruta", takefocus= False, command= abrirRuta)
saveEntry.grid()

# Error de ruta
rutaError= tk.Label(raiz, text= "Selecciona una ruta", fg= "red", font= ("jost", 15))
rutaError.grid()

# Resolución de descarga
ytRes= tk.Label(raiz, text= "Selecciona calidad", font= ("jost", 15))
ytRes.grid()

# Combobox de opciones
elec= ["Alta definición", "Baja definición", "Solo audio"]
valElec= tk.StringVar()
valElec.set(elec[0])
ytElec= ttk.Combobox(raiz, values= elec, state= "readonly", textvariable= valElec)
ytElec.grid()

# Botón descargar video/audio
downBot= tk.Button(raiz, text= "Descargar", width= 10, bg= "#C8C1BF", fg= "white", state= "disabled", takefocus= False, command= DescargarVideo)
downBot.grid()

#Label descarga completada
completeLabel= tk.Label(raiz, text= "", font= ("jost", 20))
completeLabel.grid()

raiz.mainloop()