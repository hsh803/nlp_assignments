import sys, re

regex_pattern = r"([\.,;:!?()]|--|``|''|\w+[\.,][\w\.]+|[A-Z]\w*\.|\w+-\w+[-\w]*|[#%&@£$]|\w+(?=n't)|n\'t|\w(?=')|\'?\w+)"


for line in sys.stdin:
    re.sub(r"\"", "''", line)
    #print(line)

    for token in re.findall(regex_pattern, line.strip()):
        if token != ".":
            print(token)
        elif token == ".":
            print(token)
            print()

