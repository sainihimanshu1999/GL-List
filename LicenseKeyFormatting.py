'''It was particularly an easy question'''


def licenseKey(s,k):
    string = s.upper().replace('-','')[::-1]
    return ''.join(string[i:i+k] for i in range(0,len(string),k))[::-1]