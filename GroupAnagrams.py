def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    result_dict = {}
    for str in strs:
        sort_str = ''.join(sorted(str))
        print(sort_str)
        if sort_str in result_dict:
            result_dict[sort_str].append(str)
        else:
            result_dict[sort_str] = [str]

    return list(result_dict.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))