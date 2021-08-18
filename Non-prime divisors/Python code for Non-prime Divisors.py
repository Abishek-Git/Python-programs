"""
Mathematics: Non-prime divisors

For a given intergers N, write a program to find how many non-prime divisors
it has and print them in descending order or ascending order

====================
sample input
24    --- denotes N
====================

sample output
6
1 4 6 8 12 24     ----ascending order
-------------------
6
24 12 8 6 4 1     ----decending order
====================

"""


n = int(input())
list = []

#Appending number to List
[list.append(i) for i in range(n, 0, -1)]

#Appending divisors in divisors
divisors = []
for j in list:
    (divisors.append(j) if((n % j) == 0) else "")

non_list = []
for k in divisors:
    for i in range(2, k):
        if((k % i) == 0):
            non_list.append(k)
            break

count = 1
for m in non_list:
    count += 1

non_list.append(1)
print(count)

#----------------------use below code as per question-------------

#Ascending Order
for i in non_list[::-1]:
    print(i, end=" ")

#Descending Order
for i in non_list:
    print(i, end=" ")

 


 
