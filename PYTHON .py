name = "Abdii"
age = 27
price = 88.9
print("my name is :", name)
print("my age is :", age)
print("the price of this thing is :", price)
print("My name is",name , "My age is", age, "I bought this thing and the price of this thing is ", price)
print(type(name))
print(type(age))
print(type(price))

name = "Abdii"
old = False
a = None

print(type(old))

      
print(6+4)
a = 5
b = 3
sum = a - b
print(sum)

print("Hello world")

                                                             # Arithmetic Operators
a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)#reminder
print(a ** b)#power a^b

                                                          # Assignment operators
num = 10
num -= 3
print(num)
# logical operators
print(not False)
print(not True)
a = 7
b = 3
# not
print(not False)
print(not a > b)
# and
val1 = True
val2 = True
print("ans opertor :" , val1 and val2)#true
#or
val1 = True
val2 = False
print ("ans operator :", val1 or val2)#true

# INPUT
input("enter your name :")
name = input("enter your name :")
print("Welcome", name)

val = input ("enter some value :")
print(type(val),val)

val = str(input("enter some value :"))
print(type(val), val)

name = str(input("enter your name :"))
age = int(input("enter your age :"))
subject = int(input("enter your subject :"))

print("welcome", name)
print("your age is", age)
print("your subject is", subject)

                                                           # Practice Question
a = input("enter first number :")
b =input("enter second number :")
sum = int(a) + int(b)

print("sum of two number is :" , sum)

side = float(input("enter square side :"))
print("area = ", side * side)

val1 = float (input("enter first number :"))
val2 = float (input("enter second number :"))

average = (val1 + val2) / 2
print("average of two number is :", average)


a = int(input("enter first number :"))
b = int(input("enter second number :"))
c= (a >= b)
print(" the statement is :",c)


str1 = "My name is Abdullah.\nI work on myself.\nI give time to myself.\n"
print(str1)
#\n is used for next line
#\t is used for space btw lines

                                                               #Basic operation
# 1.concatenation
str1 = "Abdullah"
str2 = "Irfan"
print(str1 + str2)

#2.Length of str
str1 = "Abdullah"
print(len(str1))
str2 = "Irfan"
print(len(str2))
final = str1 + " " +str2
print(len(final))

#Indexing
str = "Abdullah Irfan"
print(str[9])#9 which mention h 
#Slicing
str = "Abdullah Irfan"
print(str[3 : 8])#ullah and start with 0
print(str[:8])#0 to 8
print(str[9:])#9 to end
#step
                                                              #Negative slicing
str = "Abdullah Irfan"
print(str[-14 : -6])#Abdullah -1 not include and start with -1

                                                             #STRING Functions
str = "apna College"
print(str.capitalize())#Apna

str = "Apna college"
str1 = str.endswith("ege")
print(str1)#true

str = "I am study from apna college"
str1 = (str.replace("a", "o"))
print(str1)
str1 = (str.replace("apna college" , "GC Uni"))
print(str1)

str = "i am from studing python from apna college "
# str1 = (str.find("m"))
# print(str1)#3
str1 = (str.find("Q"))
print(str1)#-1  

str = "i am from studing python from apna college "
str1 = str.count("o")
print(str1)#4

                                                             #Practice Q
str = input("enter your name")
print(len(str))

str = "i am from studing python from apna college "
str1 = (str.count("s"))
print(str1)


                                                        # if else condition
light = "Green"
if(light == "Green"):
    print("go")
elif(light == "yellow" ):
    print("wait")
elif(light == "red"):
    print("stop")
  
marks = int(input("enter marks :") )


if(marks >= 90):
    print("A")
elif(marks >= 80):
    print("B")
elif(marks >= 70):
    print("C")
else:
    print("Fail")
    print("end of code")
    
age = int(input("Enter your age"))
if(age>=18):
    print("you are adult")
    print("you can drive")
