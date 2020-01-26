# I AM the Senate

import io
import os
import ffmpeg
import sys

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

AUDIO_ENCODING = enums.RecognitionConfig.AudioEncoding.LINEAR16
SAMPLE_RATE = 16000   # (in Hertz)
INPUT_LANGUAGE = 'en-US'
VIDEO_FILE = 'input2.mp4'

audio_info = types.RecognitionConfig(
		encoding = AUDIO_ENCODING,
		sample_rate_hertz = SAMPLE_RATE,
		language_code = INPUT_LANGUAGE)
speech2text_client = speech.SpeechClient()

# decodes an mp4 video into raw audio
def extract_audio(in_filename, **input_kwargs):
	try:
		raw_audio, err = (ffmpeg
			.input(in_filename, **input_kwargs)
			.output('-', format = 's16le', acodec = 'pcm_s16le', ac = 1, ar = '16k')
			.overwrite_output()
			.run(capture_stdout = True, capture_stderr = True)
		)
	except ffmpeg.Error as e:
		print(e.stderr, file = sys.stderr)
		sys.exit(1)
	return types.RecognitionAudio(content = raw_audio)

# transcribes the audio to text and saves transcript to a file
def transcribe(file_name):
	print("Audio input settings:")
	print("Audio Encoding:    %s" % AUDIO_ENCODING)
	print("Sample Rate (Hz):  %s" % SAMPLE_RATE)
	print("Input Language:    %s" % INPUT_LANGUAGE)

	print("Converting mp4 to raw audio .......")
	audio = extract_audio(VIDEO_FILE)

	print("Transcribing .......")
	file = open(file_name, "a")
	response = speech2text_client.recognize(audio_info, audio)
	for result in response.results:
		file.write(result.alternatives[0].transcript)

	print("Saving transcript in '%s' ......." % file_name)
	file.close()
