class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words = []
        if len(list1) < len(list2):
            for string in list1:
                if string in list2: 
                    if words: 
                        if list1.index(string)+list2.index(string) < words[0]:
                            words.append(list1.index(string)+list2.index(string))
                            words.append(string)
                        elif list1.index(string)+list2.index(string) == words[0]:
                            words.append(list1.index(string)+list2.index(string))
                            words.append(string)
                    else:
                        words.append(list1.index(string)+list2.index(string))
                        words.append(string)
        else: 
            for string in list2:
                if string in list1: 
                    if words: 
                        if list1.index(string)+list2.index(string) < words[0]:
                            words = []
                            words.append(list1.index(string)+list2.index(string))
                            words.append(string)
                        elif list1.index(string)+list2.index(string) == words[0]:
                            words.append(list1.index(string)+list2.index(string))
                            words.append(string)
                    else:
                        words.append(list1.index(string)+list2.index(string))
                        words.append(string)
        output = []
        for idx in range(len(words)): 
            if idx % 2 != 0: output.append(words[idx])
        return output
                    