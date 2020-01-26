#!/bin/bash

#run this if gcloud installation stuff


gcloud components update
gcloud components install app-engine-pythons
# run this if you get python library errors
# DEW IT !!!!!!!!!!!!!

pip install google-cloud-translate==2.0.0
pip install ffmpeg
pip install ffmpeg-python
pip install google-cloud-texttospeech

