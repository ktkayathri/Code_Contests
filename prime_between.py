# Find the prime numbers in the range of numbers given as input
# Input line 1 - Number of test cases (n)
# Input Line 2 to n - numbers separated by a space (range)
# Output - for each range, print the difference between the smallest and largest prime numbers in the range (numbers inclusive)

import sys
import math

def main():
    inp = sys.stdin.readlines()

    test_cases = int(inp[0])
 
    for i in range(test_cases):
        num1, num2 = inp[i+1].split(' ')
        
        num1 = int(num1)    
        num2 = int(num2)
        prime1 = -1
        for j in range(num1, num2+1):
            if is_prime(j):
                prime1 = j
                break
       
        prime2 = -1
        for j in range(num2,num1-1,-1):
            if is_prime(j):
                prime2 = j
                break

        if (prime1 == -1 and prime2 == -1):
            print(prime1)  
        elif (prime2 > prime1) or (prime1 == prime2):
            print("%d" % (prime2-prime1))
         

# Function to check if a given number is Prime or not
def is_prime(num: int) -> bool:

    sqrt = math.ceil(math.sqrt(num))
    if (num==2):
        return True
    if (num % 2 ==0 or num < 2):
        return False
    for i in range(3,sqrt+1):
        if (num % i == 0):
            return False
    return True

if __name__ == "__main__":
    main()