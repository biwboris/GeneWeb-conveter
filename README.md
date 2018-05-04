# What it is?

This programm help's you convert GeneWeb base from version 4 to 6. GeneWeb version 4 use ASCII for encoding and version 6 use UTF-8. Also changed image name encoding.

# How to build project

## Dependencies
* python3
* cx_Freeze

## Installation
* Building
    - Run ```python setup.py build``` for new gwconv build.
    - Rename config_example.txt to config.txt and copy to build folder.

* Running
    - Fill config.txt with your paths.
    - Run gwconv.exe for new base6.
    - Run imheal.exe for add new images to base6.
    - Also you can run .py file without building.