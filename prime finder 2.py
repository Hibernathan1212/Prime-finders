import time

def prime_finder(n):
    #initializes array with True values
    prime = [True] * (n + 1)
    for i in range(0, n + 1):
        prime[i] = True

    p = 3
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p + p, n+1, p):
                prime[i] = False
        p += 1
    
    #with open("/Users/nathan/Documents/Coding/Prime Numbers 2.txt", "a") as file:
    #    file.write("2\n")
    #    for p in range(3, n+1, 2):
    #        if prime[p]:
    #            file.write(str(p) + "\n")


start = time.time()
prime_finder(200000)
end = time.time()
print(end-start)

#0.23 all primes under 1,000,000
#2.42 all primes under 10,000,000
#32.87 all primes under 100,000,000
