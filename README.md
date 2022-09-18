# Secret Sharing

A Secret Sharing implementation using Lagrange Interpolation in python.

Useful for creating distributed cryptocurrency vaults that are not vulnerable to thiefs.

https://inst.eecs.berkeley.edu/~cs70/sp14/notes/n7.pdf

# Installation 

```
pip3 install -r requirements.txt
```

# Usage
## Encoding
```
./cli.py [secrets needed to decode] [secrets to generate] privatekey
./cli.py 2 3 harsh baby kitchen taste need female bacon suspect crunch market nephew argue apple favorite broken quit pill nose agree pyramid mystery can retire prefer
./cli.py 2 3 0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d
```

## Decoding

```
./cli.py [secrets needed to decode] secret1 secret2 ... 
./cli.py 2 daughter tent state prefer brown race...
./cli.py 2 0xae6ed62adbd8... 0xa5f37981b89b...
```

---
Both 24 word bip0039 and hex private key formats are supported.

# Information

Secret Sharing prevents any group of people with a number of shared secrets that is less than the degree of the secret polynomial equation to guess the secret. For example you could create 10 shared secrets of a nuclear code and distribute them to 10 army generals and make it so it is only possible to reveal the nuclear code if 5 army generals agree to launch a nuke. If 4 or less army generals get together **no information about the secret is revealed** due to properties of [finite fields](https://en.wikipedia.org/wiki/Finite_field_arithmetic).

You can customize this code to allow for 2 of 5 or 3 of 7 or any number 0 < s < t <= p where s is the number of shared secrets needed to find the secret and t is the total number of points on the polynomial that are generated and p is the characteristic prime. I'm using NIST Curve P-384.

# License

This code uses the BSD Simplified License, a permissive license that allows users to do whatever they please without providing any liability.

![crypto nerd](https://imgs.xkcd.com/comics/security.png)
