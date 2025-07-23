from googletrans import Translator

translator = Translator()
txt = input("Enter a text :")
output = translator.translate(txt,dest='en')  # use translate(), not Translator()
print(output.text)

