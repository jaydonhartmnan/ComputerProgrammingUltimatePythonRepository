def make_abc():
    result= ["a","b", "c"]
    return result 

print("demonstrate make_abc")
print(make_abc())
print("#####################")
print("")


def equal_edges( list ):
    if list[0] == list[3]:
     return True
    else:
     return False

print("is it a equal edge:")   
print("[1, 2, 3, 11] -> ", equal_edges([1, 2, 3, 11]))
print("[3, 4, 4, 3] -> ", equal_edges([3, 4, 4, 3]))
print("[2, 3, 1, 2] -> ", equal_edges([2, 3, 1, 2]))
print("#####################")
print("")


def common_edges( list1, list2 ):
   if list1[0] == list2[0] or list1[0] == list2[1] or list1[-1] == list2[-1] or list1[0]==list2[-1] or list1[-1]==list2[0]:
    return True
   else:
     return False

print("is it a common edge:")   
print("1,2,3/2,5,7->",common_edges([1, 2, 3],[2,5,7]))
print("5,9,1/8,5,7_>",common_edges([5,9,1],[8,5,7]))
print("9,2,7/8,7,0->",common_edges([9,2,7],[8,7,0]))
print("#####################")
print("")

def all_the_same(list):
  if list[0]==list[1] and list[0]==list[2]:
   return True
  else:
    return False

print("is it all the same:")  
print("1,2,3->",all_the_same([1, 2, 3]))
print("5,9,1->",all_the_same([5,9,1]))
print("1,1,1->",all_the_same([1,1,1]))
print("#####################")
print("")

def all_unique(list):
  if list[0]!=list[1] and list[0]!=list[2]:
    return True
  else:
    return False

print("is it all unique:")  
print("1,2,3->",all_unique([1, 2, 3]))
print("1,1,1->",all_unique([1, 1, 1]))
print("4,5,9->",all_unique([4, 5, 9]))
print("#####################")
print("")

def increasing(list):
  if list[0]<list[1] and list[1]<list[2]:
    return True
  else:
    return False
  
print("is it increasing:") 
print("1,3,4->",increasing([1,3,5]))
print("11,10,9->",increasing([11,10,9]))
print("4,8,12->",increasing([4,8,12]))
print("#####################")
print("")

def all_True(list):
  if list[0]=="True"   and list[1]=="True" and list[2]=="True":
   return True
  else:
    return False
 
print("Is it all true")
print(" True, True, True->",all_True(["True","True", "True"]))
print("False, False,False->",all_True(["False","False","False"]))
print("False,True,False->",all_True(["False","True","False"]))
print("#####################")
print("")

true = 0
false = 0

def mostly_true(list):
  true = 0
  false = 0
  for item in list:
    if item == "True":
      true += 1
    else:
      false += 1

  if true > false:
    return True
  else: 
    return False
  
print("Is it mostly True")
print(" True, True, True->",mostly_true(["True","True", "True"]))
print("False, False,False->",mostly_true(["False","False","False"]))
print("False,True,False->",mostly_true(["False","True","False"]))
print("#####################")
print("")

def make_copy(list):
   return(list[0],list[1],list[2])

print("make a cop demo")
print("0,1,2=>",make_copy([0,1,2]))
print("#####################")
print("")


def repeat_thrice(item):
   return(item[0],item[0],item[0])

print("repeat thrice demo")
print("1=>",repeat_thrice([1]))
print("#####################")
print("")

def make_reversed_copy(list):
  return(list[2], list[1], list[0])

print("reversed demo")
print("1,7,9=>",make_reversed_copy([1,7,9]))
print("#####################")
print("")

def reverse_in_place(list):
    first =list[2]
    second=list[1]
    last=list[0]
    return(first,second,last)

print("reverse in place demo")
print("reversed= 3,2,1=>","inorder=>",reverse_in_place([3,2,1]))
print("#####################")
print("")

