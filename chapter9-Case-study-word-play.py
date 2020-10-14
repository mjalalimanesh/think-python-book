"""
Created on Fri Apr 24 17:18:59 2020
@author: mohamad jalalimanesh
"""
# %%
###################  9_1  #####################
fin = open("words.txt")
num_lines = sum([1 for line in open("words.txt")])

count = 0
for line in fin:
    word = line.strip()
    if len(word) >= 20:
        count = count + 1
print("9_1 - Count Words with more than 20 char : ", count)

# %%
###################  9_2  #####################
fin = open("words.txt")
num_lines = sum([1 for line in open("words.txt")])


def has_no_e(word):
    return "e" not in word


count = 0
for line in fin:
    word = line.strip()
    if has_no_e(word):
        count = count + 1

print("9_2 - Percentage Words with 'e' : ", count / num_lines)

# %%
###################  9_3  #####################

fin = open("words.txt")
num_lines = sum([1 for line in open("words.txt")])


def avoids(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True


# forbidden_letters = input("enter forbidden letters \n")
forbidden_letters = "aeios"

count = 0
for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters):
        count = count + 1

print(
    "9_3 - Percentage of words that avoids  ",
    forbidden_letters,
    " : ",
    count / num_lines,
)  # aeios

# %%
###################  9_4  #####################

fin = open("words.txt")
num_lines = sum([1 for line in open("words.txt")])


def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


count = 0
letters = "acefhlo"
for line in fin:
    word = line.strip()
    if uses_only(word, letters):
        #        print(word)
        count = count + 1

print("9_4 - Percentage Words that use only 'acefhlo' : ", count / num_lines)


# %%
####################  9_5  #####################
fin = open("words.txt")
num_lines = sum([1 for line in open("words.txt")])


def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True


count = 0
letters = "aeiou"
for line in fin:
    word = line.strip()
    if uses_all(word, letters):
        #       print(word)
        count = count + 1

print("9_4 - Percentage Words that use all 'aeiou' : ", count / num_lines)

# %%
###################  9_5  #####################

fin = open("words.txt")
num_lines = sum([1 for line in open("words.txt")])


def is_abecedarian(word):
    word = word.lower()
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


def is_abecedarian_recursive(word):
    word = word.lower()
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    is_abecedarian_recursive(word[1:])


count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        #       print(word)
        count = count + 1

print("9_5 - Number of abced.. Words : ", count)

# %%
###################  9_7  #####################

fin = open("words.txt")
num_lines = sum([1 for line in open("words.txt")])


def have_three_doubles(word):
    word = word.lower()
    num_doubles = 0
    i = 0
    while i < (len(word) - 1):
        if word[i] == word[i + 1]:
            num_doubles = num_doubles + 1
            i = i + 2
            if num_doubles > 2:
                return True
            continue
        i = i + 1 - 2 * num_doubles
        num_doubles = 0
    return False


print("---------------------------------\n ex9.7 \n---------------------------------")
for line in fin:
    word = line.strip()
    if have_three_doubles(word):
        print(word)

# %%
##################  9_8  #####################


def is_palindrome(word):
    return word == word[::-1]


print("----------------------------------\n ex9.8 \n----------------------------------")
for i in range(100000, 1000000):
    conditions = [False for j in range(4)]
    conditions[0] = is_palindrome(str(i)[2:])
    conditions[1] = is_palindrome(str(i + 1)[1:])
    conditions[2] = is_palindrome(str(i + 2)[1:-2])
    conditions[3] = is_palindrome(str(i + 3)[:])
    if all(conditions) == True:
        print(i)

print("**********************************")
