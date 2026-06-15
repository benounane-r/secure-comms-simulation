from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# we are trying to crete a random key shared between node A and B
key = get_random_bytes(16)
# AES-128 needs to be 16 byte key
print("generated key:",key.hex()) # we want to see what the key is

# now we make the message to be sent 
message = b"hello node b, this is a secret message from node a"

#create the cipher object 
cipher = AES.new(key,AES.MODE_EAX)

# and now we encrypt the message 
ciphertext, tag = cipher.encrypt_and_digest(message)

print("nonce:",cipher.nonce.hex())
print("ciphertext:",ciphertext.hex())
print("tag:",tag.hex())

with open("key.bin","wb") as f : 
    f.write(key)
with open("nonce.bin","wb") as f : 
    f.write(cipher.nonce)
with open ("ciphertext.bin","wb") as f : 
    f.write(ciphertext)
with open("tag.bin","wb") as f : 
    f.write(tag)

print ("\nFiles saved node b can now decrypt the message using the key, nonce, ciphertext and tag")


