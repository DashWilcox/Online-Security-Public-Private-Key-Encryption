# These two functions will help determine if two numbers are coprimes #
# Returns the greatest common denominator for two numbers
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
# Determines if two numbers are coprime. Returns True or False
def is_coprime(x, y):
    return gcd(x, y) == 1

# Returns a list of all the prime numbers from 2 to n
def primes_less_than(n):
	all_primes=[]
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p ** 2, n + 1, p):
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers
	for p in range(n + 1):
		if prime[p]:
			all_primes.append(p)
	return all_primes

print("All primes less than 1,000:\n"+str(primes_less_than(1000)))


def calculate_N(p,q):
	return(p*q)

def calculate_T(p,q):
	T= (p-1)*(q-1)
	return T

def pick_e_d(p,q):
	T = calculate_T(p,q)
	N = calculate_N(p,q)
	e = 0
	d = 0
	
	for value in range(T,1,-1):
		if is_coprime(value, T) and is_coprime(value, N):
				e = value
				switch = True
				break
			
	for value in range((T**3),1,-1):
		if ((e*value)%T)==1:
				d= value
				switch2=True
				break
			
	print(e,d)
	return (e,d)
				




p = int(input("Give a prime number"))
q = int(input("Give another prime number"))

pick_e_d(p,q)

