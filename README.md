# Secure Communications Simulation 
A demonstration of AES-EAX encryption, a vulnerability formed by the reuse of nonce and how its fixed.

## What this project does 
- `node_a.py` : Encrypts the message using AES-EAX and saves it in a file
- `node_b.py` : Reads and decrypts the message while verifying integrity
- `attacker.py` : Demonstrates an attack by exploiting the nonce reuse 

## The vulnerability : Nonce reuse 
AES-EAX require a unique nonce for every encryption that uses the same key. By reusing a nonce, it allows an attacker to XOR 2 ciphertext together which cancels out the keystream and produces `message1 XOR message2`. If one message is known the other message is found without needing the key.

## Running it 
1. Run `python node_a.py` to generate keys and encrypt the messages 
2. Run `python node_b.py` to decrypt and verify the message
3. Run `python attacker.py` to see how the vulnerability is exploited 

## The fix 
Always generate a new unique nonce for every encryption operation with a given key. PyCryptodome does this automatically when you call 'AES.new(key, AES.MODE_EAX)' without specifying a nonce.

## Why This Matters 
Nonce reuse is a real vulnerability class that has affected real-world cryptographic protocols. This project demonstrates both the attack and the defence 