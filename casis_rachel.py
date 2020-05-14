#create a function
#replace('The quick brown fox jumps over the lazy dog', 'quick', 'slow')
#The slow brown fox jumps over the lazy dog
print()
print()

ogSent = "The quick brown fox jumps over the lazy dog" 
def change_it (ogSent,changeWord,toReplace):
    print(ogSent.replace(cWord, cReplace)) #if may number un ung max times na magpapalit  

cWord= "quick"
cReplace = "slow"
change_it(ogSent, cWord, cReplace )