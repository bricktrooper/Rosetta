# Have you ever heard the tragedy of Darth Plagueis the Wise?

from speech2text import *
from translate import *
from text2speech import *
import subprocess

#return 3-tuple, 1st elem = name of translated mp3, 2nd elem = name of translated text, 3rd elem = original text
# call with NO .p4 extension
def process(mp4_file= "tests/trudeau", input_lang= "fr",target_lang="en"):

    transcript = transcribe((mp4_file+".mp4"), mp4_file+".txt", addDialect(input_lang))

    translated_script = translate(transcript, target_lang)
    print(translated_script)

    mp3_translated_name =  mp4_file+"_translated.mp3"
    speak(translated_script, addDialect(target_lang), mp3_translated_name)

    ogFile = mp4_file+".mp4"


    #subprocess.call("./dub.sh ogFile mp3_translated_name")



    
    subprocess.check_call(['./dub.sh', ogFile, mp3_translated_name])



   # return (dub.mp4, translated_script, transcript)

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



