from speech2text import Speech2Text

# create Speech2Text object
s2t = Speech2Text()

# load audio file
s2t.load("sample.flac")

# specify audio file details
s2t.config(
	encoding = Speech2Text.DEFAULT_ENCODING,
	sample_rate = Speech2Text.DEFAULT_SAMPLE_RATE_HERTZ,
	language = Speech2Text.DEFAULT_INPUT_LANGUAGE
	)

# translate and save transcript
s2t.translate("/dev/stdout")
print()