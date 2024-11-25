import random

def isMillerRabinPassed(mrc, iterations = 20): # works for all primes
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        print("finished part 1")
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                print(i)
                return False
        return True
 
    # Set number of trials here
    for i in range(iterations):
        print(i)
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True

isMillerRabinPassed(2**82589933)