numbers = ["3","4","5"] #we take string value in list it shows error

numbers = list(map(int,numbers))# this create int value in list

#for i in range(len(numbers)):# we created for loop to convert string value to integer unless using for loop we can use map function
 #   numbers[i]=int(numbers[i])

numbers[2]=numbers[2]+1
print(numbers[2])



# filter function
a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))
print(c) # prints out [2, 5, 3]

#reduce function
list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x*y, list1)

print(num)