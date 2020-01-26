# Have you ever heard the tragedy of Darth Plagueis the Wise?

from translate import translate
from text_2_speech import text_2_speech

transcript = "change this value later"

translated_product = translate(transcript)
translated_transcript = translated_product[0]
lang = translated_product[1] 

text_2_speech(translated_transcript,lang)

