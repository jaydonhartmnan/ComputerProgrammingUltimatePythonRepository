import csv
import os

# allow files to be read from the current location
os.chdir(os.path.dirname(os.path.abspath(__file__)))


f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()


def find_longest_word(wordlist):
    most_vowels_so_far = ""
    wordvowels=0
    for words in wordlist:
        if wordvowels in ("aeiou"):
          wordvowels = wordvowels+1
        if len(wordvowels) > len(most_vowels_so_far):
            most_vowels_so_far = wordvowels
    return most_vowels_so_far

#print(find_longest_word(words))


f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()

def average_word_length(wordlist):
    letters= 0
    wordcount= 0
    average=0
    for word in words:
        wordcount= wordcount+1
        letters= letters+len(word)
    average= letters/wordcount
    return average

print(average_word_length(words))

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
a=0
b=0
c=0
d=0
f=0
for row in reader:
    name, gradelevel, percent = row
    percent= int(percent)
    if percent> 89:
        a=int(a+1)
    if percent> 79:
        b=int(b+1)
    if percent> 69:
        c=int(c+1)
    if percent> 59:
        d=int(d+1)
    if percent< 60:
        f=int(f+1)
print("a,b,c,d,e->",a,b,c,d,f)

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
failingseniors=""

for row in reader:
    name, gradelevel, percent = row
    percent= int(percent)
    gradelevel=int(gradelevel)
    if gradelevel== 12 and percent< 60:
        failingseniors= failingseniors+"  " + name
print("faling seniors->",failingseniors)



    