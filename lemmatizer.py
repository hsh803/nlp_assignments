import sys

def noun_lemma(word):
    if word.endswith("ies"):
        return word.replace("ies", "y")
    elif word.endswith("sses"):
        return word[:-2]
    elif word.endswith("ss") or word.endswith("ness") or word.endswith("ress"):
        return word
    elif word.endswith("es"):
        return word[:-1]
    elif word.endswith("s"):
        return word[:-1]
    else:
        return word

def verb_lemma(word):
    if word.endswith("ied"):
        return word.replace("ied", "y")
    elif word.endswith("ated") or word.endswith("ates"):
        return word[:-1]
    elif word.endswith("eed"):
        return word[:-1]
    elif word.endswith("lized") or word.endswith("lizes"):
        return word[:-1]
    elif word.endswith("ed"):
        return word[:-2]
    elif word.endswith("ying"):
        return word[:-3]
    elif word.endswith("ing"):
        return word[:-3]
    elif word.endswith("es"):
        return word[:-1]
    elif len(word) > 3 and word.endswith("s"):
        return word[:-1]
    elif word == "did" or word == "done" or word == "does":
        word = "do"
        return word
    elif word == "has" or word == "had" or word == "'ve":
        word = "have"
        return word
    elif word == "am" or word == "are" or word == "is" or word == "was" or word == "were" or word == "'s" or word == "'m" or word == "'re" or word == "being" or word == "been":
        word = "be"
        return word
    else:
        return word

def adj_lemma(word):
    if word.endswith("er"):
        return word[:-2]
    elif word.endswith("est"):
        return word[:-3]
    else:
        return word

def aux_lemma(word):
    if word == "am" or word == "are" or word == "is" or word == "was" or word == "were" or word == "'s" or word == "'m" or word == "'re" or word == "being" or word == "been":
        word = "be"
        return word
    elif word == "does" or word == "did" or word == "done":
        word = "do"
        return word
    elif word == "had" or word == "has" or word == "'ve":
        word = "have"
        return word
    else:
        return word

def pron_lemma(word):
    if word == "me":
        word = "I"
        return word
    elif word == "your":
        word = "you"
        return word
    elif word == "his" or word == "him":
        word = "he"
        return word
    elif word == "her":
        word = "she"
        return word
    elif word == "their" or word == "them":
        word = "they"
        return word
    else:
        return word

def part_lemma(word):
    if word == "n't":
        word = "not"
        return word
    else:
        return word

def det_lemma(word):
    if word == "an":
        word = "a"
        return word
    else:
        return word

for line in sys.stdin:
    if line.strip():
        (word, tag) = line.strip().split("\t")
        lemma = word
        if tag == "NOUN":
            lemma = noun_lemma(word)
        elif tag == "VERB":
            lemma = verb_lemma(word)
        elif tag == "ADJ":
            lemma = adj_lemma(word)
        elif tag == "AUX":
            lemma = aux_lemma(word)
        elif tag == "PRON":
            lemma = pron_lemma(word)
        elif tag == "PART":
            lemma = part_lemma(word)
        elif tag == "DET":
            lemma = det_lemma(word)
        else: 
            lemma = word
        print("{0}\t{1}\t{2}".format(word, tag, lemma))
    else:
        print()
