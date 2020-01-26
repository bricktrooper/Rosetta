#!/bin/bash

ORIGINAL="$1"
TRANSLATED="$2"

# mute
./ffmpeg -i "$ORIGINAL" -vcodec copy -an tests/muted.mp4

# dub
./ffmpeg -i tests/muted.mp4 -i "$TRANSLATED" -c:v copy -c:a aac -strict experimental tests/dubbed.mp4
