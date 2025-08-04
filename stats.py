def count_words(string):
    words_list = string.split()
    return len(words_list)

def count_symbols(string):
    count_dic = {}
    for char in string:
        if char.lower() in count_dic:
            count_dic[char.lower()] += 1
        else:
            count_dic[char.lower()] = 1
    return count_dic

def sort_on(items):
    return items["num"]

def sort_dic(dic):
    new_list = []
    for char in dic:
        new_list.append({"char": char, "num": dic[char]})

    new_list.sort(key=sort_on, reverse=True)
    return new_list