else:
    print("you are immuture")
    print("end of code")

                                                               # Nesting
age = int(input("enter your age"))

if(age >= 18):
    if(age>= 60):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# Practice Question
number = int(input("Enter a number :"))
if(number % 2 == 0):
     print("Even")
else:
    print("Odd")


                                                           #   list
marks = [ 78, 43, 21, 12, 43, 45,]
print(marks)
student = ["Abdii", "19age", "78marks"]
print(student)
#we also change it
student[0] = "Abdullah"
print(student[0])


                                                            #list slicing
marks = [45, 2, 445, 21, 54, 65, 23]
print(marks[0:3])#45,2,445
print(marks[ :5])
print(marks[-7 : -4])#45,2,445

                                                            #listmethod
list = [1, 3, 5, 2, 6]
list.append(7)#add new number
print(list)

list = [1, 3, 5, 2, 6]
list.sort() #sorting in asending order
print(list)
list = ["Abdii" ,"Maaz" , "Ahsan","Zohaib"]
list.sort()
print(list)

list = [1, 3, 5, 2, 6]
list.sort(reverse = True)#sorting in desending order
print(list)

list = [1, 3, 5, 2, 6]
list.reverse()#reverse
print(list)

list = [1, 3, 5, 2, 6]
list.insert(2,7)#index,element
print(list)

list = [3,4,5,6,8,3,9,3]
list.remove(3)#first occurance remove ,,,like first 3 remove
print(list)

list = [1, 3, 5, 2, 6]
list.pop(2)#remove element form index which i give
print(list)

                                                                #TUPLE

tup = (2,3,4,5,6)#in tuple we use ()
print(tup)
print(len(tup))#5

                                                            #Tuple Methods
#In tuple we canoot change anything
#, is a abreivated of tuple
#same methods like list or string but two imp methods
tup = (1, 2, 3, 4)
print(tup.index(1))#1  , index of 1

tup = (1, 2, 3, 4)
print(tup.count(3))#1   ,counting

#Practice Question
fav1 = input("Enter first movie :")
fav2 = input("Enter second movie :")
fav3 = input("Enter third movie :")
list.append(fav1)
list.append(fav2)
list.append(fav3)
print(list) 

                                                    # palindrome

list1 = ["m", "a", "a", "m"]
copy_list1 = list1.copy()
copy_list1.reverse()
print(copy_list1)

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
   
#count
list = ["C","D","A","A","D","A"]
print(list.count("A"))#

 #sorting
list = ["C","D","A","A","D","A"]
list.sort()
print(list)
 
 #Basic chatgpt questions
list = [1,3,4,5,6]
list.append(7)#add
print(list)

list = [1,3,4,5,6]
list.insert(4,7)#
print(list)


list = [1,3,4,5,6]
list.remove(6)
print(list)

list = [1,3,4,5,6]
list.pop(2)#remove
print(list)

list = [1,3,4,5,6]
print(list[4])#we can access any element

list = [1,3,4,5,6]
list1 = len(list)
print(list1)


                                                            # Dictionary
dict = {
    "name" : "Abdii",
     "age" :   20,
    "class" : "BSCS",
    "subject" : ["C","Java","Python"],
    "89" : "Eighty Nine"
    
    }
dict["name"] = "Abdullah"# we can change name
dict["surname"] = "Irfan"#we can add something
print(dict)

                                                       #Nested Dictionary
dict = {
    "name" : "Abdii",
    "class" : "BSCS",
    "subject" : {#nested
        "Math" : "67",
        "Science" : "78",
        "English" : "90",
        }
 
 }
print(dict["subject"])
#also
print(dict["subject"]["Science"])#78

#Dict Methods

dict = {
    "name" : "Abdii",
     "age" :   20,
    "class" : "BSCS",
    "subject" : ["C","Java","Python"],
    "89" : "Eighty Nine",
}
print(dict.keys())#give all keys  #we also  convert into list
print(dict.values())#give all values

