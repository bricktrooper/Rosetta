import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class Speech2Text:

	DEFAULT_ENCODING = enums.RecognitionConfig.AudioEncoding.LINEAR16
	DEFAULT_SAMPLE_RATE_HERTZ = 16000
	DEFAULT_INPUT_LANGUAGE = 'en-US'
	DEFAULT_AUDIO_FILE = 'input.flac'

	# CONSTRUCTOR
	def __init__(self):
		print("Initializing Speech-to-Text .......")
		self.client = speech.SpeechClient() # Instantiates a client
		self.audio = None
		self.info = None

	# Loads the audio into memory and returns a handle
	def load(self, raw_audio):
		print("Loading audio file .......")
		self.audio = types.RecognitionAudio(content = raw_audio)

	# sets the audio encoding, sample rate (Hz), and language
	def config(self, encoding, sample_rate, language):
		print("Audio input details:")
		print("Encoding:          %s" % encoding)
		print("Sample Rate (Hz):  %s" % sample_rate)
		print("Language:          %s" % language)
		self.info = types.RecognitionConfig(encoding = encoding, sample_rate_hertz = sample_rate, language_code = language)

	# translates the audio and saves transcript to a file
	def translate(self, file_name):
		print("Translating .......")
		file = open(file_name, "a")
		response = self.client.recognize(self.info, self.audio)
		for result in response.results:
			file.write(result.alternatives[0].transcript)

		print("Saving transcript in '%s' ......." % file_name)
		file.close()
