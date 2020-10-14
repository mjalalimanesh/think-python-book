
fruit = 'orangeg'
index = len(fruit)
while index > 0:
    letter = fruit[index-1]
    print(letter, end='\n')
    index = index - 1


def find(word, letter, index=0):
    index = index
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count(word, letter):
    count = 0
    ind = find(word, letter)
    while ind != -1:
        count = count + 1
        ind = find(word, letter, ind+1)
    print(count)


#print(find(fruit, 'n', 4))
#count(fruit, 'g')

####################  8_5  ####################

def rotate_word(s, n):
    rs = ''
    for c in s.lower():
        order = ord(c) + n

        if order > ord('z'):
            diff = ord('z') - ord(c)
            order = ord('a') + (n - diff) - 1

        if order < ord('a'):
            diff = ord(c) - ord('a')
            order = ord('z') + (n + diff) + 1

        rs = rs + chr(order)
    return rs

#a = rotate_word('xyz', 3)
