def alienBit(abit):
    decrypted=[]
    encrypt = abit[abit.index(".")+1:]
    start = 0
    finish = 3

    for i in range(len(encrypt)/3):
        code = encrypt[start:finish]
        if code[0] == "0":
            s = list(code)
            s[0]=""
            code = "".join(s)
        elif code[0:2]=="00":
            code.replace("00","")
        decrypted.append(chr(int(code)))
        start += 3
        finish += 3
    return "".join(decrypted)