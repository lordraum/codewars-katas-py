# How good are you really?
#There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!
#Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array

# Mi primera solución
# def better_than_average(class_points, your_points):
#    count = 0
#    for x in class_points:
#        count += x
#    return your_points > count / len(class_points)

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

print(better_than_average([4, 3, 3], 3))

# A tener en cuenta
# Función sum()
    
                
