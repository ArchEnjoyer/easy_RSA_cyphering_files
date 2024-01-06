from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5

def keygen(size):
    random_generator = Random.new().read
    key = RSA.generate(size, random_generator) #generate pub and priv key
    return key

def savekeys(key, publickeyname="public_key.pub", privatekeyname="private_key.pub"):
    #exportKey(self, format="PEM", passphrase=None, pkcs=1)
    with open(publickeyname, mode="wb") as public_file:
        public_file.write(key.publickey().exportKey(format="PEM"))
    with open(privatekeyname, mode="wb") as public_file:
        public_file.write(key.exportKey(format="PEM"))

#file, encrypted_file = "text.txt", "text.txt.gpg"
def encrypt_data(file, encrypted_file, publickeyname):
    with open(publickeyname, "rb") as k:
        key = RSA.importKey(k.read())
    cipher = PKCS1_v1_5.new(key)
    encrypted = cipher.encrypt(readdatafromfile(file))
    with open (encrypted_file, "wb") as f:
        f.write(encrypted)


def decrypt_data(encrypted_file, decrypted_file, privatekeyname):
    with open (encrypted_file, "rb") as f:
        data = f.read()
    with open(privatekeyname, "rb") as k:
        key = RSA.importKey(k.read())

    decipher = PKCS1_v1_5.new(key)
    with open (decrypted_file, "w") as f:
        f.write(decipher.decrypt(data, None).decode())
    
def readdatafromfile(path): # encrypt_data is using it
    with open(path, "r") as f:
        text = "".join(f.readlines()).encode("UTF-8")
    return text

def main():
    print("This program will make RSA pair of keys or encrypt/decrypt files with keys")
    choise = input("Select [g] for generate keys,\n       [e] for encrypting file,\n       [d] for decrypting file\nSelection: ")
    if choise == "g":
        size = input("Size of key (1024 min 4096 max): ")
        pubname = input("Name of public key (if no name given, 'public_key.pub'): ")
        privname = input("Name of private key (if no name given, 'private_key.pub'): ")

        if pubname != "": publickeyname=pubname 
        else: publickeyname="public_key.pub"
        if privname != "": privatekeyname=privname
        else: privatekeyname="private_key.pub"

        savekeys(keygen(int(size)), publickeyname, privatekeyname)

    elif choise == "e":
        file = input("Name of file to encrypt: ")
        pubname = input("Name of public key (if no name given, 'public_key.pub'): ")
        if pubname != "": publickeyname=pubname 
        else: publickeyname="public_key.pub"
        encrypt_data(file, file+".gpg", publickeyname)

    elif choise == "d":
        encrypted_file = input("Name of file to decrypt: ")
        decrypted_file = input("Name of file to write decrypted data: ")
        privname = input("Name of private key (if no name given, 'private_key.pub'): ")
        if privname != "": privatekeyname=privname 
        else: privatekeyname="private_key.pub"
        #decrypt_data("text.txt.gpg", "text123.txt", "private_key.pub")
        decrypt_data(encrypted_file, decrypted_file, privatekeyname)

    else:
        print("Something is wrong, I can feel it")




if __name__ == "__main__":
    main()