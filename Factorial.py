def factorial(sum,num):
    for i in range(1, num + 1):
        sum = i * sum
    return sum
if __name__ == '__main__':
    print(factorial(1,int(input('Enter a integer number please: '))))