print(dict.items())#in pairs 
print(dict.get("age"))#we use keys to get values 
dict.update({"Teacher" : "Mr Irfan"})#add new key value pair
print(dict)

set

set = {1, 3, 4, 5, 6}
print(set)
print(type(set))


collection = {}#empty dic
print(type(collection))
collection = set ()#empty set
print(type(collection))

                                                        #   set methods
collection = set()
collection.add(1)#add
collection.add(2)
collection.add("Abdullah",)#string
collection.add((1,3,4))#tuple
collection.remove(2)#remove2
collection.clear()#empty set
collection.pop()#remove random value
print(collection)  

set = {1, 3, 4, 5, 6}
set2 = {3,4,5,6,7,8,11}
print(set.union(set2))#union of two sets
print(set.intersection(set2))#intersection of two sets

                                                          # Practice Questions
dict = {
    "table" : ("a piece of furniture","list of facts & figures"),
     "cat" : "a small animal",
     }
print(dict)

set = {"python", "java", "C++","C","javascript"}
print(len(set))

marks = {}
x = int(input("Enter English Marks:"))
marks.update({"English": x})
y = int(input("Enter Urdu Marks:"))
marks.update({"Urdu": y})
z = int(input("Enter Maths Marks:"))
marks.update({"Maths": z})
print(marks)  

items = [
    {"name" :"Banana","category":"fruit"},
    {"name" :"Carrot","category":"vegetable"},
    {"name" :"Apple","category":"fruit"},
]
result = {}
for item in items:
     category = item["category"]
     if category not in result:
         result[category]= []
         result[category].append(item)
print(result)
        
count = 1
while count <= 5:
    print("Hello", count)#5 times hello + numbers
    count += 1
#print 1 to 5 
i = 1
while i <= 5:
    print(i)
    i += 1

#print 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1
#Practice Questions
#1. Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i +=1
#2.Print numbers from 100 to 1
i = 100
while i>=1:
    print(i)
    i -= 1
#3.Multiplication
# n= int(input("Enter the table :"))
i = 1              
while i <=10:
    print(i*7)
    i += 1
#second method
i = 7
while i <=70:
     print(i)
     i += 7
    
4.

nums =  [1,4,9,16,25,36,49,64,81,100]   #print these numbers  
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

nums = [2,3,4,5,6,7,8,9,10,11]
idx = 0
while idx<len(nums):
    print(nums[idx])
    idx +=1
5.found any number


nums = (67,45,23,56,78,77,32,92,77)
x= 77
i = 0
while i < len(nums):
    if(nums[i] == x):
         print("Found at idx",i)#found at idx 5
    else:
        print("Finding.....")#found at idx 8
    i += 1

# break
i = 1
while i <= 5:
    print(i)
    if(i ==3):
        break#123
    i += 1
    
#e.g
num = [23,45,65,76,2,43,65,76,87]

i = 0
while i <=len(num):
    print(num[i])
    if(num[i]==2):
        break #23,45,65,76,2
    i +=1

# continue
i = 1
while i <=10:
    if(i == 7):
        i +=1
        continue
    print(i)
    i += 1
e.g
num = [23,45,6,7,8,5,98,54,332]
i = 0
while i <=len(num):
       print(num[i])
       if(num[i]==7):
           break#23 45 6 7
       i +=1
#e.g
num = [23,45,6,7,8,5,98,54,332]
i = 0
while i < len(num):
    if(num[i] == 7):
        i += 1
        continue
    print(num[i])
    i += 1

# print odd or even number
i = 0
while i <= 100: 
  if(i % 2 == 0):#even  number
      print(i)
      i += 2

i = 1
while i <= 100:
    if(i % 2 !=0):#odd number
        print(i)
        i+=2

# FOR LOOP:
nums = [2,34,4,5,6,7,7,8,9]
for values in nums:
    print(values)#also used for str,tuple
