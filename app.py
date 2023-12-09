from sha256 import sha256

# for dev purposes
inp = input("Please enter your text to be hashed: ")
hashed = sha256.hash(inp)
print(hashed)
