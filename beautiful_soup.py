
import sys
def findMinInsertions(str,l,h):
    if (l>h):
        return sys.maxsize
    if (l == h):
        return 0
    if (l == h-1):
        return 0 if(str[l]==str[h]) else 1
    if (str[l] == str[h]):

        return findMinInsertions(str,l+1,h-1)
    else:
        return (min(findMinInsertions(str,l,h-1),findMinInsertions(str,l+1,h))+1)
if __name__ =="__main__":
    str = "noor"
    print("len of str",len(str))
    print(findMinInsertions(str,0,len(str)-1))

def longestPalSubstr(string): 
	maxLength = 1
	start = 0
	length = len(string) 
	low, high = 0, 0
	for i in xrange(1, length): 
		low = i - 1
		high = i 
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1 
		low = i - 1
		high = i + 1
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1

	print("Longest palindrome substring is:", string[start:start + maxLength] )
	return maxLength


def palindromeSubStrs(s): 
	m = dict() 
	n = len(s) 
	R = [[0 for x in xrange(n+1)] for x in xrange(2)] 
	s = "@" + s + "#"
	for j in xrange(2): 
		rp = 0 # length of 'palindrome radius' 
		R[j][0] = 0
		i = 1
		while i <= n: 
			while s[i - rp - 1] == s[i + j + rp]: 
				rp += 1
			R[j][i] = rp 
			k = 1
			while (R[j][i - k] != rp - k) and (k < rp): 
				R[j][i+k] = min(R[j][i-k], rp - k) 
				k += 1
			rp = max(rp - k, 0) 
			i += k 
	s = s[1:len(s)-1] 
	m[s[0]] = 1
	for i in xrange(1,n): 
		for j in xrange(2): 
			for rp in xrange(R[j][i],0,-1): 
				m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
		m[s[i]] = 1

	# printing all distinct palindromes from hash map 
	print ("Below are " + str(len(m)) + " pali sub-strings")
	for i in m: 
		print i 

def countps(str):
    length = len(str)
    start = 0
    count = 0
    cps = [[0 for i in range(length)]for j in range(length)]
    for i in range(length):
        cps[i][i] = 1
    for L in range (1, length+1):
        for i in range(length):
            k = L + i -1
            if k <length:
                if str[i] == str[k]:
                    count+=1
                    cps[i][k] = cps[i][k-1]+cps[i+1][k]+1
                else:
                    cps[i][k] = cps[i][k-1]+cps[i+1][k] - cps[i+1][k-1]
    
    return cps[0][length-1]

def longest_common_subse(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + longest_common_subse(X,Y,m-1,n-1)
    else:
        return max(longest_common_subse(X,Y,m,n-1),longest_common_subse(X,Y,n-1,m))

X = "AGGTAB"
Y = "GXTXAYB"

# Dynamic Programming implementation of LCS problem 

def lcs(X , Y):
    # find the length of the strings 
    m = len(X)
    n = len(Y) 
    L = [[None]*(n+1) for i in range(m+1)]
    print("L",L)
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
##############      Subset Sum Problem

def subset(set,n,sum):
    if n == 0:
        return False
    if sum == 0:
        return True
    if set[n-1] > sum:
        return subset(set,n-1,sum)
    return (subset(set,n-1,sum) or subset(set,n,sum-set[n-1]))
set = [3, 34, 4, 12, 5, 2] 
sum = 9
n = len(set) 


####### shortest subsequence of string

def shortestSuperSequence(X, Y): 
	m = len(X) 
	n = len(Y) 
	l = lcs(X, Y, m, n) 
	
	# Result is sum of input string 
	# lengths - length of lcs 
	return (m + n - l) 

# Returns length of LCS for 
# X[0..m - 1], Y[0..n - 1]

def lcsd(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 2) for i in range(m + 2)]

	for i in range(m + 1): 
		
		for j in range(n + 1): 
			
			if (i == 0 or j == 0) : L[i][j] = 0
			
			elif (X[i - 1] == Y[j - 1]) : 
				L[i][j] = L[i - 1][j - 1] + 1
				
			else : L[i][j] = max(L[i - 1][j], 
								L[i][j - 1]) 
			
	# L[m][n] contains length of 
	# LCS for X[0..n - 1] and Y[0..m - 1] 
	return L[m][n] 

# Driver code 
X = "AGGTAB"
Y = "GXTXAYB"

################   minimum insertion and deletion of strings #######
def lcsd(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 2) for i in range(m + 2)]  
    for i in range(m + 1): 
        for j in range(n + 1): 
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif (X[i - 1] == Y[j - 1]) : 
                L[i][j] = L[i - 1][j - 1] + 1
            else : 
                L[i][j] = max(L[i - 1][j],L[i][j - 1]) 
    return L[m][n] 

