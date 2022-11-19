try:
    import os
    #os.environ["IMAGEIO_FFMPEG_EXE"]= "/usr/bin/ffmpeg"
    import sys
    import wget
    import time
    import platform
    import webbrowser
    import tkinter as tk
    from pytube import YouTube
    import moviepy.editor as mp
    from PIL import Image, ImageTk
    from tkinter.constants import CENTER, LEFT, RIGHT
    from tkinter import ttk, filedialog, messagebox
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

# -----------------Other methods-----------------
class ExtraMethods():
    def resource_path(self, relative_path: str) -> str:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def command_so_shell(self) -> tuple[str, str]:
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

    def thumbnail(self, urlThumb: str) -> tuple[str, str, str]:
        ytThumb= YouTube(urlThumb)

        thumb= ytThumb.thumbnail_url
        thumbTitle= ytThumb.title
        thumbAuthor= ytThumb.author
        thumbDesc= ytThumb.description

        trash, ext= os.path.splitext(thumb)
        del trash
        tama= len(ext)

        if tama > 4:
            tama-= 4
            ext = ext[:-tama]
        

        outputDirectory= f"./tthumbnail{ext}"

        wget.download(thumb, out= outputDirectory)

        #Tal vez no sea necesario el return debido a que tal vez sea mejor directamente en los datos modificar el label con estos datos
        #De igual manera los atributos definidos para esto se volverían innecesarios, probar eso a ver si funciona que si debería.

        return thumbTitle, thumbAuthor, thumbDesc

# -----------------Tkinter widgets methods-----------------
class TkClass(ExtraMethods):
    banderas = [0, 0]#URL, path to keep
    fileIco = "descargaryt.ico"
    titleApp = "Descargar videos youtube"
    labelTitleApp = "Youtube downloader"
    folderName = ""
    fileName = ""
    
