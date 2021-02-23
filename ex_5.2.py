largest = 0
smallest = 99999999
num = 0
while True:
        num = input('Enter a number:')
        if num == 'done' :
            break
        try:
                i_num = int(num)
        except:
            print('Invalid input')

        if i_num > largest :
            largest = i_num
        elif  i_num < smallest :
            smallest = i_num

print('Maximum is',largest)
print('Minimum is',smallest)
