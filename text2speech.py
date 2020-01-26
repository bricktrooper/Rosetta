"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/

"""

from google.cloud import texttospeech

OUTPUT_AUDIO_ENCODING = texttospeech.enums.AudioEncoding.MP3
OUTPUT_LANGUAGE = 'en-US'
OUTPUT_AUDIO_VOID_GENDER = texttospeech.enums.SsmlVoiceGender.NEUTRAL
OUTPUT_AUDIO_FILE = 'output.mp3'

# Instantiates a client
text2speech_client = texttospeech.TextToSpeechClient()

def speak(translated_string, lang = 'en-US'):

        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text = translated_string)

        # Build the voice request, select the language code ("en-US") and the ssml
        voice = texttospeech.types.VoiceSelectionParams(language_code = lang, ssml_gender = OUTPUT_AUDIO_VOID_GENDER)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(audio_encoding = OUTPUT_AUDIO_ENCODING)

        # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
        response = text2speech_client.synthesize_speech(synthesis_input, voice, audio_config)

        # The response's audio_content is binary.
        with open(OUTPUT_AUDIO_FILE, 'wb') as out:
                # Write the response to the output file.
                out.write(response.audio_content)
                print('Audio content written to file %s' % OUTPUT_AUDIO_FILE)