str = "GC university"
for char in str:
    print(char)#u can also use else as a option not a compulsory

# Practice Questions
1.
nums = [1,4,9,16,25,36,49,64,81,100]
for values in nums:
    print(values)
    
2.
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 64

idx = 0                     
for el in nums:
    if el == x:
        print("found at idx",idx)
    idx += 1
                                                                #RANGE
print(range(5))#(o,5)

seq = (range(5))
for el in seq:
    print(el)#0,1,2,3,4 

#method in range
#1.
for i in range(5):#(stop)
 print(i)
#2.
for i in range(1,5):#(start,stop)
    print(i)
#3.
for i in range(2,10,2): #(start,stop,step)
    print(i)#even numbers
for i in range(2,100,2):
    print(i)#even numbers
for i in range(1,100,2):
    print(i)#odd numbers
        
#Practice Questions
                                                              #for loop
#1.
nums = [1,4,9,16,25,36,49,64,81,100]

for values in nums:
    print(values)
#2.
nums = [1,4,9,16,25,36,49,64,81,100]

x= 36
i = 0
for values in nums[i]:
    if values == 36:
        print("found at idx",i)
#3.
for i in range(1,101):#1 to 100
    print(i)
#4.
for i in range(101,0,-1):#100 to 1
    print(i)

# 5.multiplication of n  number
n = int(input("Enter number"))
for i in range(1,11):#start,stop
    print(n*i)

6.
sum = 0
for i in range(1,6):#sum of first 5 natural numbers
    sum += i
    
print("total sum =",sum)
# 7.using while loop

n = 8
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print("Total sum:",sum)

# 8.factorial
n = 5
fact = 1
for i in range(1,6):
    fact*=i
print("factorial of 5 is:",fact)
     
         
                                                        # Functions
def cal_sum(a,b):
    return a+b

#Test the function
print(cal_sum(3,5))
print(cal_sum(6,7))

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()

#average of 3 numbers
def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum /3
    return avg

avg = cal_avg(45,23,87)
print(avg)
#PQ
#1.
list = [1,2,3,4,5,6,7]
cities = ["Tokyo","Paris","Japan","Germany"]

def print_len(list):
    print(len(list))
    
print_len(list)
print_len(cities)

#2.
total = 0
for i in range(4):
    total+=1
    print(total)
def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum /3
    return avg

avg= cal_avg(3,5,7)
print(avg)

def cal_len(list):
    return(len(list))


list = [1,2,4,5,4,3,3,4,5]
print(cal_len(list))


cities = ["Lahore","Karachi","Pindi","Islamabad"]
uni = ["GC","UOL","PU","UCP","LCWU","UMT"]

def cal_len(list):
    return(len(list))

print(cal_len(cities))
print(cal_len(uni))

cities = ["Lahore","Karachi","Pindi","Islamabad"]
uni = ["GC","UOL","PU","UCP","LCWU","UMT"]

def cal_len(list):
    for items in list:
        print(items ,end=" ")
        

print(cal_len(cities))
print(cal_len(uni))

def cal_fac():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print("Factorial of",num,"is",fact)

cal_fac()




num = [2,3,4,3,3,4,7,8,5]
def cal_count(list):
    list1 = list.count(3)
    return list1

print(cal_count(num))


def cal_vowels(text):
    vowels = "a","e","i","o","u"
    count = 0
    for letter in text.lower():
       if letter in vowels:
            count += 1
    return count
str1 = "i love my mom"     
print(cal_vowels(str1))
    

def is_palindrome(word):
    
 word = word.lower()
 reverse = word[::-1]

 if word == reverse:
     return True
 else:
     return False
 

print(is_palindrome("madam"))


list = [4,3,2,5,3,8]
def find_max():
    max_num = list[0]
    for i in list:
        if i > max_num:
            max_num = i
    return i

print(find_max())
        
