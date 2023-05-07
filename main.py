import time
from googletrans import Translator

translator = Translator()
print("You need rename file!\n Need name:  input.txt")
dest = input("What language do you want to translate into?: ru/de/en/fr/es/pl:")

def translate_text(sentence, dest=dest):
    while True:
        try:
            translation = translator.translate(str(sentence), dest=dest)
            return translation.text
        except Exception as e:
            # Handle the error
            print(sentence)
            print(" ")
            print(f"Error occurred: {e}")
            time.sleep(3)  # Ждем 1 секунду перед повторной попыткой

with open("input.txt", "r", encoding="utf-8") as input_file, \
     open("output.txt", "w", encoding="utf-8") as output_file:

    for line in input_file:
        sentences = line.strip().split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                translation = translate_text(sentence)
                print(f"{sentence}\n{translation}\n\n")
                output_file.write(f"{sentence}\n{translation}\n\n")
                output_file.flush()
