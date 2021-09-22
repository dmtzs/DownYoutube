<p align="center">
  <img width="200" src="https://github.com/dmtzs/DownYoutube/blob/master/ytImage.png">
  <h1 align="center" style="margin: 0 auto 0 auto;">Youtube downloader app</h1>
  <h5 align="center" style="margin: 0 auto 0 auto;">Videos and audio downloader</h5>
</p>

<p align="center">
    <img src="https://img.shields.io/github/last-commit/dmtzs/DownYoutube">
    <img src="https://img.shields.io/github/issues/dmtzs/DownYoutube?label=issues">
    <img src="https://img.shields.io/github/stars/dmtzs/DownYoutube">
</p>

## The project
This projects is going to be divided in two parts. A web application and a desktop application.
<br>
You will be able to download videos in mp4 format in the highest or lower quality and mp3 audio format from youtube 
and yes, it works also for very long videos of one hour!!!.

## Desktop application
The desktop application will be developed with tkinter, so you can download the application in the part of releases ready to be executed in your 
computer without the neccesity to download python. You just need to download the exe file and its going to be ready to be downloaded.
<br>
ITS IMPORTANT TO MENTION THAT FOR NOW BECAUSE THE MOVIEPY LIBRARY DOESNT WORK FINE WITH PYINSTALLER THERE IS NOT GOING TO BE A EXE FILE FOR NOW 
JUST UNTIL THIS BUG IS FIXED BY THE CREATOR OF MOVIEPY LIBRARY. MEANWHILE YOU CAN TRY BY YOURSELF AND PLEASE IF YOU HAVE SUCESS TELL WHAT YOU DO.
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

# This app is still on development and more improvements will be added.
