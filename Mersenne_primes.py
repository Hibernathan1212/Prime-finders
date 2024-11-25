import time

def isPrime(p):
    num = 2 ** p - 1
    term = 4 % num

    for i in range(1, p - 1):
        term = term * term
        term = term - 2 
        term = term % num
        #print(i)
        #print(term)

    if (term == 0): 
        return True
    else: 
        return False

#with open("/Users/nathan/Documents/Coding/yes1.txt", "a") as file1:
#    with open("/Users/nathan/Documents/Coding/yes2.txt", "a") as file2:
#        for i in range(1,15000, 50):
#            start = time.time()
#            isPrime(i)
#            end = time.time()
#            file1.write(str(i) + "\n")
#            file2.write(str(end - start) + "\n")

start = time.time()
print(isPrime(3169))
end = time.time()
print(end-start)