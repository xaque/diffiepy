# Project 4: Diffie-Hellman

Run the passoff code with

`python3 diffie.py`

or

`./diffie.py`

You will need `openssl` installed. It should work on Linux and probably macOS. It will generate the numbers p and a and then print them out along with g<sup>a</sup> mod p. Then it will prompt user input for g<sup>b</sup> mod p, after which it will calculate the secret g<sup>ba</sup> mod p.

