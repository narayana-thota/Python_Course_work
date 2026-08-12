'''
s=set()
type(s)
#s1=set(input("enter values"))
#print(s1)
s2={1,2,35,565,565,65,6565,65659,654,54554,565}
print(s2)
s={"narayana","narayana","narayana"}
print(s)
s=set()
s.add(1)
s.add("narayana")
s.add(True)
#s.add([1,2,3,4,5])
s.add((1,2,3,4,5))
#s.add({1,2,3,4})
s.add({"name":"narayana","age":21})
print(s)

s1={1,2,3,4}
s2={4,5,6,7}
print(s1 | s2)
print(s1 & s2)
print(s1-s2)
print(s1^s2)

s={1,2,3,4,5,6}
print({1}<=s)
print({7}<=s)
print({1,2}>=s)

m={1,2,3}
n={4,5,6}
print(n.isdisjoint(m))
a={1,2,3}
b={3,5,6}
print(b.isdisjoint(a))

m={5,56,5,59,595,56,5}
print(sorted(m))
print(max(m))
print(min(m))
print(len(m))
print(sum(m))
print(any(m))
m1={5,56,5,59,595,56,5,"narayana"}
print(any(m1))

m={5,56,5,59,595,56,5}
m1=m
m1.add(75)
print(m1)
print(m)

m={5,56,5,59,595,56,5}
m1=m.copy()
m1.add(75)
print(m1)
print(m)
'''
m={5,56,59,595}
m.update([2,3])
print(m)
m.pop()
print(m)
m.remove(59)
print(m)
#m.remove(59)
m.discard(59)

a=frozenset({1,2,3,4})
#print(a)
for i in a:
    print(i)


















