def make_abc():
    result= ["a","b", "c"]
    return result 

print("demonstrate make_abc")
print(make_abc())


def equal_edges( num1, num2, num3, num4 ):
    numlist= [num1, num2, num3, num4]
    if num1 == num4:
     return True
    else:
     return False
    
print("[1, 2, 3, 11] -> ", equal_edges([1, 2, 3, 11]))
print("[3, 4, 4, 3] -> ", equal_edges([3, 4, 4, 3]))
print("[2, 3, 1, 2] -> ", equal_edges([2, 3, 1, 2]))


def common_edges( list1, list2 ):
   