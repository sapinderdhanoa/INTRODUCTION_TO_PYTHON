

def below_100_and_even(number):
 if number < 100 :
    if (number%2) == 0 :
       return True
    else:
        return False    
 else:
    print("number is greater than 100," + str(number))

print(below_100_and_even(50))
print(below_100_and_even(102))
