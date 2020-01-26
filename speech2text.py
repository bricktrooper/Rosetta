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
	return raw_audio

# transcribes the audio to text and saves transcript to a file
def transcribe(input_file = 'input.mp4', output_file = 'transcript', language = 'en-CA'):

	audio_info = types.RecognitionConfig(
		encoding = AUDIO_ENCODING,
		sample_rate_hertz = SAMPLE_RATE,
		language_code = language)

	print("Audio input settings:")
	print("Audio Encoding:    %s" % AUDIO_ENCODING)
	print("Sample Rate (Hz):  %s" % SAMPLE_RATE)
	print("Input Language:    %s" % language)

	print("Converting mp4 to raw audio .......")
	audio = types.RecognitionAudio(content = extract_audio(input_file))

	print("Transcribing .......")
	file = open(output_file, "a")
	response = speech2text_client.recognize(audio_info, audio)
	transcript = ""

	for result in response.results:
		file.write(result.alternatives[0].transcript)
		transcript = transcript + format(result.alternatives[0].transcript)

	print("Saving transcript in '%s' ......." % output_file)
	file.close()

	print(transcript)
	print(format(result.alternatives[0].transcript))
	return transcript
