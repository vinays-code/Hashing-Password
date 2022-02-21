d = {'a': 'wertghbvcxfghyut76543', 'b': 'sdfgh8765434[09iujy6tfg', 
'c': '343erderty6tghbv', 'd': '32r4fqeuwfnnyeurbre5tre4r', 
'e': 'drew3456765rtfcxdfghgvcdrftg', 'f': 'sdcvbgtfdserty654ew', 
'g': 'sdftre345654rfvcdfgfrd', 'h': 'vgt54e345ty6543esxcvbn', 
'i': 'erfgt5re43edfr434erfgfd',
    'j': '0fgfdrtgtrtfgvbnhbt54ergv', 
    'k': 'dfgtred34rtrfvc76543ertghbvf', 
    'l': 'dfrew2345ty6ygfrtgh', 'm': 'dvfgtr4ew3r4645gre', 
    'n': 'vfgrbfr53rgefbnngbf5re', 'o': 'frgthyju74r34y5htr', 
    'p': 'ergthyt5gr4t3gre', 'q': 'cdr45tyhjnhgfdser45tyhgvfr', 
    'u': 'dfgyt654ew3456yu76tgv','r':'wdefrghy4tgerfr4t3r',
    's':'vgt543w34rfgbhyt65fgr','t':'gtr54e4tgfvcdrt5r4',
    'v':'sdfgt5r44t5y3gte','w':'cdeq4t2yhtw4ber5ht4',
    'x':'dcfvbgthuw46jht','y':'iotu4hg634w34t','z':'ergub99ghbw4589'}
try:
    option = int(input("enter 1 for pass to hash and 2 hash to pass :"))
    if option == 1:
        string=input("entr the password to convert ot hash-")
        hshed_password = ""
        for i in string:
            if i in d:
                hshed_password += d[i]
            hshed_password += '#'
        print("your hashed password-", hshed_password)
    elif option == 2:
        string=input('paste the hashed string here :')
        pas = ""
        realpas = ""
        for i in string:
            if i != '#':
                pas = pas+i
            else:
                for i in d:
                    if pas == d[i]:
                        realpas += i
                pas = ""
        print(realpas)
except Exception as e:
    print(e)
