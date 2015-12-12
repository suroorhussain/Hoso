import random

def generate_status():
    f=open("/usr/share/dict/words")
    words = []
    for i in f:
        i = i.strip()
        if i.isalpha() and len(i):
            words.append(i.lower())
            
    number = random.randint(7, 30)
    sentence = []
    for i in range(number):
        sentence.append(random.choice(words))
    return ' '.join(sentence)
