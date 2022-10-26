# Introduction

This project was just something that was always on the back burner, since I was trying to learn Qt (and PyQt5) on the side. Finally in a somewhat-usable state!

# Install

- Create a virtualenv with `python3 -m venv. venv`. If the venv module doesn't exist, `sudo apt install python3-venv` or the equivalent for your distro should do it.
- Get into it. `source .venv/bin/activate` works on bash shell.
- Install the dependencies using `python3 -m pip install -r requirements.txt`.
- Run program with `python3 widget.py`.

# Dependencies

- [pycryptodome](https://pypi.org/project/pycryptodome/)
- [gmpy](https://pypi.org/project/gmpy/)
- [SymPy](https://pypi.org/project/sympy/)
- [requests](https://pypi.org/project/requests/)
- [pwntools](https://pypi.org/project/pwntools/)
- [PyQt5](https://pypi.org/project/PyQt5/)

# Thanks

- To [@malladisiddu](https://github.com/malladisiddu/) for the original project.
- [Mastering Qt5](https://www.packtpub.com/product/mastering-qt-5/9781786467126) to help me get my feet wet with Qt5 in general.
- StackOverflow for obvious reasons.

# FAQ

- *gmpy2 install fails*: You need to install libgmp. `sudo apt install libgmp-dev` works for Debian-based distros.
