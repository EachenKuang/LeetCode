def descend(s: str):
    ans = []
    current_word = []
    for i in s:
        if i.isalpha():
            current_word.append(i)
        else:
            if current_word:
                ans.insert(0, "".join(current_word))
                current_word = []
    if current_word:
        ans.insert(0, "".join(current_word))
    return " ".join(ans)

eval()