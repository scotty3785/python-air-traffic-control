# Installing Pygame for Python3 #

Many of the programs that are listed in the MagPi magazine are written using Python3 but also use the Pygame module.
Currently, Pygame works very well for Python 2 and they are working on getting it updated for Python 3 but it isn’t quite ready for general release yet.

But, if you want to work through the programs using your Raspberry Pi and Python 3, here are the steps to take to get it to work.

## Steps to install Pygame ##
  1. Install a bunch of applications including Subversion (also known as SVN) which is an open source version control system.
  1. Download the latest version of Pygame using SVN
  1. Install Pygame using Python.

## Install applications ##
First, open up a shell by double clicking on the LXTerminal icon on the Desktop. Then execute the following:
```
sudo apt-get install python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev 
```

## Download Pygame ##
Note: In order to keep the file system clean, you should create a “build” subdirectory and when you download software that you know will be built or compiled, put it in that directory. To do that, in the shell, execute these commands:

```
cd mkdir builds
cd builds
```

Then do the actual download of Pygame
```
sudo svn co svn://seul.org/svn/pygame/trunk pygame
```

## Install Pygame ##
```
cd pygame
sudo python3 setup.py build 
sudo python3 setup.py install
```


The build step will take quite a while to run.
To test to make sure it worked: Double click on the IDLE 3 icon. This will open a new window titled: Python Shell. You should see something like “Python 3.2.3” on the first line.
At the >>>, type in “import pygame” without the quotes.

If all is well, the cursor will drop to the next line with just >>>.