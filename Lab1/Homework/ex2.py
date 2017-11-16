n = int ( input ("Enter a number: ") )
a = 1

if n < 2:
    a = 0
else:
    for i in range(2, n):
        if n % i == 0:
            a = 0
if a != 0:
    print (n, "is a prime number")
else:

    print (n, "is not a prime number")
