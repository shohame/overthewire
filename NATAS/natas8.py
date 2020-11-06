
"""
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function
encodeSecret($secret) {
return bin2hex(strrev(base64_encode($secret)));
} """
import string

import pybase64

def bin2hex(hex):
    s = ''
    n = len(hex)
    for i in range(0, n, 2):
        s +=  chr(int(hex[i:i+2], 16))
    return s

encodedSecret = "3d3d516343746d4d6d6c315669563362"

bSecret = bin2hex(encodedSecret)
print (bSecret)
brSecret = bSecret[::-1]
print(brSecret)

secret = pybase64.b64decode(brSecret)
print (secret)
