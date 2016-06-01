# Skylines-pictures
tool for including pictures in Skylines flight comments.

It uses a publicly accessibly folder in Dropbox to host the pictures and creates thumbnails. These are then assembled in a block of markdown code which can be pasted directly in the comment box on Skylines.

## Prerequisites
- Dropbox
- Python

## Steps
1. Make a skylines folder: dropbox/Public/skylines
2. Make a folder to store the pictures of that particular flight (e.g skylines/awesome_flight)
3. copy `skylines_script.py` in this folder
4. run `python skylines_script.py`
