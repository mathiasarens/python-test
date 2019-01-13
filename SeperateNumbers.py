# https://www.hackerrank.com/contests/saggezza-coding-test/challenges/separate-the-numbers
def separateNumbers(s):
    if s[0] == "0":
        print("NO")
    else:
        ok = False
        for i in range(1, (len(s)//2)+1):
            num = int(s[0:i])
            first_num = num
            j = i
            while j < len(s):
                next_num = num+1
                next_num_str = str(next_num)
                next_num_str_s = s[j:j+len(next_num_str)]
                if next_num_str != next_num_str_s:
                    break
                else:
                    j+=len(next_num_str)
                    num+=1
            if j == len(s):
                print("YES " + str(first_num))
                ok = True
                break
        if not ok:
            print("NO")
        
separateNumbers("1234")
separateNumbers("91011")
separateNumbers("99100")
separateNumbers("101103")
separateNumbers("010203")
separateNumbers("13")
separateNumbers("1")
separateNumbers("99910001001")
separateNumbers("7891011")
separateNumbers("9899100")
separateNumbers("999100010001")
separateNumbers("4546474849505152")
separateNumbers("454647484950515")
separateNumbers("45464748495051")
separateNumbers("12")
separateNumbers("99")
separateNumbers("891011")