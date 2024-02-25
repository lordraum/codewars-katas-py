my_string = "Este es el código de prueba"

def spin_words(sentence):
    acc = []
    for x in sentence.split():
        if len(x) >= 5:            
            acc.append(x[::-1])
        else:
            acc.append(x)
    return ' '.join(acc)

result = spin_words(my_string)

print(result)

# Solución con comprehension lists
""" 
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
"""