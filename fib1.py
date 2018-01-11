def fib (n):
	if n < 2:
		return n
	return fib(n-2)+fib(n-1)


n = input("Enter the number of times you want to input n :")
n = int(n)
for i in range (0,n):
	a = input ("Enter number :")
	a = int(a)
	print (fib(a))
