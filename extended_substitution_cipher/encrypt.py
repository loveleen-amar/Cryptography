from exsc import ExtendedSubCipher


plaintext = input("Enter plaintext: ")
# key format <seed[str/int/double].no_of_list[int]> eg. secret.123
key = input("Enter key: ")
obj = ExtendedSubCipher(key)
ciphertext = obj.encrypt(plaintext)
print(ciphertext)