def get_avg():
    total = int(input("how many numbers : "))
    nums = []
    
    for i in range(total):
        num = int(input("enter number : "))
        nums.append(num)
    return sum(nums) / len(nums)
    
print(get_avg())
  
list = [1,2,3,4,5,6,7,8,9]
num = []
def cal_even():
    for i in list:
        if i % 2 == 0:
            num.append(i)
    return num

print(cal_even())
  

def count_words(sentence):
    words = sentence.split()
    count = len(words)
    return count

print(count_words("I love my mom"))
    
def is_prime(n):
      if n <=1:
        return False
      for i in range(2,n):
        if n % i == 0:
            return False
        return True
    

      
print(is_prime(3))

def count_case(sentense):
    lower = sentense.lower()
    upper = sentense.upper()
    count = 0
    talling = 0
    for letters in sentense:
           if letters.isupper():
               count += 1
           elif letters.islower():
               talling +=1
    return("Upper:", count, "Lower:", talling)
               
           
print(count_case("I Love My Mom"))
            

def remove_duplicate(my_list):   
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

list = [1,2,2,2,5,6,6,8,]
print(remove_duplicate(list))

def cal_sum(n):
    total = 0
    for i in range(n):
        digit = n % 10
        total+=digit
        n = n // 10
    return total


print(cal_sum(3285))

