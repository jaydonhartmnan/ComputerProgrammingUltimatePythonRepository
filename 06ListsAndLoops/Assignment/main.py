def count_failing_grades(grades):
    count=0 
    for grade in grades:
        if grade < 60:
          count= count + 1
    return count
    
inputlist = [40, 80, 71, 26, 93]
returnValue = count_failing_grades(inputlist)
print("There are this many failing grades",(returnValue))
print("######################################")
print("")


def count_act_score(list):
   validact=  0
   for act in list:
        if act >= 1 and act<= 36:
          validact= validact + 1
   return validact 

inputlist = [-5, 24, 31, 56, 25]
returnValue = count_act_score(inputlist)
print("This many valid act scores=",(returnValue))
print("######################################")
print("")

def num_sum(list):
   total= 0
   for number in list:
    total = total + number 
   return total

inputlist = [-5, 24, 31, 56, 25]
returnValue = num_sum(inputlist)
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
   
inputlist = [-5, 24, 31, 56, 25]
returnValue = avergage_act_score(inputlist)
print("Avergage act score=",(returnValue))
print("######################################")
print("")

def all_true(list):
   for item in list:
       if item not in["True"]:
        return False
   return True 
   
inputlist = ["True","False","True","True"]
returnValue = all_true(inputlist)
print("True,False,True,True-All true=",(returnValue))
print("######################################")
print("")

def any_true(list):
   for item in list:
      if item in ["True"]:
         return True
      
inputlist = ["True","False","True","True"]
returnValue = any_true(inputlist)
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

inputlist = ["Falsee","False","False","True"]
returnValue = mostly_true(inputlist)
print("False,False,False,True-mostly true=",(returnValue))
print("######################################")
print("")

def has_vowel(input):
   for item in input:
      if item in(["a", "e", "a", "i", "u", "o"]):
         return True
      else:
         return False
inputlist = ["e"]
inputlist1 = ["t"]

returnValue = has_vowel(inputlist)
print("e=",(returnValue))
returnValue1 = has_vowel(inputlist)
print("a=",(returnValue1))

print("######################################")
print("")