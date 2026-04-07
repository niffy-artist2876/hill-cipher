from cipher import encrypt, decrypt

K = [[3, 3],
     [2, 5]]

msg = input("Enter message: ")
enc = encrypt(msg, K)
dec = decrypt(enc, K)

print("Encrypted:", enc)
print("Decrypted:", dec)