# Those are short Python scripts.

'''
# Combines a range till 5 (or string ) with a coin mark.

def combine_coins(coin, lista):
    return  ', '.join(          map( lambda y, x: y + str(x)  , [ coin for i in lista]   , lista )                )

if __name__ == '__main__':
    x = combine_coins('$', range(5))
    print( x)



# Print nubers in date format.
if __name__ == '__main__':
    details = []
    user_details = input("Please enter your phone number: \n")
    details.append(user_details)
    user_details = input("Please enter your first name: \n")
    details.append(user_details)
    user_details = input("Please enter your last name: \n")
    details.append(user_details)

    details.reverse()
    print(' '.join(details))


import datetime
if __name__ == '__main__':
    day = input("Please enter day number: \n")
    month = input("Please enter month number: \n")
    year = input("Please enter year number: \n")
    f"{datetime.datetime.now():%day/%month/%year}"
    print("{}/{}/{}".format(day,month,year))

# made average with input numbers who separated by commas.
import functools
if __name__ == '__main__':
    number = input("Please enter numbers and separate them by commas : \n")
    numbers = number.split(',')
    len = len(numbers)
    result = map(lambda x: int(x), numbers)
    Sum = functools.reduce(lambda x,y: x+y ,result)
    print("The average is : ",(Sum/len))
'''
# Filter the negative numbers and print them as positive.
def filters(x):
    if (x < 0):
        print(abs(x))
    else:
        pass

if __name__ == '__main__':
    number = input("Please enter numbers and separate them by commas (don't finishing with comma): \n")
    numbers = number.split(',')
    results = map(lambda x: int(x), numbers)
    print("The result is: ")
    result = list(filter(filters, results))