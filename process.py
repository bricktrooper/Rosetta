# Have you ever heard the tragedy of Darth Plagueis the Wise?

from speech2text import *
from translate import *
from text2speech import *

#return 3-tuple, 1st elem = name of translated mp3, 2nd elem = name of translated text, 3rd elem = original text
# call with NO .p4 extension
def textualize(mp4_file = "", input_lang= "fr",target_lang="en-US"):
    transcript = transcribe(mp4_file, "tests/translated", addDialect(input_lang))
    translated_script = translate(transcript, target_lang)
    print(translated_script)
    return (transcript, translated_script)

def addDialect(lang):
	if lang=="en":
		return "en-CA"
	if lang=="fr":
		return "fr-CA"
	if lang=="hi":
		return "hi-IN"
	if lang=="ja":
		return "ja-JP"
	if lang=="es":
		return "es-ES"
	if lang=="cmn":
		return "cmn-CN"



