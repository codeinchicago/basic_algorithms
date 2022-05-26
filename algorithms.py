"""
Exercise #1
Reverse the list below in-place using an in-place algorithm.
For extra credit: Reverse the strings at the same time.
"""

words = ['this' , 'is', 'a', 'sentence', '.']

# for i in range(len(words), -1, -1):
#     print(i)


def swap_words(words):
    for i in range((len(words))//2):
        words[i], words[-i-1] = words[-i-1], words[i]
        print(words)

# swap_words(words)

"""
Exercise #2
Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.

Example Output:{'in': 1, 'computing': 1, 'a': 5, ...}

"""

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

my_dict = {}

text = a_text.split()

for word in text:
    if word.lower() not in my_dict:
        my_dict[word.lower()] = 1
    elif word.lower() in my_dict:
        my_dict[word.lower()] += 1

print(my_dict)

# z = sorted(my_dict.items())
# print(type(z))

#Sorting dictionary by words, do not want to change dictionary itself.
# print(my_dict.sort(my_dict.keys()))