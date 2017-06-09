# Plaintext -> binary
def p2b(inp):
    if(inp.lower() == 'a'):
        return('01100001')
    elif(inp.lower() == 'b'):
        return('01100010')
    elif(inp.lower() == 'c'):
        return('01100011')
    elif(inp.lower() == 'd'):
        return('01100100')
    elif(inp.lower() == 'e'):
        return('01100101')
    elif(inp.lower() == 'f'):
        return('01100110')
    elif(inp.lower() == 'g'):
        return('01100111')
    elif(inp.lower() == 'h'):
        return('01101000')
    elif(inp.lower() == 'i'):
        return('01101001')
    elif(inp.lower() == 'j'):
        return('01101010')
    elif(inp.lower() == 'k'):
        return('01101011')
    elif(inp.lower() == 'l'):
        return('01101100')
    elif(inp.lower() == 'm'):
        return('01101101')
    elif(inp.lower() == 'n'):
        return('01101110')
    elif(inp.lower() == 'o'):
        return('01101111')
    elif(inp.lower() == 'p'):
        return('01110000')
    elif(inp.lower() == 'q'):
        return('01110001')
    elif(inp.lower() == 'r'):
        return('01110010')
    elif(inp.lower() == 's'):
        return('01110011')
    elif(inp.lower() == 't'):
        return('01110100')
    elif(inp.lower() == 'u'):
        return('01110101')
    elif(inp.lower() == 'v'):
        return('01110110')
    elif(inp.lower() == 'w'):
        return('01110111')
    elif(inp.lower() == 'x'):
        return('01111000')
    elif(inp.lower() == 'y'):
        return('01111001')
    elif(inp.lower() == 'z'):
        return('01111010')
    elif(inp.lower() == ' '):
        return('00100000')
    elif(inp.lower() == ''):
        return('')
    else:
        return('00000000')

def b2p(inp):
    if(inp.lower() == '01100001'):
        return('a')
    elif(inp.lower() == '01100010'):
        return('b')
    elif(inp.lower() == '01100011'):
        return('c')
    elif(inp.lower() == '01100100'):
        return('d')
    elif(inp.lower() == '01100101'):
        return('e')
    elif(inp.lower() == '01100110'):
        return('f')
    elif(inp.lower() == '01100111'):
        return('g')
    elif(inp.lower() == '01101000'):
        return('h')
    elif(inp.lower() == '01101001'):
        return('i')
    elif(inp.lower() == '01101010'):
        return('j')
    elif(inp.lower() == '01101011'):
        return('k')
    elif(inp.lower() == '01101100'):
        return('l')
    elif(inp.lower() == '01101101'):
        return('m')
    elif(inp.lower() == '01101110'):
        return('n')
    elif(inp.lower() == '01101111'):
        return('o')
    elif(inp.lower() == '01110000'):
        return('p')
    elif(inp.lower() == '01110001'):
        return('q')
    elif(inp.lower() == '01110010'):
        return('r')
    elif(inp.lower() == '01110011'):
        return('s')
    elif(inp.lower() == '01110100'):
        return('t')
    elif(inp.lower() == '01110101'):
        return('u')
    elif(inp.lower() == '01110110'):
        return('v')
    elif(inp.lower() == '01110111'):
        return('w')
    elif(inp.lower() == '01111000'):
        return('x')
    elif(inp.lower() == '01111001'):
        return('y')
    elif(inp.lower() == '01111010'):
        return('z')
    elif(inp.lower() == '00100000'):
        return(' ')
    elif(inp.lower() == ''):
        return('')
    else:
        return('(?)')
