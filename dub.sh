#!/bin/bash

ORIGINAL="$1"
TRANSLATED="$2"

# mute
./ffmpeg -i "$ORIGINAL" -vcodec copy -an muted.mp4

# dub
./ffmpeg -i muted.mp4 -i "$TRANSLATED" -c:v copy -c:a aac -strict experimental dubbed.mp4
