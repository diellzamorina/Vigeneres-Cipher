# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:59:30 2023

@author: HP
"""

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def generate_table(self):
        self.table = []
        for i in range(26):
            row = []
            for j in range(26):
                row.append(chr((j + i) % 26 + ord('A')))
            self.table.append(row)

    def print_table(self):
        for row in self.table:
            print(row)

    def encrypt(self, message):
        message = message.upper()
        ciphertext = ""
        key_index = 0
        for char in message:
            if char.isalpha():
                row = ord(self.key[key_index]) - ord('A')
                column = ord(char) - ord('A')
                ciphertext += self.table[row][column]
                key_index = (key_index + 1) % len(self.key)
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        message = ""
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                row = ord(self.key[key_index]) - ord('A')
                column = self.table[row].index(char)
                message += chr(column + ord('A'))
                key_index = (key_index + 1) % len(self.key)
            else:
                message += char
        return message
    
    
    
cipher = VigenereCipher("VIG")
cipher.generate_table()
cipher.print_table()

message = "THE BOY HAS THE BAG"
ciphertext = cipher.encrypt(message)
print(ciphertext) #Output: ZFY FMQ JAY WXF GII