import re

def isValid(s):
    character_count = {}
    for i, c in enumerate(s):
        character_count[c] = character_count.get(c, 0) + 1
    count_1_value = 0
    count_2_value = 0
    count_1_count = 0
    count_2_count = 0
    for count in character_count.values():
        if count_1_value == 0:
            count_1_value = count
            count_1_count +=1
        elif count == count_1_value:
            count_1_count+=1
        elif count_2_value == 0:
            count_2_value = count
            count_2_count+=1
        elif count == count_2_value:
            count_2_count+=1
        else:
            return "NO"
    if count_2_count == 0 or ((count_1_count == 1 or count_2_count == 1) and (abs(count_1_value-count_2_value) == 1 or (count_1_count==1 and count_1_value==1) or (count_2_count==1 and count_2_value==1))):
        return "YES"
    else:
        return "NO"


print(isValid("aaabbcc"))
print(isValid("aaaabbcc"))
print(isValid(""))
print(isValid("a"))
print(isValid("aa"))
print(isValid("aab"))
print(isValid("abbcc"))
print(isValid("aabbcd")) # => NO
print(isValid("aabbccddeefghi"))
print(isValid("abcdefghhgfedecba"))
print(isValid("aaaabbcc"))
print(isValid("ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd")) # => YES
print(isValid("aaaaabc"))
