def function(value):

    if(value%15 == 0):
        return 'FizzBuzz'
    elif (value%3 == 0):
        return 'Fizz'
    elif (value%5 == 0):
        return 'Buzz'
    else:
        return value
    
for n in range(1,101):
    print(function(n))
    
        
