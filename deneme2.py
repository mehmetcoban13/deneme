import time
number = int(input("Please enter a number to check whether it is prime or not : "))
counter = 0
first = time.perf_counter()
for i in range(2, number+1):
    prime = True
    for j in range (2, i-1):
        if i % j == 0 :
            prime = False
            break
    if prime :
        counter += 1
#time.sleep(10) # 10 saniye oyunca uyur
print("\nThere are(is)", counter, "prime number(s) up to", number)
time.sleep(5)
elapsedTime = time.perf_counter() - first
print("Elapsed time :", elapsedTime)

