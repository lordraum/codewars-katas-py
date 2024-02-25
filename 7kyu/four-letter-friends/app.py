names = ["Ryan", "Kieran", "Mark"]

""" def getFourLetterNames(str):
    return len(str) == 4 """

def getFourLetterNames(arr):
    return list(filter(lambda x: len(x) == 4, arr))

# Otra solución con comprehension list
""" 
def friend(x):
    return [f for f in x if len(f) == 4]
 """

# fourLetterNames = list(filter(getFourLetterNames, names))

fourLetterNames = getFourLetterNames(names)

print(fourLetterNames)
