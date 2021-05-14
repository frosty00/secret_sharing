# Secret Sharing

Secret Sharing implementation using Lagrange Interpolation in python.

http://www.eecs70.org/static/notes/n8.pdf

Useful for creating cryptocurrency vaults that prevent people from stealing crypto with access to only one secret.

# USAGE

```
pip3 install -r requirements.txt
python3 secret_sharing
```

# Information

Secret Sharing uses Lagrange Interpolation in a prime field to prevent any group of people that is less than the degree of the secret polynomial equation to guess the secret. For example you could distribute a shared secret of a nuclear code to 10 army generals and make it so it is only possible to reveal the nuclear code if 5 army generals get together. If 4 or less army generals get together **no information about the secret is revealed** due to properties of [finite fields](https://en.wikipedia.org/wiki/Finite_field_arithmetic).

You can customize this code to allow for `2 of 5` or `3 of 7` or any other parameters to distribute your secret. 

# License

This code uses the BSD Simplified License, a permissive license that allows users to do what they please without any liability.
