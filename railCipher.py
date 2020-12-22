def encryption(s,key):
	n=len(s)
	m=[]
	for i in range(key):
		a=[]
		for j in range(n):
			a.append(0)
		m.append(a)
	y=0
	z=0
	flag=1
	cip=""
	for i in s:
		if y>=0 and y<=key-1:
			if y==0 and flag==1:
				m[y][z] = i
				y=y+1
			elif y==key-1 and flag==-1:
				m[y][z] = i
				y=y-1
			elif y==key-1 and flag==1:
				m[y][z]=i
				flag=-1
				y=y-1
			elif y==0 and flag==-1:
				m[y][z]=i
				flag=1
				y=y+1
			else:
				m[y][z]=i
				y=y+flag
		z+=1
	print(m)
	for i in range(key):
		for j in range(n):
			if m[i][j]!=0:
				cip+=m[i][j]
	print(cip)
def decryption(s,key):
	n=len(s)
	m=[]
	for i in range(key):
		a=[]
		for j in range(n):
			a.append(0)
		m.append(a)
	y=0
	z=0
	flag=1
	ind=[]
	plain=""
	for i in s:
		if y>=0 and y<=key-1:
			if y==0 and flag==1:
				m[y][z] = '*'
				ind.append(y*n+z)
				y=y+1
			elif y==key-1 and flag==-1:
				m[y][z] = '*'
				ind.append(y*n+z)
				y=y-1
			elif y==key-1 and flag==1:
				m[y][z]='*'
				ind.append(y*n+z)
				flag=-1
				y=y-1
			elif y==0 and flag==-1:
				m[y][z]='*'
				ind.append(y*n+z)
				flag=1
				y=y+1
			else:
				m[y][z]='*'
				ind.append(y*n+z)
				y=y+flag
		z=z+1
	c=0
	for i in range(key):
		for j in range(n):
			if m[i][j]=='*':
				m[i][j]=s[c]
				c=c+1
	for i in ind:
		row=i//n
		col=i%n
		plain+=m[row][col]
	print(plain)
print("1.Encryption \n2.Decryption \nEnter your choice:")
t=int(input())
if t==1:
	print("Enter your message to be encrypted:")
	s=input()
	print("Enter the key size:")
	key=int(input())
	encryption(s,key)
else:
	print("Enter your message to be decrypted:")
	s=input()
	print("Enter the key size:")
	key=int(input())
	decryption(s,key)