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

def count_number(word):
    total=0
    for number in word:
       if number in "1,2,3,4,5,6,7,8,9,0":
        total = total + 1
    return total

print("count_number")
print("banana15480->",count_number("banana15480"))
print("12134bo9765y->",count_number("12134bo9765y"))
print("####################")


def count_target_letters(word,character):
   total= 0
   for characters in word:
      if characters in character:
         total=total+1 
   return total 

print("count_target letter")
print("cat->",count_target_letters("cat","a"))
print("banana->",count_target_letters("banana","a"))
print("->",count_target_letters("","a"))
print("####################")

def in_alphabetical_order(letters):
   previos =letters[0]
   for letter in letters:
      if letter < previos:
         return False
      previos = letter
   return True 

print("in_a_order")
print("a,b,c,d",in_alphabetical_order("abcd"))
print("p,x,l",in_alphabetical_order("pxl"))
print("h,i,j,k",in_alphabetical_order("hijk"))
print("####################")

def alternate_case(word):
   nextupper=True
   result=""
   for letters in word:
      if nextupper== True:
         result= result + letters.upper()
         nextupper= False
      elif nextupper== False:
         result= result+ letters
         nextupper= True
   return result 
   
print("alternate_case")
print("hello",alternate_case("hello"))
print("bye now",alternate_case("bye now"))
print("good monring ",alternate_case("good morning"))
print("####################")

def remove_vowels(letters):
   result= ""
   for letter in letters:
      if letter in "aeiou":
         pass
      else:
         result=result+letter
   return result 
print("remove_vowels")
print ("apple=>",remove_vowels("apple"))
print ("banana=>",remove_vowels("banana"))
print ("elephant=>",remove_vowels("elephant"))
print("####################")

def to_camle_case(word):
   result=""
   nextupper=True
   for letter in word:
      if nextupper== True:
         result= result + letter.upper()
         nextupper= False
      elif nextupper== False:
         pass
      nextupper= True
   return result
print("to_camle_case")
print ("apple fish=>",to_camle_case("apple fish"))
print ("banana cat=>",to_camle_case("banana cat"))
print ("elephant dog=>",to_camle_case("elephant dog"))
print("####################")


def to_snake_case(word):
  return '_'.join(word.split())
print("to_snake_case")
print("hello world, it it a good day=>",to_snake_case("hello world, it it a good day"))
print("####################")


def filter_valid_act_scores(list):
   validact=  0
   for act in list:
        if act >= 1 and act<= 36:
          validact= validact+ act
   return validact 

print("filter_valid_act_scores")
print ("30,20,34,56,78,2,1,0,-5=>",filter_valid_act_scores(30,20,34,56,78,2,1,0,-5))
print("####################")



