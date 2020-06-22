# room_status_checker

Quick Overview
--------------

The goal of this project is to display a message, if a room is occupied.

Hardware
--------

### Rasberry
* with Raspbian Buster

### Sensors:
* infrared motion sensor: RPI HC-SR501 (PIR) 

### Display:
* Waveshare 2.9 inch e-Paper module 

### Assembly:
* USB power adaptor (at least ~2,5 A)

Software
--------

Python3 will be used for the development.

### Needed Libs on RPi:
* For Hardware:
  * RPI.GPIO (default)
  * Waveshare e-Paper lib
* debugpy - for remote debugging with VsCode


Development - First Steps
-------------------------

A Python installation of min. 3.7 is needed.
For an easy to use integration, it is suggested to set the Python installation on the system path.
This project is is set up to be used with Microsoft VsCode as an IDE.
Git used as a VCS tool, the latest version should work.
To set a minimal working environment, the following steps are necessary:

* Clone this repo to your local machine
* In VsCode use the File -> Open Workspace function to open the ./.vscode/piWeather.code-workspace
* To install the recommended extensions, go left to the Extensions view and type @recommended and install the workspace recommendations
* restart VsCode and open the Workspace again -> all needed python packages will be installed

There are two launch configurations: local start for windows and attach to remote debugger for the Raspberry Pi.
The tasks are created to deploy the source files on the Raspberry.

### Connect to Raspberry:

The only stable method to connect to the Rapsberry is to explicitly use it's IP address.
It is usually displayed on the e-Paper display.

You can use VNC Viewer to connect to it directly or per SSH.
To use passwordless SSH see https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md
