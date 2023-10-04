
Encrypt key: e
Private key: d  
Modulus: n 
prime 1: p
prime 2: q 

We then define n = p * q

We have the Euler's totient as:
$\Phi = (p - 1) * (q - 1)

We have the congruence:
e * d $\equiv$ 1 mod ($\Phi(n)$)

To find the private key d, and hence break RSA cryptography, the best way to do this is to factorize n. This would give us p and q, which then would allow us to find d. 




