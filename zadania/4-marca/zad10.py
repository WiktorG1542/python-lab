def group_words_by_length(words: list[str]):
    grouped = {}
    for word in words:
        grouped.setdefault(len(word), []).append(word)
    return grouped

print(group_words_by_length(["apple", "banana", "cat", "dog", "elephant", "bat"]))  