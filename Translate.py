
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return " ".join( words[word] for word in sentence.split() )

if __name__ == '__main__':
    print(translate("el gato esta en la casa"))