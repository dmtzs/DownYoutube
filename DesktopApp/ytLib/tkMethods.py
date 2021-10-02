try:
    import os
    #os.environ["IMAGEIO_FFMPEG_EXE"]= "/usr/bin/ffmpeg"
    import sys
    import wget
    import time
    import platform
    import webbrowser
    import tkinter as tk
    import moviepy.editor as mp
    from pytube import YouTube
    from PIL import Image, ImageTk
    from tkinter import ttk, filedialog, messagebox
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

# -----------------Other methods-----------------
class extraMethods():
    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def commandSOShell(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

    def thumbnail(self, urlThumb):
        ytThumb= YouTube(urlThumb)

        thumb= ytThumb.thumbnail_url
        thumbTitle= ytThumb.title
        thumbAuthor= ytThumb.author
        thumbDesc= ytThumb.description

        _, ext= os.path.splitext(thumb)

        outputDirectory= f"./tthumbnail{ext}"

        wget.download(thumb, out= outputDirectory)

        return outputDirectory, thumbTitle, thumbAuthor, thumbDesc

# -----------------Tkinter widgets methods-----------------
class tkClass(extraMethods):
    banderas= [0, 0]#URL, path to keep
    fileIco= "descargaryt.ico"
    titleApp= "Descargar videos youtube"
    labelTitleApp= "Youtube downloader"
    folderName= ""
    fileName= ""
    thumbTitle= ""
    thumbAuthor= ""
    thumbDesc= ""
    thumbOutputDirectory= ""
    
# -----------------Main window and their components-----------------
    def GUI(self):
        def desbloqBoton():
            if ((self.banderas[0]== 1)and(self.banderas[1]== 1)):
                downBot.config(state= "normal", bg= "red")
            else:
                downBot.config(state= "disabled", bg= "#C8C1BF")

        def repoGit():
            webbrowser.open("https://github.com/dmtzs/DownYoutube")

        def cambiarLabelTrue(*args):
            url= ytEntry.get()
            
            if url!= "" and "https://www.youtube.com/" in url:
                texto= "URL ingresada correctamente"
                color= "green"
                self.banderas[0]= 1
                self.thumbOutputDirectory, self.thumbTitle, self.thumbAuthor, self.thumbDesc= self.thumbnail(url)
            
            elif (("https://www.youtube.com/" not in url) and url!= ""):
                texto= "Ingresa una URL válida"
                color= "red"
                self.banderas[0]= 0

            elif url== "":
                texto= "Ingresa la URL del video"
                color= "red"
                self.banderas[0]= 0

            desbloqBoton()
            
            return ytError.config(text= texto, fg= color, font= ("jost", 15))

        def abrirRuta():
            global folderName

            folderName= filedialog.askdirectory()
            if len(folderName) > 1:
                texto= folderName
                color= "green"
                self.banderas[1]= 1
            else:
                texto= "Por favor elije una ruta"
                color= "red"
                self.banderas[1]= 0
            
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

            # Download complete pop up
            messagebox.showinfo("Alert", "Descarga completada")

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
        comando, sis= self.commandSOShell()
        os.system(comando)
        raiz.title(self.titleApp)
        raiz.columnconfigure(0, weight= 1)
        raiz.resizable(width= False, height= False)
        try:
            iconImage= self.resource_path(self.fileIco)
            raiz.iconbitmap(iconImage)
        except:
            raiz.iconbitmap(self.fileIco)
        screenWidth = raiz.winfo_screenwidth()# Ancho del área de visualización
        screenHeight = raiz.winfo_screenheight()# Alto del área de visualización
        if sis== "Windows":
            width= 500
            height= 550
        else:
            width= 1000
            height= 1050
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        raiz.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")

        #Label title of the application
        titleLabel= tk.Label(raiz, fg= "red", text= self.labelTitleApp, font= ("jost", 25))
        titleLabel.place(x= 102, y= 5)

        # Label youtube link
        ytdlabel= tk.Label(raiz, text= "Ingresa la URL del video:", font= ("jost", 15))
        ytdlabel.place(x= 135, y= 58)

        # Entry box
        ytEntryText= tk.StringVar()
        ytEntry= tk.Entry(raiz, width= 79, textvariable= ytEntryText)
        ytEntry.place(x= 10, y= 100)
        ytEntry.focus()
        ytEntryText.trace_add("write", cambiarLabelTrue)

        # Error message
        ytError= tk.Label(raiz, text= "", fg= "red", font= ("jost", 11))
        ytError.place(x= 120, y= 120)

        # Label for rtequest the path in which the video or mp3 file will be stored
        saveLabel= tk.Label(raiz, text= "Guarda el video:", font= ("jost", 15))
        saveLabel.place(x= 170, y= 160)

        # Button for keep the file
        saveEntry= tk.Button(raiz, width= 10, bg= "red", fg= "white", text= "Ruta", takefocus= False, command= abrirRuta)
        saveEntry.place(x= 10, y= 190)

        # Path error
        rutaError= tk.Label(raiz, text= "Selecciona una ruta", fg= "red", font= ("jost", 8))
        rutaError.place(x= 90, y= 193)

        # Download resolution
        ytRes= tk.Label(raiz, text= "Selecciona calidad de video o solo audio:", font= ("jost", 15))
        ytRes.place(x= 10, y= 230)

        # Combobox of options
        elec= ["Alta definición", "Baja definición", "Solo audio"]
        valElec= tk.StringVar()
        valElec.set(elec[0])
        ytElec= ttk.Combobox(raiz, values= elec, state= "readonly", textvariable= valElec, width= 15)
        ytElec.place(x= 380, y= 235)

        # Video/audio download button
        downBot= tk.Button(raiz, text= "Descargar", width= 10, bg= "#C8C1BF", fg= "white", state= "disabled", takefocus= False, command= DescargarVideo)
        downBot.place(x= 200, y= 270)

        # Label to github repository
        labelGit= tk.Label(raiz, text= "Repositorio del programa:", font= ("jost", 10))
        labelGit.place(x= 130, y= 525)

        # Button to repository
        butGit= tk.Button(raiz, width= 10, bg= "red", fg= "white", text= "Repositorio", takefocus= False, command= repoGit)
        butGit.place(x= 290, y= 523)

        # Thumbnail
        # Ima= Image.open("./tthumbnail.jpg")
        # #Ima= Image.open(self.thumbOutputDirectory)
        # Ima= Ima.resize((200, 150), Image.ANTIALIAS)# height, width
        # renderIma= ImageTk.PhotoImage(Ima)

        # ImaLabel= tk.Label(raiz, image= renderIma)
        # ImaLabel.place(x= 20, y= 320)

        # Thumbnail info
        # thumbTitleLabel= tk.Label(raiz, text= self.thumbTitle, font= ("jost", 10))
        # thumbAuthorLabel= tk.Label(raiz, text= self.thumbAuthor, font= ("jost", 10))
        # thumbDescLabel= tk.Label(raiz, text= self.thumbDesc, font= ("jost", 10))
        
        # thumbTitleLabel.place(x= 200, y=560)

        raiz.mainloop()