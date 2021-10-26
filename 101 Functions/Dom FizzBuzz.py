count = int(input("Welcome to Fizz Buzz! How high would you like to count?: "))
def func(count):
  for i in range(count + 1):
    if i % 3 == 0 and i % 5 == 0 : print('FizzBuzz')
    elif i % 5 == 0 : print('Buzz')
    elif i % 3 == 0 : print('Fizz')
    else : print(f"{i}")
func(count)


