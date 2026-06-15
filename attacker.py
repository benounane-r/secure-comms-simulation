#attacker has access to both messages 
with open("ciphertext.bin","rb") as f :
    ciphertext1 = f.read()
with open("ciphertext2.bin","rb") as f  :
    ciphertext2 = f.read()
print("ciphertext 1:", ciphertext1.hex())
print("ciphertext 2:", ciphertext2.hex())

#XOR the 2 ciphertexts todether to cancel out the keystream
xor_results = bytes(a ^b for a,b in zip(ciphertext1,ciphertext2))

print("\nXOR of the two ciphertexts:",xor_results.hex())

#if the attacker knows the plaintext of one of the messages, they can easily recover the other message by XORing the result with the known plaintext
# now we XOR with the first message to cancel it out and to be left with the second one 
known_plaintext = b"hello node b, this is a secret message from node a"
recovered_message2 = bytes(a ^ b for a,b in zip(xor_results,known_plaintext))
try:
    print("\nRecovered message 2:",recovered_message2.decode()) 
except UnicodeDecodeError:
    print("\nRecovered message 2 (not valid UTF-8):", recovered_message2)
    print("attack failed - message could not be recovered ")