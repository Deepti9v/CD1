i = 20
print i
i = 30
print i
print 4+5
print "hi" + " hello"
print "hi"+`3`
print "hi",3,"again" #There is space printed before ,

''' Sample code starts here '''
name = "zen"
print "My name is "+name
print "hello"+`4`
first_name = "Hello"
second_name = "Code"
print "My name is {} {}".format(first_name,second_name)
my_string = "hello world"
print my_string.capitalize()
print my_string #It shows the original string, cos you are not changing the string
my_string = "HELLO WORLD"
print my_string.lower()
my_string = 'HeLlo WoRLD'
print my_string.swapcase()
my_string = "apple pie"
print my_string.find("le ") #-1, not found, anything else, the starting index
my_string = "egg ham bacon egg egg"
print my_string.replace("egg","kitty")
print my_string #shows egg ham bacon
print my_string.replace("egg","kitty",2) #only first two occurences

ninjas = ['hi','hello']
mylist = ['4',['list','in',6,9.0],9343]
empty_list = []

fruits = ['apple','banana']
vegetables = ['lettuce','cucumber']
fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables * 3

x = [2,3,"hi"]
x = x + x # tried x+5, but hey, you can concatenate only list to a list
print x

x.append("new guy") #Appends to the end of the list
print x

x.insert(3,"old guy")
print x

x.remove(2) #removes the element 2 from the list
x.pop(2) #removes the element from index 2
x.pop() #removes the last element
print x

my_list = [1,'yen','hi','zen']
print len(my_list)
print max(my_list)
my_list = [0.8,1,2,4]
print min(my_list)

my_list = [0,"hi"] #0 is considered false
print any(my_list)
print all(my_list)
my_list = [1,1]
print all(my_list)

''' tuples '''
tuple_data = ('physics', 'chemistry', 1997, 2000)
for i in tuple_data:
    print i
print tuple_data[0]

dog = ("barks","bites")
dog = dog + ("domestic",)
dog = dog + ("doggy",)

print dog[1:] #prints from the first
dog = dog[:3] + ("man's best friend",) + dog[3:]
print dog

value = ("Michael","Instructor","Coding Dojo")
(name,position,company) = value
print name,position,company
print len(value)

print min(value)
tuple_falsey = (0,False,'',0,0,[])
print any(tuple_falsey)
tuple_truey = (1,True,[12],(1,2))
print any(tuple_truey)
print all(tuple_truey)

num = (1,2,3,4)
for index,item in enumerate(num):
    x= (index,item) #this makes it a tuple?
    print str(index)+"="+str(item) #you need to convert to str else,it will give error unsupported operand type(s) for +: 'int' and 'str'

num = (1,5,4,3)
print sorted(num) #and returns list: sorted is for tuples
print tuple(sorted(num)) #this converts it into tuple
# print num.sort() #You can use sort only on list

print tuple(reversed(num))

def get_circle_area(r):
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c,a)
