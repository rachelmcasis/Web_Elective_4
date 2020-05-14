NumList = [ 1, 4, 5, 8, 10] 
NewList = ['d', 'b', 'c', 'z', 'a']

def is_sorted(List):
    
    if (List == sorted(List)): 
        print ("Yes, List is sorted.") 
    else: 
        print ("No, List is not sorted.") 
    

print (is_sorted(NumList))
print (is_sorted(NewList))
      