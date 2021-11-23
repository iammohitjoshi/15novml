Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
##Q2
5**9
1953125
3//2
1
7//3
2
7/3
2.3333333333333335
6 == 6
True
a=20; a+=30; a%3; print(a)
2
50
True * False
0
True &False
False
True and False
False
((6>3) and (7<4) or (False >True) and (False <= True))
False
s1 = "Nice to have it "
s2 = "here"
s1 += s2
s1
'Nice to have it here'
##q3^^
##q4
a=[1,2,[3,4],[5,[100,200,[hello]],23,11],1,7]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a=[1,2,[3,4],[5,[100,200,[hello]],23,11],1,7]
NameError: name 'hello' is not defined. Did you mean: 'help'?
A=[1,2,[3,4],[5,[100,200,[hello]],23,11],1,7]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    A=[1,2,[3,4],[5,[100,200,[hello]],23,11],1,7]
NameError: name 'hello' is not defined. Did you mean: 'help'?
a
50
A
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
A=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
A
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
A[3][1][2]
['hello']
s1 = "Nice to have it "
s2 = "here"
##q5
type(A)
<class 'list'>
s1 += A
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s1 += A
TypeError: can only concatenate str (not "list") to str
s1.append(A)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s1.append(A)
AttributeError: 'str' object has no attribute 'append'
s1.join(A)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s1.join(A)
TypeError: sequence item 0: expected str instance, int found
A.append(0,s1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    A.append(0,s1)
TypeError: list.append() takes exactly one argument (2 given)
A.insert(0,s1)
A.append(s2)
A
['Nice to have it ', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
##q6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
for i in numbers:
    if(i%2==0)
    
SyntaxError: expected ':'
for i in numbers:
    if(i%2==0):
        print(i)
        elif(i==237):
            
SyntaxError: invalid syntax
for i in numbers:
    if(i%2==0):
        print(i)
    elif(i==237):
        break

    
386
462
418
344
236
566
978
328
162
758
918
for i in numbers :
    if(i==237)
    
SyntaxError: expected ':'
for i in numbers:
    if(i==237):
        break
    elif(i%2==0):
        print(i)

        
386
462
418
344
236
566
978
328
162
758
918
##Q7

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1 - color_list_2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(color_list_1 - color_list_2)
NameError: name 'color_list_2' is not defined. Did you mean: 'color_list_1'?
color_list_1 - color_list_2
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    color_list_1 - color_list_2
NameError: name 'color_list_2' is not defined. Did you mean: 'color_list_1'?
color_list_2 = set(["Red", "Green"])
print(color_list_1 - color_list_2)
{'Black', 'White'}


##Q8

string=input("enter the sentence to be checked -")
enter the sentence to be checked -a brown fox jumped over a lazy dog
sting=string.strip()
string=string.upper()
dictionary={}
flag=1
for i in range(65,91):
    dictionary[chr(i)]=0
    for i in string:
        if(ord(i)>=65 and ord(i)<=90):
            dictionary[i]+=1
  for i in dictionary:
      
SyntaxError: unindent does not match any outer indentation level
string=input("enter the sentence to be checked -")
enter the sentence to be checked -a brown fox jumped over a lazy dog
sting=string.strip()
string=string.upper()
dictionary={}
flag=1
for i in range(65,91):
    dictionary[chr(i)]=0
    for i in string:
        if(ord(i)>=65 and ord(i)<=90):
            dictionary[i]+=1
            
enter the sentence to be checked -a brown fox jumped over a lazy dog
sting=string.strip()
string=string.upper()
dictionary={}
flag=1
for i in range(65,91):
    dictionary[chr(i)]=0
    for i in string:
        if(ord(i)>=65 and ord(i)<=90):
            dictionary[i]+=1
            
SyntaxError: multiple statements found while compiling a single statement
##Q9

n=input(("Enter a number - "))
Enter a number - 5
num1=n
num2=n*2
num3=n*3
print(int(num1)+int(num2)+int(num3))
615

##Q10
