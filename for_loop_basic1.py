#Count from 0 to 150
for x in range(151):
    print(x)
#Print all multiples of 5 from 5 to 1000
for x in range(5, 1001, 5):
    print(x)
# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo
for x in range(1, 101, 1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# Add odd integers from 0 to 500,000, and print the final sum
sum = 0
for x in range(1, 500000, 2):
    sum = sum + x

print"This is the sum", sum

#Print positive numbers starting at 2018, counting down by fours.
for x in range(2018, 0, -4):
    print(x)

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexible_counter(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)

flexible_counter(3, 64, 4)
def add(a,b):
    x = a + b
    return x
new_value = add(3,5)
print(new_value)
def a():
    return 5
print(a())
#2
def a():
    return 5
print(a()+a())

#Find if a # is even or odd
num = 11
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

def years_to_days(age):
    year = 365
    days = 0 
    days = age * year
    return days
print(years_to_days(23))