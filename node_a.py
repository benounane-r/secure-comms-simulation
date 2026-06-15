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


print("we are now testing a vunrability. \nREUSE OF NONCE")
message2 = b"Attack at dawn, meet at the bridge"
cipher2 = AES.new(key,AES.MODE_EAX,nonce=cipher.nonce)
ciphertext2, tag2 = cipher2.encrypt_and_digest(message2)
print("ciphertext 1:",ciphertext.hex())
print("ciphertext 2:",ciphertext2.hex())

with open("ciphertext2.bin","wb") as f :
    f.write(ciphertext2)


print("\n\n\nnow we want to fix this vunrabulity by using a new nonce for the second message")

message2 = b"Attack at dawn, meet at the bridge"
cipher2 = AES.new(key,AES.MODE_EAX)
ciphertext2,tag2= cipher2.encrypt_and_digest(message2)

print("ciphertext 1 :",ciphertext.hex())
print("ciphertext 2 :",ciphertext2.hex())
#showing the have different nonces now
print("nonce 1 ", cipher.nonce.hex())
print("nonce 2 ", cipher2.nonce.hex())

with open("ciphertext2.bin","wb") as f :
    f.write(ciphertext2)

with open("nonce2.bin","wb") as f :
    f.write(cipher2.nonce)
with open("tag2.bin","wb") as f :
    f.write(tag2)
    
