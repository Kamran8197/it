for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")


n = int(input("Ədədi daxil edin: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")


n = int(input("Ulduzların sayını daxil edin: "))
for i in range(n):
    print('*', end='')


for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

hasil = 1 
sum = 0
x = 1
n = int(input("Eded daxil edin: "))
while x < n:
    if x % 2 == 0:
         hasil *= x
    else:
         sum +=x
    x+=1 

print("Hasil: ", hasil)
print("Cem: ", sum)