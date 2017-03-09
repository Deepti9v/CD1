def stars(x):
    for i in x:
            if type(i) == str: #if isinstance(x,int)
                print len(i)*i[0].lower()
            else:
                print '*'*i
    return

x = [4, 6, 1, 3, 5, 7, 25]
print stars(x)
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print stars(x)
