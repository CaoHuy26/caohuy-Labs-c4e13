numbers = [1, 6, 8, 1, 2, 1, 5, 6]

n = int ( input ("Enter a number? ") )

count = 0

for i in numbers:
    if n == i:
        count += 1
print ("{0} appears {1} times in my list".format (n, count) )

#with count()
print ("{0} appears {1} times in my list".format (n, numbers.count(n) ) )
