
def gcdOfStrings(str1: str, str2: str) -> str:
    while str1 != str2:
        if len(str1) >= len(str2) and len(str2)>0:
            if str1.startswith(str2):
                str1 = str1[len(str2):]
            else:
                str1=""
        if len(str2) > len(str1):
            if str2.startswith(str1) and len(str1)>0:
                str2 = str2[len(str1):]
            else:
                str2=""
    return str1

#gcdOfStrings("ABCABC","ABC")
gcdOfStrings("ABC","ABCABC")
gcdOfStrings("LEET","CODE")