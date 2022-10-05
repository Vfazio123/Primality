'''
Vincent Fazio
CSC 2343-01
Lab 5 Showing Primality 

This program takes a positve number as input and figures whether it is prime or composite.
It also takes inputted number, and finds all prime numbers between the first prime and last prime of the square rooted number.
'''
from math import sqrt

print("Example Input: 101")
num = int(input("Enter a positive number: "))

# Function FindPrime
# returns false or true depending upon whether it is prime or not
def FindPrime(seq):
   if seq > 1:   
      for i in range(2,seq):
         if seq % i == 0:
            return False
      return True   

#arr to store primes found inbetween first and last prime numbers of square rooted number
arr = []
for i in range(2, int(sqrt(num))+1):
   if FindPrime(i):
      arr.append(i)

#print out, if number is prime and the array that goes with that number
if FindPrime(num):
   print(arr,"shows that",num, "is prime.")
else:
   print(arr,"shows that",num, "is composite.")
