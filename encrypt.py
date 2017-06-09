import translate

def go(etype):
    if etype == 1:
        bread()
    else:
        print("Unknown encryption type.")

def bread():
    ptxt = input("What string would you like to encrypt?\n> ")
    key = input("What is your encryption key?\n> ")

    while len(key) < len(ptxt):
        key += key

    btxt = ''
    for i in ptxt:
        btxt += translate.p2b(i)

    bkey = ''
    for i in key:
        bkey += translate.p2b(i)

    ctxt = ''
    ce = 0
    for i in btxt:
        ctxt += bincry(i, str(bkey[ce]))
        ce += 1
    
    f = open("output.txt", "w+")
    f.write(ctxt)
    f.close()
    
    print("Encypted string:\n" + str(ctxt) + "\nEncrypted string saved to output.txt\n")

def bincry(pbin, kbin):
    if(pbin == kbin):
        return('0')
    else:
        return('1')
