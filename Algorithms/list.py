my_list = [41,23]
my_second_list = [42,24]

try:
    print my_list[1] + my_second_list[2]
except:
    print my_list[0] + my_second_list[1]

i,j = (1,2),[3,4]
print i,j

num = 1,2,3
print num #it creates a tuple automatically
num1, num2, num3 = 1,3,5
print num2 #tuple unpacking , u can still do (num2)

# i,j = 1,2,3
# print j #error unpacking
# (i,j) = (1,2,3) #error unpacking
# print j
(i,j,k) = (1,2,3)
print i


our_list = ['Martin','Michael']
for val in enumerate(our_list): #takes the info and turns into a tuple of index,value
    print val
for idx,value in enumerate(our_list):
    print value,idx

name = {"sw": "sara wong","dp" : "deepti velusamy"}
for key in name:
    print key
for key in name:
    print key,name[key]
name = {"sw": "sara wong","dp" : "deepti"}

#gets the key,values
for key,value in name.items():
    print key,value

print name["sw"] #cant use 0/index here

i,j = "sq"
print i
print j
