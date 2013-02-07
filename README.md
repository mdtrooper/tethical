Tethical
========

Tethical is a tactical RPG engine with online gaming support. If you don't know what is a tactical RPG, take a look at Final Fantasy Tactics or Disgaea.
See the homepage at (http://tethical.kivutar.me).

Installation instructions for the developpers (Ubuntu Maverick)
---------------------------------------------

Add the following PPA to your sources.list:

    deb http://ppa.launchpad.net/panda3d/ppa/ubuntu maverick main

Install the dependancies

    sudo aptitude install panda3d 

Get the source code

    git clone git@github.com:Kivutar/tethical.git

Launch the server

    cd server
    python main.py

Launch the client

    cd client
    python main.py

Natty users should launch the client using python2.6

Installation Panda3D instructions (Linux Mint 13)
---------------------------------------------
Download Panda3D (SDK 1.8.0 For Ubuntu Oneiric):

https://www.panda3d.org/download/panda3d-1.8.0/panda3d1.8_1.8.0~oneiric_amd64.deb
https://www.panda3d.org/download/panda3d-1.8.0/panda3d1.8_1.8.0~oneiric_i386.deb

Download the packages dependencies:
http://packages.ubuntu.com/oneiric/libhighgui2.1
http://packages.ubuntu.com/oneiric/libcv2.1


Installation instructions for the testers
-----------------------------------------

Get the [panda3d runtime](http://www.panda3d.org/download.php?runtime&version=devel) for your OS and install it.

Download the [game client](http://cv.kivutar.me/tethical/tethical.p3d) and launch it.

in the actual state of the developpement, the server may be offline due to bugs or security issues, find me on the support channel (Kivutar @ #ffh on irc.esper.net) to get the server running.