#########  longest common substring  
def LCSubStr(X, Y, m, n): 
 
	LCSuff = [[0 for k in range(n+1)] for l in range(m+1)] 
	result = 0
	for i in range(m + 1): 
		for j in range(n + 1): 
			if (i == 0 or j == 0): 
				LCSuff[i][j] = 0
			elif (X[i-1] == Y[j-1]): 
				LCSuff[i][j] = LCSuff[i-1][j-1] + 1
				result = max(result, LCSuff[i][j]) 
			else: 
				LCSuff[i][j] = 0
	return result 

X = "AGGTAB"
Y = "GXTXAYB"

############## longest polindrome in a string     #########

def longestPalSubstr(string): 
	maxLength = 1
	start = 0
	length = len(string) 
	low, high = 0, 0
	for i in range(1, length): 
		low = i - 1
		high = i 
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1 
		low = i - 1
		high = i + 1
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1

	print("Longest palindrome substring is:", string[start:start + maxLength] )
	return maxLength

# A Dynamic Programming solution for Rod cutting problem 
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + val[i-j-1])
            print("max_val",max_val)
        val[i] = max_val
    return val[n] 
 
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 


#########   eggs 

import sys 

# Function to get minimum number of trials 
# needed in worst case with n eggs and k floors 
def eggDrop(n, k): 

	# If there are no floors, then no trials 
	# needed. OR if there is one floor, one 
	# trial needed. 
	if (k == 1 or k == 0): 
		return k 

	# We need k trials for one egg 
	# and k floors 
	if (n == 1): 
		return k 

	min = sys.maxsize 
 
	for x in range(1, k + 1): 

		res = max(eggDrop(n - 1, x - 1), 
				eggDrop(n, k - x)) 
		if (res < min): 
			min = res 

	return min + 1

# Driver Code 
if __name__ == "__main__": 

	n = 4
	k = 20
	 
# A Dynamic Programming based Python Program for the Egg Dropping Puzzle 
INT_MAX = 32767

# Function to get minimum number of trials needed in worst 
# case with n eggs and k floors 
def eggDrop(n, k): 
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)] 
    for i in range(1, n + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
    print('eggFloor',eggFloor)
    for j in range(1, k + 1):
        eggFloor[1][j] = j 
    for i in range(2, n + 1): 
        for j in range(2, k + 1): 
            eggFloor[i][j] = INT_MAX 
            for x in range(1, j + 1): 
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res  
    return eggFloor[n][k] 
n = 4
k = 20

l = [5, 4, 4, 2, 2, 8]
l.sort()
for i in range(len(l)):
    if l[i] != l[i-1]:
        print(len(l)-i)
arr = [5, 4, 4, 2, 2, 8]
arr = [1, 2, 3, 4, 3, 3, 2, 1]
while len(arr)!=0:
    n = (len(arr))
    arr = [x for x in arr if x != min(arr)]
    print(n,len(arr))
    
print("*"*12)

import sys   
def cutRod(price, n): 
    if(n <= 0):
        return 0
    max_val = -sys.maxsize-1
    for i in range(0, n): 
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
        print("max_val",max_val)
    return max_val

# Driver code 
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 


# A Dynamic Programming solution for Rod cutting problem 
INT_MIN = -32767
def cutRod(price, n): 
    val = [0 for x in range(n+1)] 
    print("val1",val)
    val[0] = 0
    print("val",val)
    for i in range(1, n+1): 
        max_val = INT_MIN
        print("i",i)
        for j in range(i): 
            max_val = max(max_val, price[j] + val[i-j-1])
            print("price[j]",price[j],"val[i-j-1]",val[i-j-1])
        val[i] = max_val
    return val[n] 
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 

def powe(n):
    if n ==0:
        return False
    while n!=1:
        if n%2 !=0:
            return False
        n = n//2
    return True
    

def coins(arr,m,sums):
    if sums==0:
        return 1
    if sums < 0:
        return 0
    if m<=0 and sums>=1:
        return 0
    return (coins(arr,m-1,sums))+ coins(arr,m,sums-(arr[m-1]))
#print(coins([1,2,3],3,4)) 8310913031 rojesh

import sys
print("&"*12)
def mincoins(arr,n,sums):
    if sums==0:
        return 0
    res = sys.maxsize
    for i in range(0,n):
        if arr[i] <= sums:
            print("i",i)
            sub_coins = mincoins(arr,n,sums-arr[i])
            print("sub_coins",sub_coins)
            if sub_coins!= sys.maxsize and sub_coins+1<res:
                res = sub_coins+1
                print("res",res)
    return res
coins = [1,2,3]
m = len(coins)
V = 4
print("minimum number of coins required is: ",mincoins(coins,m,V))

def minCoins(coins, m, V): 
	if (V == 0): 
		return 0 
	res = sys.maxsize  
	for i in range(0, m): 
		if (coins[i] <= V): 
			sub_res = minCoins(coins, m, V-coins[i]) 
			if (sub_res != sys.maxsize and sub_res + 1 < res): 
				res = sub_res + 1
	return res 
coins = [9, 6, 5, 1] 
m = len(coins) 
V = 11
print("Minimum coins required is",minCoins(coins, m, V)) 



                





