def replace_all(text, dict):
    text = str(text)
    for i, j in dict.items():
        text = text.replace(i, j)
    return text
