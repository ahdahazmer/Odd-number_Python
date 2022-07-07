num = int(input("Enter a number: "))

if num <= 5:
    print('Please insert number that more than 5. You enter', num)
else:
    print('Odd number that more than 5 are: ')
    for i in range(7, num, 2):
        print(i)