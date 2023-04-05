import random
class DH_Endpoint(object):

    def __init__(self):
        self.public_key1 = random.randint(605, 9635)
        self.public_key2 = random.randint(605, 9635)
        self.private_key = random.randint(605, 9635)
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self):
        partial_key_r = self.generate_partial_key()
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        symb_index = encrypted_message.find('&')
        key = ord(encrypted_message[symb_index+1])
        for c in encrypted_message[:symb_index]:
            decrypted_message += chr(abs(ord(c)-key))
        return decrypted_message
