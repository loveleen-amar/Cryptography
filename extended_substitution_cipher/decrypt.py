from exsc import ExtendedSubCipher

ciphertext = input("Enter ciphertext: ")
# key format <seed[str/int/double].no_of_list[int]> eg. secret.123
key = input("Enter key: ")
obj = ExtendedSubCipher(key)
plaintext = obj.decrypt(ciphertext)
print(plaintext)
