"""
Exercise #1
Reverse the list below in-place using an in-place algorithm.
For extra credit: Reverse the strings at the same time.
"""

words = ['this' , 'is', 'any', 'sentence', '.']

def swap_words(words):
    for i in range((len(words))//2):
        words[i], words[-i-1] = words[-i-1][::-1], words[i][::-1]
    #Need to swap the middle for lists of odd length.
    if len(words) % 2 != 0:
        words[len(words)//2]= words[len(words)//2][::-1]
    
    print(words)


# test = 'alphabet'
# print(test[::-1])

swap_words(words)

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

## Exercise #3

"""
Write a function implementing a Linear Search Algorithm. A linear search is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched. If you do not find a match, return -1
"""

nums_list = [10,23,45,70,11,15,'a']
target = 70

def linear_search(nums_list, target):
    for num in nums_list:
        if num == target:
            return True
    return -1

print(linear_search(nums_list, 70))
print(linear_search(nums_list, 75))
print(linear_search(nums_list, 'a'))

# If number is not present return -1
            