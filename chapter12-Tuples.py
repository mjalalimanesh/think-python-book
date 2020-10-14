def sum_all(*args):
    s = 0
    for arg in args:
        s = s + arg
    return s


####################  12_1  ####################
def most_frequent(s):
    d = histogram(s)
    for key, value in sorted(d.items(), key=lambda item: item[1], reverse=True):
        print(key, value)


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


print("12-1 : ")
most_frequent("helloworls!")

####################  12_2  ####################


def anagram_sets(path="words.txt"):
    fin = open(path)
    d = dict()
    for line in fin:
        word = line.strip()
        key = "".join(sorted(word))
        if key not in d:
            d.setdefault(key, []).append(word)
        else:
            d[key].append(word)
    return d


def anagram_sets_in_order(path="words.txt"):
    fin = open(path)
    d = dict()
    for line in fin:
        word = line.strip()
        key = "".join(sorted(word))
        if key not in d:
            d.setdefault(key, []).append(word)
        else:
            d[key].append(word)
    b = sorted(d.items(), key=lambda item: len(item[1]), reverse=True)
    return dict(b)


def select_n_char_anagrams(n, path="words.txt"):
    d = anagram_sets(path)
    new_dict = {}
    for key in d:
        if len(key) == n and len(d[key]) > 1:
            new_dict[key] = d[key]
    b = sorted(new_dict.items(), key=lambda item: len(item[1]), reverse=True)
    return dict(b)


dic = anagram_sets()
print(select_n_char_anagrams(12, path="words.txt"))

####################  12_3  ####################


def read_words_to_dic(path="words.txt"):
    fin = open(path)
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = 1
    return d