def reverse_string(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

print(reverse_string("HELLO"))
   
   
def reverse_with_while(word):
        reversed = ""
        i = len(word) - 1
        while i >= 0:
            reversed = reversed + word[i]
            i = i - 1
        return reversed

print(reverse_with_while("MYMOM"))

def reverse_words(sentense):
    words = sentense.split(" ")
    reversed_words = [word[::-1] for word in words]
    reversed_sentense = " ".join(reversed_words)
    return reversed_sentense
    

print(reverse_words("I LOVE MY MOM"))
         
    
def analyze_data(my_list):
    mean = sum (my_list) / len(my_list)
    median = sorted(my_list)[len(my_list) // 2]
    mode = max(set(my_list), key = my_list.count)
    return("Mean:",mean,"Median:", median,"Mode:",mode)

print(analyze_data([1,2,4,4,5]))
        
def  count_words(sentence):
    words= sentence.split()
    count = len(words)
    return count

print(count_words("I Love python"))

a = int(input("Enter a number: "))
b= int(input("Enter b number: "))
operation= str(input("Enter operation :"))
sum = a + b
Subtract = a - b
multiple = a * b
division = a / b
if operation == "+":
    print(sum)
elif operation == "-":
    print(Subtract)
elif operation == "*":
        print(multiple)
elif operation == "/":
            print(division)  
            
else:
            print("Invalid operation")
            
            
def most_vowel_word(sentence):
    vowels ="aeiou"
    words = sentence.split()
    count = 0
    max_word = ""
    for word in words:
         for letter in word:
             if letter.lower() in vowels:
                 count += 1
                 if count > len(max_word):
                     max_word = word
    return max_word
print(most_vowel_word("I love python"))

                                               #PRACTICE QUESTIONS OF ALL METHODS
                                                            # 1.for loop

for i in range(1,11):
    print(i)
# 2.
n = int(input("Enter a number n:"))
sum = 0
for i in range(1, n + 1):
    sum +=i
print("The sum of number n:",n, "is:",sum)
3. 
for i in range(1,11):
    print(i)
4.
for i in range(0,21,2):#even number
    
    print(i)
#5.
str = "hello"
for char in str:#h   e  l      l   0  #vertical
    print(char)
6.
for i in range(1,6):
    square = i * i
    print("The square of", i , "is",square)
 #7.   
fruits = ["apple", "banana","cherry"]#list
for char in fruits:
    print(char)
#8.
sum = 0
for i in range(1,101):
    sum += i
print(sum)

9.
nums = [1,2,3,4,5,6,7,8]
for i in nums:
        if i % 2 == 0:
            print(i)#even number
#10.
n = 5
print("Mutliplication of:",n)
sum = 0
for i in range(1,11):
    i *=n
    sum +=1
    
    print("Muliplication of" ,n,"x",sum,"=",i)
11.
numbers = [5, 6, 7]
max_num = numbers[0]  # Start by assuming the first is the biggest

for i in numbers:
    if i > max_num:
        max_num = i

print("The largest number is:", i)

12.
nums = [2,3,4,5,6,7,8,5,4,2,5,7,8]
for i in nums:
    if i == 8:
        break
    print(i)
13.
nums = [1,2,3,4,10,5,6,7,8]
for i in nums:
    if i == 10:
        continue
    print(i)
    i += 1

# while loop
1.
num = 0
while num <= 20:#even number
    print(num)
    num+=2

#2.
n = 5
i = 1
while i <= 10:
    sum = i*n
    print("Multiplication of", n, "x", i, "=", sum)
    i += 1
3.
num = 121
num1 = num.copy()
num1.reverse()
while num1.reverse()!=num:
    print("palindrome")
else:
    print("not palindrome")

4.
str = "I love Python"
str1= len(str)
print(str1)
14-7-25
1.  
for i in range(1,11):
 print(i)
#2.
for i in range(0,11,2):
    print(i)
#3.
for i in range(5,51,5):
    print(i)
#4.
nums = [1,2,3,4,5,6,7,8,9,10]
for i in nums:
    square = i*i
    print(square)
5.
for i in range(10,0,-1):
    print(i)
6.
i = 0
while i <= 9:
    i +=1
    print(i)
#7.
i = 1
sum = 0
while i <= 100:
    sum += i
    print(sum)
    i +=1
8.
i = 0
while i <= 100:
    i +=1
    if i == 47:
        break
    print(i)
9
for value in range(1,51,2):
 print(value)
10
num = int(input("Enter your number: "))
fact = 1
for num in range(1,num +1):
    fact *= num
print("factorial of", num ,"is:",fact)
11.
list = [1,2,2,4,4,4,3,3,5]
list1 = list.count(4)
print(list1)
12.

num = int (input("Enter a number :"))
rev = 0
while num >0:
    digit = num % 10
    rev = rev *10+digit
    num = num // 10
print(rev)
13.
num = int(input("Enter any number :"))
print("Multiplication of",num,"is:")
for i in range(1,11):
    total = num * i
    print(total)
14.
for i in range(1,11):
    square = i*i
    print(square)
15.
for i in range(-10,11):
    print(i)
16.
for i in range(10,101,10):
    print(i)
17.
i = 1
while i <=10:
    print(i)
    i += 1
#18.
i = 2
while i <=20:
    print(i)
    i +=2
19.
num = 12345  
count = 0
while num > 0:           #count digits in a number
    num = num // 10
    count += 1  
print(count)
#20.
num = 1234
rev = 0
while num > 0:                    #reverse numbers
    digit = num % 10
    rev = rev *10+digit  
    num = num // 10
print(rev)
21.
num = 5
fac = 1
while num > 0:
   fac = fac * num
num -= 1
print(fac)
22.
num = 123456
sum_digit = 0
while num > 0:
    digit = num % 10
    sum_digit += digit
    num = num //10
print(sum_digit)
23.
num =1
while num <= 100:
    if num % 5 == 0:
      print(num)
    num +=1
24.
str = "hello"
i = 0
while i <len(str):
  print(str[i])
  i +=1
25.
num = 1
while num <= 100:
  if num % 3 == 0 and num % 7 == 0:
    print(num)
    break
  num+=1
# Find all prime numbers between 1 and 100

# Print Fibonacci series up to N terms

# Count how many vowels and consonants in a string

# Remove duplicates from a list using a loop

# Find the maximum value in a list without using max()

# Build a pattern (e.g., triangle of stars *)

# Find if a number is a palindrome

# Print a multiplication table up to 10x10

# Print only unique characters from a string

# Count frequency of each character in a strin


nums = [5,8,4]
max_num = max(nums)
result = []               # Multiply each internal value of an object by the greatest number found in that object.
for num in nums:
  result.append(num *max_num)
print(result)


nums = [4,7,5]
min_num = min(nums)
result = []                #divide by min number
for num in nums:
  result.append(num / min_num)
print(result)

nums = [2,3,5]
square = 0 
max_num = max(nums)
result = []                  #Create a new list with values squared, then multiply each by the max of the original list.
for num in nums:
  square = num*num
  result.append(square*max_num)
print(result)


nums = [3,4,5,6]
product = 1
max_num = max(nums)
for num in nums:
  if num != max_num:           #Find the product of all numbers in a list except the maximum.
   product *= num
print(product,max_num)


nums = [5,7,3]
max_num = max(nums)
difference = 0
for num in nums:                   #Replace each value in a list with its difference from the maximum value.
  difference = max_num - num
  print(difference)
  
dic = {"a" : 2, "b": 7, "c": 8,}
max_value = max(dic.values())
result = {}

for key in dic:
  result[key] = dic[key] *max_value
print(result)
  
  
nums = [2,3,4,6,5,3,6,4,2,6]
max_num = max(nums)
count  = 0 
for num in nums:                     #Check if the maximum value in a list appears more than once.hehehehhe
  count = nums.count(max_num)
         
print("The maximum value is:",max_num)
print("repeat",count,"Times")


nums = [4,6,7,9]
avr = sum(nums)/len(nums)
new_list = []
for num in nums:     #Write a function that returns a new list with each number multiplied by the average of the list.
  new_list.append(avr * num)
print(new_list)

dic = { "a" : 5,"b" : 15,"c" : 20}
result = {}
for key in dic:
    if dic[key] > 10:
        result[key]=dic[key]*2
print(result)
        
dic = {"a": 5, "b" : 15, "c" : 8}
result = {}
for key in dic:
    if dic[key] < 10:
        result[key]= dic[key]*0
    else:
        result[key] = dic[key]
print(result)


dic = {"a": 7,"b" : 4, "c" : 9, "d" : 2}
result = {}
for key in dic:
    if dic[key] %2==0:
        result[key]= dic[key]
print(result)
        
dic = {"a":6, "b": 23, "c": 12, "d": 11}
count = 0
for key in dic:
    if dic[key] >10:
        count += 1
print(count)
        
dic = {"a":20, "b": 3 , "c": 15, "d": 8}
result ={}
for key in dic:
    value = dic[key]
    result[key] = value *2 if value > 10 else value
print(result)

dic = {"a":5,"b":7,"c":8}
sum = 0
for key in dic:
    sum += dic[key]
print(sum)

dic = {"a" : 20, "b": 12,"c": 77, "d": 3}
max_value = max(dic.values())
result = {}
for key, value in dic.items():
    if value == max_value:
     result[key]= {"value":value,"is MAX":True}
    else:
        result[key] = value
print(result)

dic = {"a": 45, "b": 67, "c": 90}
result = {}
for key,value in dic.items():
    if value > 50:
        result[key] = {"value":value,"isHigh":True}
    else:
        result[key]= value
print(result)

dic = {"a":45, "b": 67, "c": 90}
min_value = min(dic.values())
result = {}
for key, value in dic.items():
    if value != min_value:
        result[key] = value
print(result)


dic = {"a": 45, "b": 89, "c": 30}
result = {}
for key, value in dic.items():
    if value < 50:
        result[key] = "low"
    else:
        result[key] = value
print(result)

dic = {"a": 45, "b": 89, "c": 30}
count = 0
for key, value in dic.items():
    if value > 60:
        count += 1
print(count)

dic = {"a":45, "b":60, "c" : 90}
max_key = max (dic, key=dic.get)
print(max_key) 

dic = {"a": 5,"b":6,"c":8}
result = {} 
for key, value in dic.items():
    result[key]=value*2
print(result)  

dic = {"a": 3, "b": 4, "c": 7, "d": 8}
result = {}
for key, value in dic.items():
    if value%2==0:
        result[key] = value
    print(result)

items = [
    {"name" :"Banana","category":"fruit"},
    {"name" :"Carrot","category":"vegetable"},
    {"name" :"Apple","category":"fruit"},
]
result = {}
for item in items:
     category = item["category"]
     if category not in result:
         result[category]= []
         result[category].append(item)
print(result)




str = "phython is fun"
for char in str:
    print(char)  # prints each character on a new line


num = int(input("Enter any number :"))
print("Multiplication of",num,"is:")
result = 0
for i in range(1,11):
    result = num * i
    print(num,"*",i,"=",result)  


for i in range(1,51):
    if i % 3 == 0:
      print(i)

for i in  range(1,11):
     sq = i**2
     print(sq) 

nums = [2,4,5,2,2,7,2]
count = 0
for num in nums:
    if num == 2:
        count += 1
print(count)  

for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

for i in range(1,5):
    star = "*" * i  
    print(star)

                                                    #    MINI PROJECTS

import random
secret_number = random.randint(1,10)

for i in range(5):
    guess = int (input("Guess a number between 1 and 10:"))
    if guess == secret_number:
        print("Congratulations you won!")
        break
    if guess < secret_number:
        print("Too low, try again!")
    if guess > secret_number:
        print("Too high, try again!")
    else:
        print("Try again")
        print(f" Tries left :{4-i}")
else:
        print("Game Over","The number is:",secret_number)
        print("Do you want to play again?")
        play_again = input("Yes/No:")
        if play_again=="yes": 

num = 1
count = 0
while num < 101:
    if num % 2 == 0:
        count += 1
    num += 1
print(count)

sum = 0
for i in range(1,5):
    sum = i*"*"
    print(sum)

nums = [3,5,7,9]
sum = 0
for i in nums:
    sum += i
print(sum)

num = 123
rev = 0
while num >0:
    digit = num % 10
    rev = rev *10 + digit             #numbers
    num =num // 10
print(rev)

        
num = [1,2,3]             #list
rev =num[::-1] 
print(rev)

import random
secret_number = random.randint(1,10)
guess = 0
while guess!= secret_number:
    guess = int(input("Guess the number: "))
    if guess==secret_number:
        print("You guessed it right")
    else:
        print("Try again")
  

for i in range(0,101,2):
  print(i)
  
  
n = int(input("Enter a number :"))

if (n <=1):
     print("Not prime")
else:
     for i in range(2,n):
        if( n%i==0):
           print("Not prime")
           break
     else:
       print("Prime")
       
import random
secret_number = random.randint(1,10)
guess = int(input("Enter a number:"))
if secret_number == guess :
    print("You guessed it right")
else:
    print("wrong answer")


def cal_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
    
print(cal_factorial(5))

def cal_vowels(str):
    
    vowels = "aeiou"
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count

    
print(cal_vowels("Alhamdulila"))

def find_max(my_list):
    max_num = my_list[0]
    for i in my_list:
        if i > max_num:
           max_num = i
    return max_num
    
print(find_max([1,2,9, 3,4,3,7]))

students = [
    {"name": "Ali", "marks": [85, 90, 92]},
    {"name": "Sara", "marks": [88, 91, 89]},
    {"name": "Zain", "marks": [85, 90, 92]}
]
avr1 = sum ([student["marks"][0] for student in students])/len(students) 
avr2 = sum ([student["marks"][1] for student in students])/len(students)
avr3 = sum ([student["marks"][2] for student in students])/len(students)
print("Average of first marks: ",avr1)
print("Average of second marks: ",avr2)
print("Average of third marks: ",avr3)



        
                  



    




    
    
    



    



         
    







