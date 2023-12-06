def is_alliteration(word1,word2):
   if word1[0]== word2[0]:
      return True
   return False
print("is_alliteration")
print("banan,apple->",is_alliteration("banana","apple"))
print("boy,bat->",is_alliteration("boy","bat"))
print("####################")



def count_vowel(word):
    total=0
    for letter in word:
        if letter in["a","e","i","o","u"]:
         total= total +1 
    return total

print("count_vowel")
print("banana->",count_vowel("banana"))
print("boy->",count_vowel("boy"))
print("####################")

def count_number(number):
   if number in[1,2,3,4,5,6,7,8,9,0]:
      total = total+1
   return total

print("count_number")
print("banana15480->",count_number("banana15480"))
print("12134bo9765y->",count_number("12134bo9765y"))
print("####################")

