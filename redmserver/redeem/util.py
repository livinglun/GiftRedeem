## file: util.py is a set of functions for the system

import re,random

GIFTLIST = ['gift01','gift02','gift03','gift04','gift05','gift06','gift07','gift08','gift09','gift10']

def checkEmail(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    else:
        return True
    
    
def genRedmCode(email):
        ## ascii 'a' = 97, 'z' = 122
        codespace = []
        for num in range(10):
            codespace.append(str(num))
        for asc in range(97,123):
            codespace.append(str(unichr(asc)))
        for asc in range(65,91):
            codespace.append(str(unichr(asc)))
        
        mailstr = email.replace('@','').replace('.','').replace('_','').replace('-','')
        while len(mailstr) < 8:
            mailstr = mailstr + mailstr
            
        code = ''
        for idx in range(8):
            if idx < len(mailstr)-1:
                sum = 0
                #print mailstr[idx:]
                for ch in mailstr[idx:]:
                    sum = sum + ord(ch)
                code = code + codespace[sum%62]
            else:
                code = code + 'z'
        #print 'code:',code
        return code
        
def getGift(code):
        codesum = 0
        for cha in code:
            codesum = codesum + ord(cha)
        select = codesum%len(GIFTLIST)
        return GIFTLIST[select]