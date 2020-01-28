#!/bin/bash

ORIGINAL="$1"
TRANSLATED="$2"

# mute
./ffmpeg -i "inputs/${ORIGINAL}.mp4" -vcodec copy -an "outputs/${ORIGINAL}_muted.mp4"

# dub
./ffmpeg -i "outputs/${ORIGINAL}_muted.mp4" -i "outputs/${TRANSLATED}.mp3" \
		 -c:v copy -c:a aac -strict experimental "outputs/${ORIGINAL}_dubbed.mp4"
