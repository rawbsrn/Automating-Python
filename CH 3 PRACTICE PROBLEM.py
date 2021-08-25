def collatz(number):
        if number % 2 == 0:
           return number // 2
        return 3 * number + 1

while True:
    try:
        print('what numba')
        num = int(input())
        break
    except ValueError:
        print('oopsie poopsie')
    
while num != 1:
    num = collatz(num)
    print(num)
    
print('yay')

