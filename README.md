# Youtube videos and audio downloader
This projects is going to be divided in two parts. A web application and a desktop application.

## Desktop application
The desktop application will be developed with tkinter, so you can download the application in the part of releases ready to be executed in your 
computer without the neccesity to download python. You just need to download the exe file and its going to be ready to be downloaded.
<br>
The command in order to create the exe file with pyinstaller is:
```
pyinstaller --noconfirm --onefile --windowed --add-data "C:/Users/Diego/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/moviepy;moviepy/" --add-data "./descargaryt.ico;." --name "ytDownloader" --icon "./descargaryt.ico" "./youtube.py"
```
<br>
If we want to create the executable file using pyinstaller in this specific case that we use pyinstaller for the creation of the same exe file we 
will need to include in the --add-data pyinstaller flag the complete directory of the moviepy library so the program will be executed correctly.
<br>
The pyinstaller command above includes this folder, you should include the path in which you moviepy library is stored in your PC.

## Web application
This application will be developed with the time and will be hosted with the time too so you will be able to access to the web application as a normal 
web application through your internet browser of your preferences and will have the same functionality.

# More content to the README will be uploaded from september 8 and further.
