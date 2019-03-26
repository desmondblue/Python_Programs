#PF-Assgn-56
'''
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.
'''
def max_frequency_word_counter(data):
    word=""
    frequency=0
    temp = data.lower()
    list = temp.split(' ')
    for i in list:
        count = list.count(i)
        if count>frequency:
            frequency = count
            word = i
            
        elif count==frequency:
            if len(word)>len(i):
                continue
            else:
                word =i
    print(word,frequency)


data="Hands to clap and eyes to see"
max_frequency_word_counter(data)
