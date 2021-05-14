# Secret Sharing

Secret Sharing implementation using Lagrange interpolation in python.

http://www.eecs70.org/static/notes/n8.pdf

Useful for creating cryptocurrency vaults that prevent people from stealing crypto with access to only one secret.

# USAGE

```
pip3 install -r requirements.txt
python3 secret_sharing
```

# Information

Due to the nature of secret sharing algorithms an attacker cannot gain any new information about the secret unless he has `N` keys. This means that it is possible to distribute a secret amongst ten people and if nine of them get together they will not learn anything about the secret. Typically they are described as 2 of 5 or 3 of 7 keys. This means that of the 7 points generated on a polynomial only 3 are needed to derive the secret key.

# License

This code uses the BSD Simplified License, a permissive license that allows users to do what they please without any liability.
