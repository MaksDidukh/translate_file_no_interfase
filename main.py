import requests
import json
import time



def translate_text(q, source="ru", target="de", format="text"):
    url = "http://94.231.205.187:5000/translate"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "q": q,
        "source": source,
        "target": target,
        "format": format
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    return response.json()

with open("input.txt", "r", encoding="utf-8") as input_file, \
     open("output.txt", "w", encoding="utf-8") as output_file:

    for line in input_file:
        sentences = line.strip().split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                translation = translate_text(sentence, source="ru", target="de", format="text")
                # time.sleep(1)
                print(f"{sentence}\n{translation['translatedText']}\n\n")
                output_file.write(f"{sentence}\t{translation['translatedText']}\n\n")
                output_file.flush()
