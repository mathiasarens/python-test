class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i,j = 0,0
        last_character_of_name = ""
        while i < len(typed):
            if name[j] == typed[i]:
                last_character_of_name = name[j]
                if j < len(name)-1:
                    j+=1
                i+=1
            elif last_character_of_name == typed[i]:
                i+=1
            else:
                return False
        return name[j] == typed[len(typed)-1]

solution=Solution()
print(solution.isLongPressedName("alex","aaleex"))
print(solution.isLongPressedName("saeed","ssaaedd"))
print(solution.isLongPressedName("leelee","lleeelee"))
print(solution.isLongPressedName("laiden","laiden"))
print(solution.isLongPressedName("vtkgn","vttkgnn"))
print(solution.isLongPressedName("pyplrz","ppyypllr"))