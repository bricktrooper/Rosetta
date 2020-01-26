from speech2text import Speech2Text
from ffmpeg_test import decode_audio

# create Speech2Text object
s2t = Speech2Text()

# obtain raw audio format
raw_audio = decode_audio("input2.mp4")

# load audio file
s2t.load(raw_audio)

# specify audio file details
s2t.config(
	encoding = Speech2Text.DEFAULT_ENCODING,
	sample_rate = Speech2Text.DEFAULT_SAMPLE_RATE_HERTZ,
	language = Speech2Text.DEFAULT_INPUT_LANGUAGE
	)

# translate and save transcript
s2t.translate("output2")
print()
