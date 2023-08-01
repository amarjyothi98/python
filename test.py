# def square (x):
#     print(x*x) 

# print(square(4))

# def printMe(str):
#     print(str)
#     return; 

# print(printMe("this is something I have put into printMe(str)"))


# def fact(n):
#     if(n == 0): 
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(5))
# print(fact(0))


#sieve of Eratosthenes problem

# def prime_sieve (n): 
#     prime = [0 for i in range(101)]
#     for i in range (2, n+1):  #2 to 50
#         if prime[i] == 0:
#             for j in range (i*i, n+1, i): 
#                 prime[j] == 1




#fibonacci series problem

# def fib (n):
#     a = 0
#     b = 1

#     if(n == 1): 
#         print(a)

#     else:

#         print(a)
#         print(b)

#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)

# fib(5)


