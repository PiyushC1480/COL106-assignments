import random
import math
#To generate random prime less than N
def randPrime(N):
	print(N)
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

# return appropriate N that satisfies the error bounds
def findN(eps,m):# calculatib=ng the least upper bound for n
	"""calculation logic:
	let a and b are two strings of equal length . in out case one denote the pattern and other denote the part of text which we are comparing with pattern.
	let H(a) be hash value for a and H(b) is hash value of b.( i.e. H(a) 26^m-1 * a[0]+ and so on...)
	let Hp(a) denote the value of hash value for a and  Hp(b) denote the value of hash value for b which are evaluated for prime p.

	we say Hp(a)  = Hp(b) if H(a) mod p  = H(b) mod p.
	this means  (H(a) - H(b)) mod p =  0 or H(a)-H(b) is a multiple of prime p.
	let D = |H(a) - H(b)|. 
	from claim 1 of assignmant we have D has at most log(D) prime divisors 
	let prime factorization of D contains k prime with repetition.
	we have k<=log(D)
	Probability that random prime p from {1,.....,N} is a divisor is  =  k/(pi(N)) <= log(D)/ (pi(N)) <= log(D)/(N/2log(N))  = log(D) * log(N) / (2N) <= eps
	since log(D) <= m (length of difference is less than or equal to the original length of the number( length == no of bits used))
	we have 
	N/(2log(N)) >= m/eps ---(2)
	for N = 2* (m/eps) log(m/eps) 
	we find that the equality (2) holds
	"""
	return math.ceil((2 * m * (math.log(m/eps,2)))/eps)

# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
	txt_len = len(x)# stores the length of list taking O(log(n)) space
	pat_len = len(p)#stores the length of list taking O(log(m)) space
	f_p = 0# stores the hash value calculated for pattern : takes O(loq (q)) space
	f_x = 0 # stores the hash value calculated for pattern : takes O(loq (q)) space
	final_list = []# stores the final_list . taking O(k) space 
	for i in range(0,pat_len):#iterating pver patttern to calculate the fist hash value 
		f_p = (26*f_p + (ord(p[i])-65))% q # takes O(logq) space theta(log(q)) time for logq to be the length of bit string correxponding to f_x
		f_x = (26*f_x + (ord(x[i])-65))% q # takes O(logq) space and theta(log(q)) time for logq to be the length of bit string correxponding to f_x
	"""time complexity taken by above algorithm is O(m)"""
	for i in range(txt_len-pat_len+1):#iteratig over the text length -pat_len taking O(n-m)
		if f_p == f_x :# if the hash value calculated are equal then we append it in the final_list 
			final_list.append(i) # O(1*) * means amortized 
		 # if index is less then the pattern length and the text length
		if i<txt_len-pat_len: 
			f_x = (26*((f_x-((pow(26,pat_len-1)*(ord(x[i])-65))%q)) )+ (ord(x[i+pat_len])-65)) % q # calculating the new hash value for x[i+1 to i+m]
		"""this takes O(logq) time and O(logq space because length of f_x is O(logq) and all computation takes O(1) time (amortized)"""
		if f_x < 0:# if negative value is obtained then add the q to get the positive answer 
			f_x = f_x+q#O(logq) time
	return final_list
"""time complexity analysis : the above algorith takes O(m(logq+logq) + (n-m)logq)==> O((n+m)logq)  """
"""space complexity analysis: the above algorith takes O(k+ logn+ logm+ 2logq) . since logq< logn  giving the splace coplexity as O(k+logn+logm)"""
	

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):

	txt_len = len(x)# stores the length of list taking O(log(n)) space
	pat_len = len(p)#stores the length of list taking O(log(m)) space
	f_p_temp=0# stores the hash value calculated for pattern : takes O(loq (q)) space
	f_x = 0 # stores the hash value calculated for pattern : takes O(loq (q)) space
	final_list = []# # stores the final_list . taking O(k) space 

	"""here for evaluation of hash value, we are not considering the position of ? and cooresponding position in text. for example hash value of "AB?C" is (26^3*0+ 26^2*1+ 26^0*2)(see i have not included the ? term) """
	for i in range(0,pat_len):#(O(m))
		if p[i] =='?':
			q_pos = i # mark where the question mark is occuring 
			f_p_temp = (26*f_p_temp)% q#O(logq)
			f_x = (26*f_x)% q#O(logq)
		else:# if not '?' then evaluate as usual
			f_p_temp = (26*f_p_temp + (ord(p[i])-65))% q#O(logq)
			f_x = (26*f_x + (ord(x[i])-65))% q

	for i2 in range(txt_len-pat_len+1):##iteratig over the text length taking O(n-m ) time 
		if f_p_temp == f_x:# if hash value mathces then append in the final list
			final_list.append(i2)
		# methadology :  remove the first aplphabet from substring of txt considered,add the next alphabet in that substring from text, remove  the alplabet next to '?' , and add the alphabet which was at position of '?' in the text
		if pat_len == 1:
				f_x = 0
		else:
			if i2<txt_len-pat_len:  # otherwise if pat_len is one then pow(26,pat_len-q_pos-2) is less than 1 
				"""below if-else is mutually disjoint because for a given pattern either the ? appears in front or in last or at any position except these two"""
				if q_pos == pat_len-1:
					f_x = math.ceil(((26*(f_x-(pow(26,pat_len-1)*(ord(x[i2])-65)%q) + (pow(26,pat_len-q_pos-1)*(ord(x[i2+q_pos])-65)%q)))%q) % q)
				elif q_pos == 0:# wildcard appears in the start of term
					f_x = math.ceil(((26*(f_x - (pow(26,pat_len-q_pos-2)*(ord(x[i2+q_pos+1])-65)%q)))%q + (ord(x[i2+pat_len])-65)%q) % q)
				else:
					f_x = math.ceil(((26*(f_x-(pow(26,pat_len-1)*(ord(x[i2])-65)%q) + (pow(26,pat_len-q_pos-1)*(ord(x[i2+q_pos])-65)%q) - (pow(26,pat_len-q_pos-2)*(ord(x[i2+q_pos+1])-65))%q))%q + (ord(x[i2+pat_len])-65)%q) % q) # O(logq)

		if f_x < 0: # if negative value is obtained then add the q to get the positive answer
				f_x = f_x+q
	return final_list
"""time complexity analysis : the above algorith takes O(m(logq+logq) + (n-m)logq)==> O((n+m)logq)  """
"""space complexity analysis: the above algorith takes O(k+ logn+ logm+ 2logq) . since logq< logn  giving the splace coplexity as O(k+logn+logm)"""
"""which are same as that of modPatternMatch()"""