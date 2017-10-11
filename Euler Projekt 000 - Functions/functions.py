###############################################################################

from os import path

#Is a number prime
def isNewPrime(number,primes):
	for prime in primes:
		if number%prime == 0:
			return False
	return True

#Generate primes up to a limit
def genPrimes(upper):
	filepath = path.join(path.dirname(__file__),"primes.txt")
	primes=set()
	
	print("Checking existance of generated prime file")
	if not path.exists(filepath):
		print("File does not exist, generating...")

		primes.add(2)
		for natnum in range(2,upper):
			if isNewPrime(natnum,primes):
				primes.add(natnum)
		
		f = open(filepath,"w")
		f.write(str(primes)[1:-1])
		print("File generated. Next run of this program should skip this step!")
	else:
		print("File exists, parsing...")
		f=open(filepath, 'r')
		for num in f.read().split(','):
			primes.add(int(num))
		print("Parsing complete!")
	
	f.close()
	return primes

###############################################################################

def textrotate(l, n):
	l=str(l)
	return l[-n:] + l[:-n]

###############################################################################