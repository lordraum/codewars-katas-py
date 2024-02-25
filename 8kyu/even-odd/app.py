def evenOrOddOld(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


# Operador ternario opcion_1 if condición else opcion_2

evenOrOdd = lambda x: 'Even' if x % 2 == 0 else 'Odd'

print(evenOrOdd(6))