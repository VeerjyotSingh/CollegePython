import time
def isPrime(n,primeList = []):
	if n <= 1:
		return False
	elif n == 2:
		return True
	elif n%2 == 0:
		return False
	else:
		if primeList:
			for p in primeList:
				if p * p > n:
					break
				if n % p == 0:
					return False
			return True
		else:
			for i in range(3,((int(n**0.5))+1),2):
				if n%i == 0:
					return False

		return True

def allPrimeTill(n):
	primeList = []
	for i in range(2,n+1):
		if isPrime(i,primeList):
			primeList.append(i)
	return primeList
start = time.time()
allPrimeTill(10000)
end = time.time()
print(end - start)

""""""