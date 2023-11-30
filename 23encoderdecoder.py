#encoding and decoding in python

import base64
def encoder():
    message = input("Message to be encoded>> ")
    message_in_bytes = bytes(message,"utf-8")
    encoded_message = base64.b64encode(message_in_bytes)
    print(f"Encoded: {encoded_message}")

def decoder():
    message2 = input("Message to be decoded>> ")
    message2_in_bytes = bytes(message2,"utf-8")
    decoded_message = base64.b64decode(message2_in_bytes)
    print(f"Encoded: {decoded_message}")

print("Python Decoder and Encoder")

print("1.Encoder")
print("2.Decoder")

option = int(input("Select option >> "))

if option==1:
    encoder()

elif option==2:
    decoder()

else:
    print("error try again")