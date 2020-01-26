# Have you ever heard the tragedy of Darth Plagueis the Wise?

from speech2text import *
from translate import *
from text2speech import *

transcript = transcribe("tests/trudeau.mp4", "tests/translated", "fr-CA")

str2 = translate(transcript, "en")
print(str2)

speak(str2, "en-CA", "tests/translated.mp3")
