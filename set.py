s=input("Enter the colors of first set:")
t=input("Enter the colors of second set:")
s1=s.split(" ")
s2=t.split(" ")
u=set(s1)
v=set(s2)
s4=u.intersection(v)
print(s4)
s3=u.difference(v)
print(s3)
s5=u.union(v)
print(s5)
s6=u.isdisjoint(v)
s7=u.symmetric_difference(v)
print(s6,s7)




