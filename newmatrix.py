n=5
x=[]
y=[]
count=0
for i in range(0,n):
	for j in range(0,n):
		count=count+1
		x.append(count)
	y.append(x)
	x=[]
disc=[]
#print count
flag=0
p=0
q=0
s=0
while len(disc)!=count:
	if y[p][q] not in disc:
		print y[p][q],flag
		disc.append(y[p][q])
		if flag==0:
			if p+1<n:
				p=p+1
			else:
				flag=1
				s=s+y[p][q]
				
		if flag==1:
			if q+1<n:
				q=q+1
		 	else:
				flag=2
				s=s+y[p][q]

		if flag==2:
			if p-1>=0:
				p=p-1
				print p
			else:
				flag=3
				s=s+y[p][q]
				
		if flag==3:
			if q-1>=0:
				q=q-1
			else:
				flag=0
				s=s+y[p][q]
				 
				
	else:
		s=s+y[p][q]
		if flag==0:
			p=p-1
			q=q+1
			flag=1
		elif flag==1:
			q=q-1
			p=p-1
			flag=2
		elif flag==2:
			p=p+1
			q=q-1
			flag=3
		elif flag==3:
			q=q+1
			flag=0
			p=p-1

print s
