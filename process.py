# Have you ever heard the tragedy of Darth Plagueis the Wise?

from speech2text import *
from translate import *
from text2speech import *
import subprocess
import os

#return 3-tuple, 1st elem = name of translated mp3, 2nd elem = name of translated text, 3rd elem = original text
# call with NO .p4 extension
def process(mp4_file = "trudeau", input_lang = "fr",target_lang ="en"):

	os.system('mkdir -p outputs')

	mp3_translated_name =  mp4_file + "_translated"
	transcript = transcribe(("inputs/" + mp4_file + ".mp4"), ("outputs/" + mp4_file + "_transcript"), addDialect(input_lang))

	translated_script = translate(transcript, "outputs/" + mp3_translated_name, target_lang)
	print(translated_script)

	speak(translated_script, addDialect(target_lang), "outputs/" + mp3_translated_name + ".mp3")

	subprocess.check_call(['./dub.sh', mp4_file, mp3_translated_name])

def addDialect(lang):
	if lang == "en":
		return "en-CA"
	if lang == "fr":
		return "fr-CA"
	if lang == "hi":
		return "hi-IN"
	if lang == "ja":
		return "ja-JP"
	if lang == "es":
		return "es-ES"
	if lang == "cmn":
		return "cmn-CN"



