print ("hello world")


# this is a comment

#Variables and Multiple assignment

age = 20
sentence = "hi"
print(age)

print (sentence)

sarah, bob , mike = 16,21,17

print(sarah)
print(bob)
print(mike)


sarah = bob = mike

print (sarah, bob, mike)

#arithmetic operators and strings

age1 = 12
age2 = 18

print(age1 + age2) # should be 30

print (age2 - age1) 

print (age2*age1)

print (age2 /age1)
print ("test")
#-------------------------------------
#strings 

sent1 = "today is a beautiful day"

print(sent1)

first = "joe"
last = "he"

print (first + last)
print (first + " " + last)

print (first * 10)

#slicing (each character has an index)
sent = "bozo"
print (sent[0])

#place holders in strings
name3 = "jake"
sentence3 = "%s is %d years old"

#print (sentence3 % name3) #%s = string

print(sentence3 % ("avi", 23))

#f''
name = "Avi"
print (f"Hello, {name3}")
x = 1
y = 2
print (f"sum of x and y is {x+y}")