'''
Rebuild Sentences
'''
def rebuild_sentence(words, lengths):
    sentence_rebuilded = []
    for length in lengths:
        for word in words:
            if len(word) == length:
                sentence_rebuilded.append(word)
                words.remove(word)
                break
    return ' '.join(sentence_rebuilded)


words = ["hello", "world", "my", "name", "is", "hassan"]
lengths = [5, 6, 2, 4, 2, 5]
print(rebuild_sentence(words, lengths))