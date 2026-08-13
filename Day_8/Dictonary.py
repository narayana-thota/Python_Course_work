d={}
d={10:92,12:67,14:80}
'''d[10]=1
print(d)
d[10]=1.0
print(d)
d[10]="narayana"
print(d)
d[10]=(1,2,3,4)
print(d)
d[10]=(2+3j)
print(d)
d[10]=True
print(d)
d[10]=[1,2,3,4,5]
d[10]=1
d[1]=20
print(d)
d[2]=12.3
print(d)
d[3]="narayana"
print(d)
d[4]=2+3j
d[5]=True
d[6]=[1,2,3,4,5]
print(d)
d[7]={1,2,3,4}
print(d)

data={'name':'narayana','course':'pfs','batch':65}
print(85 in data)
print('course' in data)
print(data['name'])
print(data['batch'])
#print(data['age'])
print(data.get('name'))
print(data.get('batch'))
print(data.get('age','key is not present'))
print(data.get('batch','key is not present'))

data={'name':'narayana','course':'pfs','batch':65}
data['age']=21
print(data)
data['phno']=9059374985
print(data)
data.update({"email":"narayanathota67@gmail.com",'py':65})
print(data)
print(id(data))
print(data['py'])

data={'name': 'narayana', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9059374985, 'email': 'narayanathota67@gmail.com', 'py': 65}
data.popitem()
print(data)
data.pop('age')
print(data)
del data['batch']
print(data)
data.clear()
print(data)

data={'name': 'narayana', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9059374985, 'email': 'narayanathota67@gmail.com', 'py': 65}
#print(len(data))
#print(max(data))
#print(min(data))
#print(sorted(data))
print(data.keys())
print(data.values())
print(data.items())

d={1:1,2:2,3:3}
d[4]=4
print(d)
n=d.copy()
n[5]=5
print(n)
print(d)
d.setdefault(1,'thota')
print(d)
 '''
data={'name': 'narayana', 'course': 'pfs', 'batch': 65, 'age': 21, 'phno': 9059374985, 'email': 'narayanathota67@gmail.com', 'py': 65}
d=dict.fromkeys(data.keys(),0)
print(d)






