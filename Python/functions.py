def odd_even():
    for i in range(1,2001):
        if (i%2 == 0):
            print "Number is",i,"This is an even number"
        else:
            print "Number is",i,"This is a odd number"
    return

def Multiply(a,n):
    result = []
    for i in a:
        result.append(i*n)
    return result

def layered_multiples(arr):
    list =[]
    for i in arr:
        list.append([1]*i);
    return list

a = [2,4,10,16]
odd_even()
print Multiply(a,5)
print layered_multiples(Multiply([2,4,5],3))