# -----------------Main window and their components-----------------
    def GUI(self):
        def salir() -> None:
            try:
                os.remove("./tthumbnail.jpg")
            except:
                pass
            finally:
                raiz.destroy()

        def desbloq_boton() -> None:
            if ((self.banderas[0]== 1)and(self.banderas[1]== 1)):
                downBot.config(state= "normal", bg= "red")
            else:
                downBot.config(state= "disabled", bg= "#C8C1BF")

        def repo_git() -> None:
            webbrowser.open("https://github.com/dmtzs/DownYoutube")

        def config_ima_label_show(thumbTitle: str, thumbAuthor: str, thumbDesc: str) -> None:
            # Thumbnail
            Ima= Image.open("./tthumbnail.jpg")
            Ima= Ima.resize((200, 150), Image.ANTIALIAS)# height, width
            renderIma= ImageTk.PhotoImage(Ima)
            Ima.close()

            ImaLabel.configure(image= renderIma)
            ImaLabel.image= renderIma

            thumbTitleLabel.config(text= thumbTitle)
            thumbAuthorLabel.config(text= thumbAuthor)
            thumbDescLabel.config(text= thumbDesc)

        def config_ima_label_del() -> None:
            try:
                os.remove("./tthumbnail.jpg")
            except:
                pass
            finally:
                ImaLabel.configure(image= None)
                ImaLabel.image= None

                thumbTitleLabel.config(text= "")
                thumbAuthorLabel.config(text= "")
                thumbDescLabel.config(text= "")

        def cambiar_label_true(*args) -> tk.Label:
            url= ytEntry.get()
            
            if url!= "" and "https://www.youtube.com/" in url:
                texto= "URL ingresada correctamente"
                color= "green"
                self.banderas[0]= 1
                thumbTitle, thumbAuthor, thumbDesc= self.thumbnail(url)

                config_ima_label_show(thumbTitle, thumbAuthor, thumbDesc)
            
            elif (("https://www.youtube.com/" not in url) and url!= ""):
                texto= "Ingresa una URL válida"
                color= "red"
                self.banderas[0]= 0

                config_ima_label_del()

            elif url== "":
                texto= "Ingresa la URL del video"
                color= "red"
                self.banderas[0]= 0
                
                config_ima_label_del()

            desbloq_boton()
            
            return ytError.config(text= texto, fg= color, font= ("jost", 15))

        def abrir_ruta() -> None:
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
            
            desbloq_boton()
            rutaError.config(text= texto, fg= color)

        def descargar_video() -> None:
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
                newFolderNameIn= video_audio_converter()
                time.sleep(2)
                print(newFolderNameIn)
                os.remove(newFolderNameIn)

            # Download complete pop up
            messagebox.showinfo("Alert", "Descarga completada")

        def video_audio_converter() -> str:
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

        raiz = tk.Tk()
        comando, sis = self.command_so_shell()
        os.system(comando)
        raiz.title(self.titleApp)
        raiz.columnconfigure(0, weight= 1)
        raiz.resizable(width= False, height= False)
        if sis == "Windows":
            try:
                iconImage= self.resource_path(self.fileIco)
                raiz.iconbitmap(iconImage)
            except:
                raiz.iconbitmap(self.fileIco)
        else:
            pass
        
        screenWidth = raiz.winfo_screenwidth()# Ancho del área de visualización
        screenHeight = raiz.winfo_screenheight()# Alto del área de visualización
        if sis== "Windows":
            width= 1000
            height= 1050
        else:
            width= 1000
            height= 1050
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        raiz.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")

        #Label title of the application
        titleLabel= tk.Label(raiz, fg= "red", text= self.labelTitleApp, font= ("jost", 25))
        titleLabel.place(relx= 0.5, y= 25, anchor=CENTER)

        # Label youtube link
        ytdlabel= tk.Label(raiz, text= "Ingresa la URL del video:", font= ("jost", 15))
        ytdlabel.place(relx= 0.5, y= 58, anchor=CENTER)

        # Entry box
        ytEntryText= tk.StringVar()
        ytEntry= tk.Entry(raiz, width= 79, textvariable= ytEntryText)
        ytEntry.place(relx= 0.5, y= 100, anchor=CENTER)
        ytEntry.focus()
        ytEntryText.trace_add("write", cambiar_label_true)

        # Error message
        ytError= tk.Label(raiz, text= "", fg= "red", font= ("jost", 11))
        ytError.place(relx= 0.5, y= 130, anchor=CENTER)

        # Label for rtequest the path in which the video or mp3 file will be stored
        saveLabel= tk.Label(raiz, text= "Guarda el video:", font= ("jost", 15))
        saveLabel.place(relx= 0.5, y= 170, anchor=CENTER)

        # Button for keep the file
        saveEntry= tk.Button(raiz, width= 10, bg= "red", fg= "white", text= "Ruta", takefocus= False, command= abrir_ruta)
        saveEntry.place(x= 10, y= 190)

        # Path error
        rutaError= tk.Label(raiz, text= "Selecciona una ruta", fg= "red", font= ("jost", 8))
        rutaError.place(x= 90, y= 193)

        # Download resolution
        ytRes= tk.Label(raiz, text= "Selecciona calidad de video o solo audio:", font= ("jost", 15))
        ytRes.place(x= 10, y= 245)

        # Combobox of options
        elec= ["Alta definición", "Baja definición", "Solo audio"]
        valElec= tk.StringVar()
        valElec.set(elec[0])
        ytElec= ttk.Combobox(raiz, values= elec, state= "readonly", textvariable= valElec, width= 15)
        ytElec.place(x= 380, y= 250)

        # Video/audio download button
        downBot= tk.Button(raiz, text= "Descargar", width= 10, bg= "#C8C1BF", fg= "white", state= "disabled", takefocus= False, command= descargar_video)
        downBot.place(relx= 0.5, y= 305, anchor=CENTER)

        # Frame for the github repository actions
        frameGithub = tk.Frame(raiz)
        frameGithub.place(relx= 0.5, y= 1030, anchor=CENTER)

        # Label to github repository
        labelGit= tk.Label(frameGithub, text= "Repositorio del programa:", font= ("jost", 10))
        labelGit.pack(side=LEFT)

        # Button to repository
        butGit= tk.Button(frameGithub, width= 10, bg= "red", fg= "white", text= "Repositorio", takefocus= False, command= repo_git)
        butGit.pack(side=RIGHT)

        # Label for showing the thumbnail
        ImaLabel= tk.Label(raiz, image= None)
        ImaLabel.place(x= 20, y= 320)

        # Video info
        thumbTitleLabel= tk.Label(raiz, text= "", font= ("jost", 10), wraplength= 750)
        thumbAuthorLabel= tk.Label(raiz, text= "", font= ("jost", 10))
        thumbDescLabel= tk.Label(raiz, text= "", font= ("jost", 10), wraplength= 750)
        
        thumbTitleLabel.place(x= 225, y= 330)
        thumbAuthorLabel.place(x= 225, y= 370)
        thumbDescLabel.place(x= 225, y= 400)

        raiz.protocol("WM_DELETE_WINDOW", salir)

        raiz.mainloop()