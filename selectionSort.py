newval = []
costofprog=0
print("Size of array should be an int and the values in array should be float. If they are not ValueError will be printed. You will have to restart the program if that occurs.")

size = int(input('Enter size of array: '))
nsize = size
values = [float(input('Enter a value: ')) for _ in range(size)]

n = nsize
while n > 0:
    minval = min(values)
    newval.append(minval)
    values.remove(minval)
    n = n-1
    costofprog=costofprog+1

print(newval)

print("The cost of program is O(", costofprog,")")
