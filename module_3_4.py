def single_root_words(root_words, *other_words):
    same_words = []
    for i in range(len(other_words)):
        root_words = root_words.lower()
        other_words_list = list(other_words)
        other_words_list[i] = other_words_list[i].lower()
        count = other_words_list[i].count(root_words) or root_words.count(other_words_list[i])
        if count > 0:
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
