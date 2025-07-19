import random
import string as s


chars= " " + s.punctuation + s.digits + s.ascii_letters
chars=list(chars)

keys=chars.copy()
random.shuffle(keys)


#encryption
pas=input("Enter the password:")
ecry=""

for letters in pas:
    index=chars.index(letters)
    ecry+=keys[index]

print(f"Encrypted password:{ecry}")
