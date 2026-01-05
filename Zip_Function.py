
names = ("Snehal","Pratik","Harsh")
comps = ("Dell","Lenovo","HP")

zipped1 = list(zip(names,comps))
print(zipped1)

zipped2 = set(zip(names,comps))
print(zipped2)

zipped3 = dict(zip(names,comps))
print(zipped3)

for (a,b) in zipped1:
    print(a,b)
