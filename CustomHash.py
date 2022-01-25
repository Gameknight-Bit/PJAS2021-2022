### Constants ###
key = 'hello world'
#################

### Helper Functions ###
def hexToBinary(hexNum):
    return padBinary("{0:08b}".format(int(hexNum, 16)))

def binaryToHex(b):
    dec = int(b, 2)
    return str(hex(dec))[2:]

##### BINARY MUTATOR FUNCTIONS #####
def padBinary(b):
    while len(b)%8 != 0:
        b = "0"+b
    return b

def padBinary32(b):
    while len(b)%32 != 0:
        b = "0"+b
    return b

def rightrotate(binary, num):
    while num > len(binary):
        num -= len(binary)

    cutBinary = binary[0 : (len(binary)-num)]
    endBinary = binary[len(binary)-num : len(binary)]
    return (endBinary+cutBinary)

def rightshift(binary, num):
    if num >= len(binary):
        retBinary = ""
        for i in binary:
            retBinary += "0"
        return retBinary
    else:
        cutBinary = binary[0 : (len(binary)-num)]
        endBinary = ""
        for i in range(num):
            endBinary += "0"
        return (endBinary+cutBinary)

def xor(binary1, binary2):
    if len(binary1) != len(binary2):
        print(binary1 + " DOESNT MATCH " + binary2)
        print("Binary lengths dont match to execute XOR calcuation")
        return
    retBinary = ""

    for i in range(len(binary1)):
        res = binary1[i : i+1]

        if binary2[i : i+1] == "1" and res == "1":
            retBinary += "0"
        elif binary2[i : i+1] == "1" and res == "0":
            retBinary += "1"
        elif binary2[i : i+1] == "0" and res == "1":
            retBinary += "1"
        else:
            retBinary += "0"
    
    return retBinary

def notb(binary):
    retBinary = ""
    for i in range(len(binary)):
        res = binary[i : i+1]

        if res == "1":
            retBinary += "0"
        else:
            retBinary += "1"
    return retBinary

def andb(binary1, binary2):
    if len(binary1) != len(binary2):
        print(binary1 + " DOESNT MATCH " + binary2)
        print("Binary lengths dont match to execute and calcuation")
        return
    retBinary = ""

    for i in range(len(binary1)):
        res = binary1[i : i+1]

        if binary2[i : i+1] == "1" and res == "1":
            retBinary += "1"
        else:
            retBinary += "0"
    
    return retBinary

def add(binary1, binary2): #mod 2^32 addition
    num1 = int(binary1,2)
    num2 = int(binary2,2)

    retVal = '{0:08b}'.format((num1+num2) % 4294967296) #4294967296 == 2^32

    return padBinary(retVal)

#####################################

def hash(k): #Main Hashing Algorithm
    #Custom Constant Hash Values#
    hash0 = "6a09e667"
    hash1 = "bb67ae85"
    hash2 = "3c6ef372"
    hash3 = "a54ff53a"
    hash4 = "510e527f"
    hash5 = "9b05688c"
    hash6 = "1f83d9ab"
    hash7 = "5be0cd19"

    kConstants = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
                  0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
                  0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
                  0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
                  0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
                  0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
                  0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
                  0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
                  0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
                  0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
                  0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
                  0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
                  0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
                  0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
                  0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
                  0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
    
    ###### Preprocessesing ######
    binaryKey = ''.join(format(ord(i), '08b') for i in k) #could also use bytearray
    binaryKey += '10000000' #append 1 to end

    while(len(binaryKey)%(512-64) != 0):
        binaryKey += '00000000'

    #SPLIT BINARY INTO 512-64 bit sections!!!!!#

    binLen = '{0:064b}'.format(len(''.join(format(ord(i), '08b') for i in k))) #replace k with section
    if len(binLen) > 64:
        print("ERROR: length of key is TOO LONG!!!")
    else:
        binaryKey += binLen

    #Done with main processing    

    mSchedule = []
    scheduleLen = 0
    while scheduleLen < 16: #Word Processing (32-bit sections)
        mSchedule.append(binaryKey[scheduleLen*32:(scheduleLen+1)*32])
        scheduleLen += 1

    for _ in range(48):
        mSchedule.append('00000000000000000000000000000000')

    #Modifying Zero Indexes#
    i = 16
    while i < len(mSchedule):
        t1 = xor(xor(rightrotate(mSchedule[i-15], 7), rightrotate(mSchedule[i-15], 18)), rightshift(mSchedule[i-15], 3))
        t2 = xor(xor(rightrotate(mSchedule[i-2], 17), rightrotate(mSchedule[i-2], 19)), rightshift(mSchedule[i-2], 10))

        mSchedule[i] = padBinary32(add(add(add(mSchedule[i-16], t1), mSchedule[i-7]), t2))
        i += 1 #counter
    #################################

    #Compression#
    a = hexToBinary(hash0)
    b = hexToBinary(hash1)
    c = hexToBinary(hash2)
    d = hexToBinary(hash3)
    e = hexToBinary(hash4)
    f = hexToBinary(hash5)
    g = hexToBinary(hash6)
    h = hexToBinary(hash7)

    for x in range(64):
        s1 = xor(xor(rightrotate(e, 6), rightrotate(e, 11)), rightrotate(e, 25))
        ch = xor(andb(e, f), andb(notb(e), g))
        temp1 = add(add(add(add(h, s1), ch), padBinary32("{0:b}".format(int(kConstants[x])))), mSchedule[x])
        s0 = xor(xor(rightrotate(a, 2), rightrotate(a, 13)), rightrotate(a, 22))
        maj = xor(xor(andb(a, b), andb(a, c)), andb(b, c))
        temp2 = add(s0, maj)

        h=g
        g=f
        f=e
        e=padBinary32(add(d, temp1))
        d=c
        c=b
        b=a
        a=padBinary32(add(temp1, temp2))
    
    hash0 = binaryToHex(padBinary32(add(hexToBinary(hash0), a)))
    hash1 = binaryToHex(padBinary32(add(hexToBinary(hash1), b)))
    hash2 = binaryToHex(padBinary32(add(hexToBinary(hash2), c)))
    hash3 = binaryToHex(padBinary32(add(hexToBinary(hash3), d)))
    hash4 = binaryToHex(padBinary32(add(hexToBinary(hash4), e)))
    hash5 = binaryToHex(padBinary32(add(hexToBinary(hash5), f)))
    hash6 = binaryToHex(padBinary32(add(hexToBinary(hash6), g)))
    hash7 = binaryToHex(padBinary32(add(hexToBinary(hash7), h)))

    return (hash0+hash1+hash2+hash3+hash4+hash5+hash6+hash7)

#hash(key)
import hashlib

print(hash(key))
