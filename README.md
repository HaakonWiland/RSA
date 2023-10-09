# RSA
RSA cryptography project to decrypt and encrypt text, mainly for learning purposes.   

# General knowledge about RSA  
Encrypt key: e
Private key: d  
Modulus: n 
prime 1: p
prime 2: q 

We then define n = p * q

We have the Euler's totient as:
$\Phi(n)$ = (p - 1) * (q - 1)

We have the congruence:
e * d $\equiv$ 1 mod ($\Phi(n)$)

We say that d, is the modular inverse of e mod $\Phi(n)$.


When breaking the encryption:
To find the private key d, and hence break RSA cryptography, the best way to do this is to factorize n. This would give us p and q, which then would allow us to find d. 


**Overview example on how RSA work:**

Alice: Private_A, Public_A
Bob: Provate_B, Public_B

Say Alice wants to send a message, m, to Bob. 

Define Encryption functin E, and Decryption function D.

Steps:
1. Alice encypt m, using Bobs public key and the encryption function: 
E(public_B, m) = c. This gave us the chipher text c, which is by itself unreadable. 

2. Bob decrypts the cipher text with the decryption function, and his private key: D(private_B, c) = m.

Note that private_B is the only key that can decrypt a cipher made by public_B, hence it should be kept secret.

