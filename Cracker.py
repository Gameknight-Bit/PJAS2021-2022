import hashlib #used for some hash algorithms like sha and md

password = 'CreepyCoolScientists132'
validChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def hash(s): #Hashing algorithm (Custom or Already Found)
    return hashlib.sha224(s.encode()).hexdigest()

password = hash(password)
