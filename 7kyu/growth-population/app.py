# PARAM => p0 => INIT POPULATION
# PARAM percent => population increase percentage (%)
# PARAM aug => New Inhabitants Per Year
# PARAM p => Population Limit --> STOP NUMBER
# RETURN => years => Years To Reach Population Limit

""" def nb_year(p0, percentage, aug, p):
    years = 0
    while p0 < p:
        p0 += int((p0 * (percentage/100)) + aug)
        years += 1
    return years """

def nb_year(p0, percent, aug, p, years= 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years

test1 = nb_year(1500, 5, 100, 5000) #15
test2 = nb_year(1500000, 2.5, 10000, 2000000) #10

print(test1, test2)



