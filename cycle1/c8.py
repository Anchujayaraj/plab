
d = {'name': 'anju', 'place': 'idukki', 'course': 'bca'}

s= sorted(d.items())

print('ascending order : ',s)

s1= dict( sorted(d.items(),reverse=True))

print('descending order : ',s1)
