# Youtube videos and audio downloader
This projects is going to be divided in two parts. A web application and a desktop application.

## Desktop application
The desktop application will be developed with tkinter, so you can download the application in the part of releases ready to be executed in your 
computer without the neccesity to download python. You just need to download the exe file and its going to be ready to be downloaded.
<br>
The command in order to create the exe file with pyinstaller is:
```
pyinstaller --noconfirm --onefile --windowed --add-data "D:/DownYoutube/DesktopApp/descargaryt.ico;." --name "ytDownloader" --icon "./descargaryt.ico" "./youtube.py"
```
<br>
If we want to create the executable file we will need to change some files directly in the same library of moviepy.
<br>
We will need to go to the path in which the library is, in my case is in the next paths:

* C:\Users\Diego\AppData\Local\Programs\Python\Python39\Lib\site-packages\moviepy\audio\fx\all\__init.py__
* C:\Users\Diego\AppData\Local\Programs\Python\Python39\Lib\site-packages\moviepy\video\fx\all\__init.py__

Then we need to paste the next code in the __init__.py file of the audio:

```python
#import pkgutil

import moviepy.audio.fx as fx

#__all__ = [name for _, name, _ in pkgutil.iter_modules(
    #fx.__path__) if name != "all"]

#for name in __all__:
    #exec("from ..%s import %s" % (name, name))
    #print("from moviepy.audio.fx import %s" % (name))

from moviepy.audio.fx import audio_fadein
from moviepy.audio.fx import audio_fadeout
from moviepy.audio.fx import audio_left_right
from moviepy.audio.fx import audio_loop
from moviepy.audio.fx import audio_normalize
from moviepy.audio.fx import volumex
```
An then we need to paste the next code in the __init__.py file of the video:

```python
#import pkgutil

import moviepy.video.fx as fx

#__all__ = [name for _, name, _ in pkgutil.iter_modules(
    #fx.__path__) if name != "all"]

#for name in __all__:
    #exec("from ..%s import %s" % (name, name))
    #print("from moviepy.video.fx import %s" % (name))

from moviepy.video.fx import accel_decel
from moviepy.video.fx import blackwhite
from moviepy.video.fx import blink
from moviepy.video.fx import colorx
from moviepy.video.fx import crop
from moviepy.video.fx import even_size
from moviepy.video.fx import fadein
from moviepy.video.fx import fadeout
from moviepy.video.fx import freeze
from moviepy.video.fx import freeze_region
from moviepy.video.fx import gamma_corr
from moviepy.video.fx import headblur
from moviepy.video.fx import invert_colors
from moviepy.video.fx import loop
from moviepy.video.fx import lum_contrast
from moviepy.video.fx import make_loopable
from moviepy.video.fx import margin
from moviepy.video.fx import mask_and
from moviepy.video.fx import mask_color
from moviepy.video.fx import mask_or
from moviepy.video.fx import mirror_x
from moviepy.video.fx import mirror_y
from moviepy.video.fx import painting
from moviepy.video.fx import resize
from moviepy.video.fx import rotate
from moviepy.video.fx import scroll
from moviepy.video.fx import speedx
from moviepy.video.fx import supersample
from moviepy.video.fx import time_mirror
from moviepy.video.fx import time_symmetrize
```
All the settings shown above will not affect the normal operation of the moviepy library.

## Web application
This application will be developed with the time and will be hosted with the time too so you will be able to access to the web application as a normal 
web application through your internet browser of your preferences and will have the same functionality.

# More content to the README will be uploaded from september 8 and further.
