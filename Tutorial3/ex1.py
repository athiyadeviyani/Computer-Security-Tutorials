from Cryptodome.Hash import SHA256

bin_hash = SHA256.new(b"Athiya Deviyani").digest()
printable = bin_hash.hex()
print(printable)