import time

def IsPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

def Is_Prime(n):
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

def Is_prime(n):
    prime = [False] * (n + 1)
    for i in range(0, n + 1):
        prime[i] = False
    
    p = 5
    while (p < n+1):
        if (p % 2 != 0 and p % 3 != 0):
            i = 5
            is_prime = True
            while(i * i <= p):
                if (p % i == 0 or p % (i + 2) == 0):
                    is_prime = False
                    break
                i += 6
            if is_prime:
                prime[p] = True

        j = p + 2
        if (j % 2 != 0 and j % 3 != 0):
            i = 5
            is_prime = True
            while(i * i <= j):
                if (j % i == 0 or j % (i + 2) == 0):
                    is_prime = False
                    break
                i += 6
            if is_prime:
                prime[j] = True
        p += 6
        
    with open("/Users/nathan/Documents/Coding/Prime Numbers.txt", "a") as file:
        file.write("2\n3\n")
        for p in range(5, n+1, 2):
            if prime[p]:
                file.write(str(p) + "\n")

start = time.time()
Is_prime(1000000)
end = time.time()
print(end-start)


##num = 5
##with open("/Users/nathan/Documents/Coding/Prime Numbers.txt", "a") as file:
##    file.write("2\n")
##    file.write("3\n")
##    while num <= 100000:
##        if Is_Prime(num) == True:
##            file.write(str(num))
##            file.write("\n")
##        num += 2
#51 seconds all primes under 10,000,000