import encrypt
#import decrypt

def main():
    while 1:
        edDec(enType())
        inp0 = 'notset'
        while inp0 == 'notset':
            inp1 = input("Would you like to encrypt again? (y/n)\n> ")
            if inp1 == 'y':
                inp0 = 'y'
                print('\n')
            elif inp1 == 'n':
                exit()
            else:
                print('Answer not recognised. Please retry using \'y\' or \'n\'\n')

def enType():
    etype = 'notset'
    while etype == 'notset':
        inp0 = input("What encryption type would you like?\n01) Breadcrypt\n99) Exit\n> ")
        if inp0 == '01' or inp0 == '1':
            print("Encryption type set.\n")
            return 1
        elif inp0 == '99':
            exit()
        else:
            print("Type unknown, please try again.\n")

def edDec(etype):
    ed = 'notset'
    while ed == 'notset':
        inp0 = input("Would you like to encrypt or decrypt?\n01) Encrypt\n02) Decrypt\n99) Change encryption type\n> ")
        if inp0 == '1' or inp0 == '01':
            ed = 'e'
            print("Selected encryption\n")
            encrypt.go(etype)
        elif inp0 == '2' or inp0 == '02':
            #ed = 'd'
            print("Selected decryption, but it isn't yet supported. Please select another option.\n")
            #decrypt.go(etype)
        elif inp0 == '99':
            print('\n')
            enType()
        else:
            print("Type unknown, please try again.\n")

main()
