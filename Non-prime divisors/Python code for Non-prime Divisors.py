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
for i in non_list:
    print(i, end=" ")


 