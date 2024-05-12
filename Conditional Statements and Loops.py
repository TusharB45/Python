for n in range(1,11):
    print (n * 2)

for x in range(1,31):
    if x % 2 == 1:
        print (x, end = " ")
    else:
        print ("Even", end = " ")

for item in range(len(n)):
    print (n[item] * 10, end = " ")
  
nums = [1,35,12,24,31,51,70,100]
def count(numbers):
    numbers = sorted(numbers)
    tot = 0
    
    while numbers[tot] < 20:
        tot += 1
    return tot
count(nums)
