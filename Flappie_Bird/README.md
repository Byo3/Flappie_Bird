# Flappy Bird 🐤:
Building a clone of flappy bird from scratch using python.
It was using one file, to simplify the project.

To rendering it uses a classic library of Python
called Pygame.
For execute the game for itself, it is necessary execute this command below,
in case that you do not have installed the library yet.

Select the path where you are going to install.
for example:

``/home/my_user/directory_where_I_installed``

All you have to do is create a virtual environment for python

# For Linux Edition🐧

## Checks if you have python installed 🐍.

### `` python --version``

### If you already have Python installed:

first, you have to access the directory.

``cd /home/my_user/directory_where_I_installed/FlappyBird``

``python -m venv .venv``

active the environment:

``source .venv/bin/activate``

``pip install pygame``

### if you do not have Python execute:

| Arch                 | Debian              |
|----------------------|---------------------|
| ``sudo pacman -Syu`` | ``sudo apt update`` |


if it returned **"command not found"** or similar, execute
these lines below:


| Arch                      | Debian                      |
|---------------------------|-----------------------------|
| ``sudo pacman -S python`` | ``sudo apt install python`` |


