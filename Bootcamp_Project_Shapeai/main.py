import hashlib

name = input("Please Enter Your name:")
hash_n = hashlib.md5(name.encode())
hash_name = hash_n.hexdigest()

print("Your name is in md5:" + hash_name)