from collections import defaultdict
# Complete the electionWinner function below.

def electionWinner(votes):
    number_of_voltes_per_candidate = defaultdict(lambda:0)
    for vote in votes:
        number_of_voltes_per_candidate[vote]+=1
    
    maximum_votes = 0
    for k, v in number_of_voltes_per_candidate.items():
        if v > maximum_votes:
            maximum_votes = v

    name_list = []
    for k, v in number_of_voltes_per_candidate.items():
        if v == maximum_votes:
            name_list.append(k)
    
    if len(name_list)==1:
        return name_list[0]
    else:
        lowest_name_lower_case = name_list[0].lower()
        lowest_name = name_list[0]
        for index in range(1, len(name_list)):
            if name_list[index].lower() > lowest_name_lower_case:
                lowest_name = name_list[index]
                lowest_name_lower_case = name_list[index].lower()
        return lowest_name

# print(electionWinner(['Alex','Michael','Harry', 'Harry'])=='Harry')
# print(electionWinner(['Alex','Michael','Alex', 'Michael', 'Harry', 'Harry'])=='Alex')
print(electionWinner(['Michael','Alex', 'Michael', 'Alex','Harry', 'Harry']))
# print(electionWinner(['Alex'
# Michael
# Harry
# Dave
# Michael
# Victor
# Harry
# Alex
# Mary
# Mary]))