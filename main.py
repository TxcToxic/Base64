import base64


def encodeString(string: str):
    message = string
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    encodedString = base64_bytes.decode('ascii')
    return encodedString


def decodeString(string: str):
    base64_message = string
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decodedString = message_bytes.decode('ascii')
    return decodedString

str1 = encodeString("En/Decode tuto from -TOXIC-#1835")
print(str1 + " | " + decodeString(str1))
