import hashlib #used for some hash algorithms like sha and md
import time
from HashingPlayground import hash

password = 'pjas' #Is Encrypted before testing
realPassword = 'pjas' #Used for storing debug vars
validChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
maxPasswordLength = 10

### HASHING ALGORITHMS ###
def hashSHA224(s): #Hashing algorithm (In Library)
    return hashlib.sha224(s.encode()).hexdigest()

def hashSHA256(s): #Hashing algorithm (In Library)
    return hashlib.sha256(s.encode()).hexdigest()

def hashMD5(s): #Hashing algorithm (In Library)
    return hashlib.md5(s.encode()).hexdigest()

def customHash(s): # customHash def in HashingPlayground.py
    return hash(s)
###########################

def writeToFile(algorithmName, passwordHash, realPass, password, runtime, iter):
    linesToAdd = ['', "------------------", algorithmName+" Hashing '"+realPass+"'", str(iter)+" Iterations", "Runtime: "+str(runtime)+" seconds", "Hash: "+passwordHash, "Password: "+password, "------------------", ""]
    with open('results.txt', 'a') as f:
        f.writelines('\n'.join(linesToAdd))

from itertools import chain, product
def generateCharCombos(chars, maxlen): #Generates all combonations to iterate through
    return (''.join(c)
        for c in chain.from_iterable(product(chars, repeat = i)
        for i in range(1, maxlen+1)))

# Brute Force Algorithm #

## Custom Hash 'pja' ## 
#password = customHash('pja')
#realPassword = 'pja'
#unencryptedPass = ""

#repeated = 0
#start = time.time()

#for combo in generateCharCombos(validChars, maxPasswordLength):
#    repeated += 1
#    if repeated%1000 == 0:
#        print("Iteration: "+str(repeated)+" | Test Case: "+combo)
#    hashedVersion = customHash(combo)
#    if hashedVersion == password:
#        unencryptedPass = combo
#        break

#writeToFile("Custom Hash", password, realPassword, unencryptedPass, time.time()-start, repeated)
#print("Completed in: "+str(time.time()-start)+" seconds | with "+str(repeated)+" iterations!")
#print("Password was: "+unencryptedPass)
#print("Hash was: "+password)
########################

## Custom Hash 'pjas' no uppercase/numbers ##
#password = customHash('pjas')
#realPassword = 'pjas'
#validChars = 'abcdefghijklmnopqrstuvwxyz'
#unencryptedPass = ""

#repeated = 0
#start = time.time()

#for combo in generateCharCombos(validChars, maxPasswordLength):
#    repeated += 1
#    if repeated%1000 == 0:
#        print("Iteration: "+str(repeated)+" | Test Case: "+combo)
#    hashedVersion = customHash(combo)
#    if hashedVersion == password:
#        unencryptedPass = combo
#        break

#writeToFile("Custom Hash", password, realPassword, unencryptedPass, time.time()-start, repeated)
#print("Completed in: "+str(time.time()-start)+" seconds | with "+str(repeated)+" iterations!")
#print("Password was: "+unencryptedPass)
#print("Hash was: "+password)
###################################################

cycle = 1 #0 = MD5, 1 = SHA224, 2 = SHA256

while cycle < 3:
    if cycle == 0:
        password = hashMD5('1sD5q')
    elif cycle == 1:
        password = hashSHA224('1sD5q')
    else:
        password = hashSHA256('1sD5q')
    
    realPassword = '1sD5q'
    validChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    unencryptedPass = ""

    repeated = 0
    start = time.time()

    for combo in generateCharCombos(validChars, maxPasswordLength):
        repeated += 1
        if repeated%1000000 == 0:
            print("Iteration: "+str(repeated)+" | Test Case: "+combo)
        if cycle == 0:
            hashedVersion = hashMD5(combo)
        elif cycle == 1:
            hashedVersion = hashSHA224(combo)
        else:
            hashedVersion = hashSHA256(combo)
        if hashedVersion == password:
            unencryptedPass = combo
            break
    
    if cycle == 0:
        writeToFile("MD5", password, realPassword, unencryptedPass, time.time()-start, repeated)
    elif cycle == 1:
        writeToFile("SHA224", password, realPassword, unencryptedPass, time.time()-start, repeated)
    else:
        writeToFile("SHA256", password, realPassword, unencryptedPass, time.time()-start, repeated)
    print("Completed in: "+str(time.time()-start)+" seconds | with "+str(repeated)+" iterations!")
    print("Password was: "+unencryptedPass)
    print("Hash was: "+password)
    cycle += 1

print("DONE!")
