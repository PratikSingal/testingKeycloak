def convertToPEM(base64):
    result = ''
    lines = 0
    start = 0
    while start < len(base64):
        result+= base64[start:start+64] + '\n'
        lines = lines + 1
        start = len(result) - lines

    return "-----BEGIN PUBLIC KEY-----\n" + result + "-----END PUBLIC KEY-----"




