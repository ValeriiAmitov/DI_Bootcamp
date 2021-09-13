from typing import Text
from googletrans import Translator

translator = Translator()
translations = translator.translate(['Bonjour', 'Au revoir', 'Bienvenue', 'A bientôt'], dest='en')

for i in translations:
    print(i.origin, '=>', i.text)