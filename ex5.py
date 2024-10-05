import json
import os


class CaesarCipher:
    def __init__(self, key):
        self.key = key

    # encrypte thae string according to the self key using casarCipher
    # return the encrypted string
    def encrypt(self, string):
        encryptString = ""
        newKey = self.key % 26
        if newKey == 0:
            return string
        for char in string:
            if char.isalpha():
                number = ord(char) + self.key
                if 90 < number < 97 and char.isupper():
                    number = number - 26
                elif number < 64:
                    number = number + 26
                elif number > 122:
                    number = number - 26
                elif 90 < number < 97 and char.islower():
                    number = number + 26
                char = chr(number)
                encryptString += char
            else:
                char = char
                encryptString += char
        return encryptString

    # decrypte the string to the original string that was encryprted with the key using casarCipher
    # return the decrypted string
    def decrypt(self, string):
        copySelf = CaesarCipher(self.key * -1)
        return copySelf.encrypt(string)


class VigenereCipher:
    def __init__(self, list):
        self.list = list

    # encrypte thae string according to the self key using casarCipher
    # return the encrypted string
    def encrypt(self, string):
        maxLen = len(self.list)
        index = 0
        encryptedString = ""
        for chl in string:
            if chl.isalpha():
                if index == maxLen:
                    index = 0
                new_Key = CaesarCipher(self.list[index])
                encryptedString += new_Key.encrypt(chl)
                index = index + 1
            else:
                encryptedString += chl
        return encryptedString

    # decrypte the string to the original string that was encryprted with the key using VigenereCipher code
    # return the decrypted string
    def decrypt(self, string):
        tempSelf = VigenereCipher([-x for x in self.list])
        return tempSelf.encrypt(string)


# convert a text/string  into int key according to the alphabet order
# return a new object type VigenereCipher with the int keys
def getVigenereFromStr(key):
    newList = []
    keyTemp = key.lower()  # to preserve the original key
    for index in keyTemp:
        if index.isalpha():
            newList.append(ord(index) - ord('a'))
    return VigenereCipher(newList)


# encrypt the text using the cipher class of the encryptor
def encryptFile(encryptor, inputtxt):
    return encryptor.encrypt(inputtxt)


# decrypt the text using the cipher class of the encryptor
def decryptFile(encryptor, inputtxt):
    return encryptor.decrypt(inputtxt)


#
def loadEncryptionSystem(dir_path):
    fileName = os.path.join(dir_path, "config.json")
    with open(fileName, 'r') as f:
        loadedDict = json.load(f)

    encrypSysType = loadedDict["type"]  # the type:Vigenere or Caesar
    encrypSysKey = loadedDict["key"]  # the key to the code
    encrypt = loadedDict["encrypt"]  # true to encrypt- flase to decrypt
    targetFile = ".txt" if encrypt else ".enc"  # the target file type according to encrypt-txt/decrypt-enc
    resultFile = ".enc" if encrypt else ".txt"  # output file to be saved in according to encrypt-enc/decrypt-txt
    
    if encrypSysType == "Vigenere":
        if isinstance(encrypSysKey, str):
            encryptObj = getVigenereFromStr(encrypSysKey)
        else:
            encryptObj = VigenereCipher(encrypSysKey)
    if encrypSysType == "Caesar":
        encryptObj = CaesarCipher(encrypSysKey)

    for currentInput in os.listdir(dir_path):
        filePath = os.path.join(dir_path, currentInput)
        name, fileType = os.path.splitext(currentInput)
        if fileType == targetFile:
            with open(filePath, 'r') as file:
                content = file.read()
                if encrypt:
                    newData=encryptFile(encryptObj, content)
                else:
                    newData = decryptFile(encryptObj, content)
            newFile = name + resultFile
            with open(os.path.join(dir_path, newFile), 'w') as outputFile:
                outputFile.write(newData)
