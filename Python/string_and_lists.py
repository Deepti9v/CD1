str = "If monkeys like bananas, then I must be a monkey!"
print str.find("monkey")
new_str = str.replace("monkey", "alligator")
print new_str

x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
x = x[0] + x[len(x) - 1]
print x

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
# for i in range(0,len(x)-1): #typically until n-1
#     min_idx = i
#     for j in range(i+1,len(x)): #typically until n
#         if (x[j] < x[min_idx]):
#           min_idx = j
#     tmp = x[i]
#     x[i] = x[min_idx]
#     x[min_idx] = tmp

x.sort()  # alternatively above snippet can be used
remaining = len(x) - (len(x)/2)
l = x[:len(x)/2]
r = x[-remaining:]
# l1 = x[0:len(x)/2]
# r1 = x[len(x)/2:len(x)]
r.insert(0, l)
print r
