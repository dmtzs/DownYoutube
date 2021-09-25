try:
    import os
    import sys
    import platform
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

class tkClass():
    banderas= [0, 0]#URL, Ruta guardar
    folderName= ""
    fileName= ""
    fileIco= "descargaryt.ico"

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def commandSOShell(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema
    
    def configWindow(self):
        raiz= tk.Tk()
        comando, sis= self.commandSOShell()
        os.system(comando)
        raiz.title("Descargar videos youtube")
        raiz.columnconfigure(0, weight= 1)
        raiz.resizable(width= False, height= False)
        iconImage= self.resource_path("descargaryt.ico")
        raiz.iconbitmap(iconImage)
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