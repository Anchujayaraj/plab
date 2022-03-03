import csv
d={1:'Smith',2:'John',3:'Mary',4:'Lilly'}
with open("sample.csv","w") as f1:
    csvrdr=csv.writer(f1)
    for item in d.items():
        csvrdr.writerow(item)
with open("sample.csv","r") as f1:
    csvrdr=csv.reader(f1)
    for row in csvrdr:
        print(" ".join(row))
