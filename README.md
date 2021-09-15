# Youtube videos and audio downloader
This projects is going to be divided in two parts. A web application and a desktop application.

## Desktop application
The desktop application will be developed with tkinter, so you can download the application in the part of releases ready to be executed in your 
computer without the neccesity to download python. You just need to download the exe file and its going to be ready to be downloaded.
<br>
The command in order to create the exe file with pyinstaller is (Please check firts the considerations in Development mode and Production mode):
```
pyinstaller --noconfirm --onefile --windowed --add-data "C:/Users/Diego/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/moviepy;moviepy/" --add-data "./descargaryt.ico;." --name "ytDownloader" --icon "./descargaryt.ico" "./youtube.py"
```
<br>
If we want to create the executable file using pyinstaller in this specific case that we use pyinstaller for the creation of the same exe file we 
will need to include in the --add-data pyinstaller flag the complete directory of the moviepy library so the program will be executed correctly.
<br>
The pyinstaller command above includes this folder, you should include the path in which you moviepy library is stored in your PC.

### Development mode
If you want to run the code not in an exe mode then comment the next code line below that will appear in the code of the youtube.py script:

``
os.environ["IMAGEIO_FFMPEG_EXE"]= "/usr/bin/ffmpeg"
``

### Production mode
If you want to run the program through the exe file then before executing the pyinstaller command you need to uncomment the next code line below 
in the same part that the code line is en the script:

``
os.environ["IMAGEIO_FFMPEG_EXE"]= "/usr/bin/ffmpeg"
``

## Web application
This application will be developed with the time and will be hosted with the time too so you will be able to access to the web application as a normal 
web application through your internet browser of your preferences and will have the same functionality.

# More content to the README will be uploaded from september 8 and further.
