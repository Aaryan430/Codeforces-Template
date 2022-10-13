import random # Importing the random library so as to use the randint fucntion to chose any random integer in between a given range.

# Below exp is the fast exponentiation function to calculate x^y % p
def power(x, y, p):
	
	# initialising ans variable to store the answer.
	ans = 1
	
    # taking mod of x with p as x can be greater than p.
	x = x % p

    # While y is greater then 0 check if y is odd then multiply x with the ans , else make x = x^2%p and making y=y/2 for each iteration.
	while (y > 0):
		
		# If y is odd, multiply x with ans
		if (y & 1):
			ans = (ans * x) % p
		# y must be even after above operation since x is multiplied once so y can be taken now as y=y-1.
        # and y/2 == y-1/2 in integer division
		y = y>>1; # y = y/2
		x = (x * x) % p # now multiplying x with x and making x = x^2 % p
	
	return ans # returning the answer.


# miller_rabin algorithm is used below to check for primality of number n it returns false if number n is composite and returns false
# is n is probably prime and return true only if it is prime.Here d is an odd number such that n-1 = 2^r*d,for somr r>=1. 
def miller_rabin(d, n):
	
	# picking and random number from 1-n-1.
	a = random.randint(2, n - 1)

	# Compute a^d % n
	x = power(a, d, n)

	if (x == 1 or x == n - 1):
		return True

	# checking until d!=n-1 if x^2%n==1 then return false and else if x^2%n==n-1 returning true.
	while (d != n - 1):
		x = (x * x) % n
		d *= 2

		if (x == 1):
			return False
		if (x == n - 1):
			return True

	# If result not found until this point then number may be prime but we will not return true as we are considering the numbers which
	# are for sure prime.
	return False

#Function is prime is used to check whether a number(i.e n) is prime or not here k is the accuracy factor,
#More large the value of k is higher is the accuracy of the algorithm.
def isPrime( n, k):
	# checking if n<=1 since negative numbers are not considered here and for n=4 we know it is composite. 
	if (n <= 1 or n == 4):
		return False

    # for n==2 or n==3 returning true.
	if (n <= 3):
		return True

    # find r such that n-1 = 2^r*d,r>=1
	d = n - 1
	while (d % 2 == 0):
		d //= 2

	# Iterate given number for 'k' Iterations
	for it in range(k):
		if (miller_rabin(d, n) == False):
			return False

	return True


# Driver Code Starts from here.

# Taking input of the accuracy factor.
k = int(input("Enter the accuracy factor : "))

# Taking the input of the number upto which the primes are required.
num = int(input("Enter the number upto which Primes are Required : "))

#printing all the primes upto num
print("All primes smaller than "+str(num)+" : ")

for i in range(1,num):
	if (isPrime(i, k)):
		print(i , end=" ")



#ANS of part Two

# As comparison to other algorithms Miller Rabin algorithm is better then other as we can see the time complexity for miller rabin is
# O(K∗(log(N))^3) .It is better then the basic algo in time and when it comes to the comparison with the fermat algo the fermat algo gives 
# wrong results with the carcmicheal numbers but with miller rabin algorithm it is not there.
# Fermat algo Time Complexity :  O(k (logn)3) 
# Basic algo Time complexity : O(2^n/2)

