import random
import math
from decimal import *


def get_mod_1(x):
	y=math.floor(x)
	return Decimal(x-y)

def get_x(x):
	val=Decimal(x).ln()
	return Decimal(get_mod_1(val))

#random num in range for a to b
def get_random(a,b):
	return random.randint(a,b)

#get value in Dn 
#here Dn ={10**n,10**n+1,........,10**(n+1)-1}
def get_Dn(n,i):
	return (10**n)+i

# def make_val(val):
# 	getcontext().prec=30
# 	curr=1/(10**30)
# 	x=0
# 	while(val!=0):
# 		x+=curr*(val%10)
# 		curr*=10
# 		val//=10
# 	return Decimal(x)

#encryption of text
# s :string , k =common secret key 
def xor(s,k):
	length=len(s)
	for i in range(length):
		# making each character as a number
		s=(s[:i]+chr(48+(ord(s[i])^ord(k[i%len(k)]))%10 ) +s[i+1:] )
	return s

def get_secret_key():
	#initial precision set to upto 60 digits 
	getcontext().prec=60
	#random seed 
	s=get_random(1,1000)
	
	#get x in range(0,1)
	x=get_x(s) 	
	print("x = ",x)
	# for current world computation n>=50 we can use get_random()
	n=10		
	#p1,p2 random position selection from Dn
	p1=get_random(1,10**(n+1)-(10**n)-2)
	p2=get_random(1,10**(n+1)-(10**n)-2)
	#alice
	a=get_Dn(n,p1)
	#bob
	b=get_Dn(n,p2)

	a_dash=get_mod_1(a*x)
	b_dash=get_mod_1(b*x)
	
	print("a_dash = ",a_dash)
	print("b_dash = ",b_dash)
	
	initial_k1=get_mod_1(a_dash*b)

	print("Initial_k1 = ",initial_k1)
	k1=initial_k1*(10**30)
	k1=math.floor(k1)
	initial_k2=get_mod_1(b_dash*a)
	print("Initial_k2 = ",initial_k2)	
	k2=initial_k2*(10**30)
	k2=math.floor(k2)
	#for better precision take only first 30 digits
	if(k1==k2):
		return initial_k1
	else:
		return 0

val=get_secret_key()
if(val==0):
	val=get_secret_key()

k="{0:.30f}".format(val)
print(k)
#message   in binary form  i.e we can convert message into fix bit  like 8 
#so that we can turn binary into msg
m="11100001110"
#encrypt
x=xor(m,k)
print("Encryption:",x)
#decrypt
y=xor(x,k)

print("Decrytion",y)


