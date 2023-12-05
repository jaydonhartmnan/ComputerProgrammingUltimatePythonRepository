def count_failing_grades(grades):
    count=0 
    for grade in grades:
        if grade < 60:
          count= count + 1
    return count
    
inputlist1 = [40, 80, 71, 26, 93]
returnValue = count_failing_grades(inputlist1)
print("There are this many failing grades",(returnValue))
print("######################################")
print("")


def count_act_score(list):
   validact=  0
   for act in list:
        if act >= 1 and act<= 36:
          validact= validact + 1
   return validact 

inputlist2 = [-5, 24, 31, 56, 25]
returnValue = count_act_score(inputlist2)
print("This many valid act scores=",(returnValue))
print("######################################")
print("")

def num_sum(list):
   total= 0
   for number in list:
    total = total + number 
   return total

inputlist3 = [-5, 24, 31, 56, 25]
returnValue = num_sum(inputlist3)
print("Number sum=",(returnValue))
print("######################################")
print("")

def avergage_act_score(list):
   validact=  0
   mean=0
   count=0
   for act in list:
      for act in list:
        if act >= 1 and act<= 36:
          validact= validact + act
          count= count + 1
      mean= validact/count
      return mean
   
inputlist4 = [-5, 24, 31, 56, 25]
returnValue = avergage_act_score(inputlist4)
print("Avergage act score=",(returnValue))
print("######################################")
print("")

def all_true(list):
   for item in list:
       if item not in["True"]:
        return False
   return True 
   
inputlist5 = ["True","False","True","True"]
returnValue = all_true(inputlist5)
print("True,False,True,True-All true=",(returnValue))
print("######################################")
print("")

def any_true(list):
   for item in list:
      if item in ["True"]:
         return True
      
inputlist6 = ["True","False","True","True"]
returnValue = any_true(inputlist6)
print("True,False,True,True-Any true=",(returnValue))
print("######################################")
print("")

truecount=0
falsecount=0
def mostly_true(list):
   for item in list:
      if item in list=="True":
         truecount== truecount + 1
   for item in list:
      if item in list=="False":
         falsecount==falsecount + 1
   if truecount > falsecount:
      return True 
   else:
      return False
print("mostly tue demo")
inputlist7 = ["Falsee","False","False","True"]
returnValue = mostly_true(inputlist7)
print("False,False,False,True-mostly true=",(returnValue))
print("######################################")
print("")

def has_vowel(input):
   for item in input:
      if item in"a, e, , i u, o":
         return True
      
   return False
inputlist8 = ["e"]
inputlist9 = ["a"]
print("has a vowel demo")
returnValue = has_vowel(inputlist8)
print("e=",(returnValue))
returnValue1 = has_vowel(inputlist9)
print("a=",(returnValue1))

print("######################################")
print("")

def all_the_same(list):
   first= list[0]
   for num in list:
      if first!= list[0]:
         return False
      else:
         return True


print("all the same demo")
print("2,2,2",all_the_same([2,2,2]))
print("1,2,3",all_the_same([1,2,3]))
print("######################################")
print("")

def increasing(list):
    first= list[0]
    previos = list[0]-1
    for num in list:
      if num <= previos and num < first:
         return False
      else:
         return True

print("increasing demo")
print("2,2,2",increasing([2,2,2]))
print("1,2,3",increasing([1,2,3]))
print("######################################")
print("")

def incrimating(list):
   for num in list:
      if list[1]== (list[0]-1) or list[1]==(list[0]+1):
         return True
      else:
         return False

print("incimating demo")     
print("2,2",incrimating([2,2]))
print("1,2,",incrimating([1,2]))
print("######################################")
print("")

      
