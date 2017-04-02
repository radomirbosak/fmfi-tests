FMFI tests
==========

This is a static webpage written in python. It provides old tests/exams (písomky) for students of matfyz in Bratislava.

It uses the [Bottle](http://bottlepy.org/docs/dev/index.html) framework. It creates a local webserver on localhost.

A running instance of this can be found on [fmfi.rbos.sk](http://fmfi.rbos.sk).

![screenshot](scr.png)

Running
-------
```console
$ cd fmfi
$ python3 fmfimain.py
```

Running in docker container
---------------------------
```console
$ docker build -t fmfi .
$ docker run -p 8080:80 fmfi
```

Note to content
---------------
Note that only the `"Matematická analýza (1)"` link works correctly in this repository. To make other links functional, create the corresponding directories and files under `fmfi/files/`, the `title.csv` file. See the `fmfi/files/ma1` directory for reference.

To change the the list of subjects, edit the `fmfi/predmety.py` file.

Dependencies
------------
* python3-bottle