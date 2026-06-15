from Crypto.Cipher import AES

with open("key.bin","rb") as f:
    key=f.read()
with open("nonce.bin","rb") as f:
    nonce = f.read()

with open("ciphertext.bin","rb" ) as f :
    ciphertext=f.read()
with open("tag.bin","rb") as f:
    tag = f.read()
 
# now we have all the files we need to decrypt the message
print("node b got the message ")
print("ciphertext:",ciphertext.hex())

# we create the cipher object using the key and nonce to decrypt
cipher = AES.new(key,AES.MODE_EAX,nonce = nonce)
# now we can decrypt the message and verify the tag
plaintext = cipher.decrypt_and_verify(ciphertext,tag)
print("\n decrypted message:",plaintext.decode())