#!/bin/bash

ORIGINAL="$1"
TRANSLATED="$2"
DUBBED="$3"

temp_file=$(mktemp)

# mute
./ffmpeg -i "$ORIGINAL" -vcodec copy -an $temp_file".mp4"

# dub
./ffmpeg -i $temp_file".mp4" -i "$TRANSLATED" -c:v copy -c:a aac -strict experimental static/"$DUBBED"

rm ${temp_file}
