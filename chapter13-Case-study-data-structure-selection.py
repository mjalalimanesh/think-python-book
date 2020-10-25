from string import punctuation, whitespace
from matplotlib import pyplot as plt
import random
import numpy as np

####################  13_1  #####################


def process_line(line, words):
    """
    Populate a dictionary with single words in a line
    Parameters
    ----------
    line : str
        line to extract words from.
    words : dict
        dictionary which words from line are added to.

    Returns
    -------
    None.

    """
    # line = line.replace("-", " ")
    # line = line.replace("'s", "")
    # line = line.replace("'re", "")
    # line = line.replace("'ll", "")
    # line = line.replace("'m", "")
    # line = line.replace("'ve", "")
    # line = line.replace("'d", "")
    line = line.replace("”", "")
    line = line.replace("“", "")

    line_words = line.split()
    line_words = list(map(lambda x: x.strip(punctuation + whitespace), line_words))
    line_words = list(map(str.lower, line_words))
    line_words = [word for word in line_words if word != ""]
    for word in line_words:
        words[word] = words.get(word, 0) + 1


def process_file(path="emma.txt"):
    """
    Generate a dictionary from a textfile containng words in file 
    as keys and frequency of word as value

    Parameters
    ----------
    path : str, optional
        path for text fiel. The default is "emma.txt".

    Returns
    -------
    words : dict
        dictionary of words and frquencies.

    """
    fin = open(path)
    words = {}
    for i, line in enumerate(fin):
        if i < 45 and i > 16262:
            continue
        process_line(line, words)
    return words


def read_words_to_dic(path="words.txt"):
    """
    read words from a text file with a word in each line to a dict
    """
    fin = open(path)
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = 1
    return d


words = process_file("emma.txt")
word_list = read_words_to_dic("words.txt")

####################  13_2  #####################


print("Exercise 13.2 : ")
print("total number of words words", sum(words.values()))
print("number of unique words", len(words))

# for word in words:
#     if word not in word_list:
#         print(word)

####################  13_3  #####################
def sord_dict_by_value(d):
    """
    sort dictionary, d by values 
    """
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


print("Exercise 13.3 : ")
words_sorted = sord_dict_by_value(words)
most_common = list(words_sorted.items())[0:10]
print("most common words : ")
for word, rep in most_common:
    print(word, rep, sep="\t")

####################  13_5  #####################


def choose_from_hist(hist):
    """
    choose a random key from a dictionary with probabily proportional to 
    their value

    Parameters
    ----------
    hist : dict

    Returns
    -------
    a random key in hist
    """
    keys = np.array(list(hist.keys()))
    values = np.array(list(hist.values()))
    total = np.sum(values)
    range_numbers = np.arange(0, np.size(keys))
    ind = random.choices(k=1, population=range_numbers, weights=(values / total))
    return keys[ind]


print("Exercise 13.5 : ")
print("select random from words with weight : ", choose_from_hist(words))

####################  13_6  #####################

print("Exercise 13.6 -> diff ")
words_set = set(words)
word_list_set = set(word_list)
diff = words_set.difference(word_list_set)

####################  13_8  #####################
print("Exercise 13-8 : ")


def process_str(string_obj):
    """
    Takes an string and returns a processed list of words in
    """
    string_obj = string_obj.replace("”", "")
    string_obj = string_obj.replace("“", "")
    string_obj = string_obj.replace("--", "")

    str_words = string_obj.split()
    str_words = list(map(lambda x: x.strip(whitespace), str_words))
    str_words = [word for word in str_words if word != ""]
    return str_words


def markov_analysis(words_list, prefix_length=1, suffix_length=1):
    """
    markov analysis on a text file words
    Gets an ordered word list (for instance list of words in a book 
    by order of occurence) and returns a dictionary of markov analysis

    Parameters
    ----------
    words_list : list
        list of words to be analyzed.
    prefix_length : int, optional
        length of prefix on markov analysis. The default is 1.
    suffix_length : int, optional (Non-default value NOT FULLY IMPLEMENTED)
        length of prefix in markov analysis . The default is 1.

    Returns
    -------
    d : dict
        keys ore tuple f prefixes and values are lists of suffix strings.

    """
    d = {}
    i = 0
    while i < (len(words_list) - (prefix_length + suffix_length)):
        prefix = tuple(words_list[i : i + prefix_length])
        suffix = " ".join(
            words_list[(i + prefix_length) : (i + prefix_length + suffix_length)]
        )

        if suffix not in d.get(prefix, []):
            d.setdefault(prefix, []).append(suffix)
        i = i + 1
    return d


def next_word(prefix, d):
    ind = random.randint(0, len(d[prefix]) - 1)
    return d[prefix][ind]


def next_prefix(pprefix, next_word):
    from_pprefix = pprefix[-(len(pprefix) - 1) :]
    new_word = tuple(next_word.split())
    return (from_pprefix + new_word)[(-len(pprefix)) :]


def generate_text(prefix, d, sentence_length=30):
    print(" ".join(prefix), end=" ")
    for i in range(sentence_length):
        pprefix = prefix
        nxt_word = next_word(prefix, d)
        print(nxt_word, end=" ")
        prefix = next_prefix(pprefix, nxt_word)


with open("emma.txt", "r") as myfile:
    data = " ".join([line.replace("\n", "") for line in myfile.readlines()[45:16262]])

all_words = process_str(data)
d = markov_analysis(all_words, prefix_length=2, suffix_length=1)

generate_text(("He", "was"), d)

####################  13_9  #####################
print("\nExercise 13-9 : Plot")

d = process_file(path="emma.txt")
d_sorted = sord_dict_by_value(d)
frequencies = list(d_sorted.values())[0:]
ranks = np.arange(1, len(frequencies) + 1)

plt.figure()
plt.scatter(np.log(ranks), np.log(frequencies), marker="+")

