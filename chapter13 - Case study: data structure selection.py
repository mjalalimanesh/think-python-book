from string import punctuation, whitespace

################################################
####################  13_1  #####################
################################################

fin = open('kafka.txt')

words = []
for i, line in enumerate(fin):
    if i < 40:
        continue
    line_words = line.split()
    line_words = list(map(str.strip, line_words))
    line_words = list(map(lambda x: x.strip(punctuation), line_words))
    line_words = list(map(str.lower, line_words))
    line_words = [word for word in line_words if word != ""]

    words.extend(line_words)

words_set = set(words)
