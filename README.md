# Secret Sharing

A Secret Sharing implementation using Lagrange Interpolation in python.

Useful for creating distributed cryptocurrency vaults that are not vulnerable to thiefs.

http://www.eecs70.org/static/notes/n8.pdf

# Usage

```
pip3 install -r requirements.txt
python3 secret_sharing.py
```

# Information

Secret Sharing prevents any group of people with a number of shared secrets that is less than the degree of the secret polynomial equation to guess the secret. For example you could create 10 shared secrets of a nuclear code and distribute them to 10 army generals and make it so it is only possible to reveal the nuclear code if 5 army generals agree to launch a nuke. If 4 or less army generals get together **no information about the secret is revealed** due to properties of [finite fields](https://en.wikipedia.org/wiki/Finite_field_arithmetic).

You can customize this code to allow for 2 of 5 or 3 of 7 or any number 0 < s < t <= p where s is the number of shared secrets needed to find the secret and t is the total number of points on the polynomial that are generated and p is the characteristic prime. I'm using NIST Curve P-384.

# License

This code uses the BSD Simplified License, a permissive license that allows users to do whatever they please without providing any liability.
