def char_count(text):
    count = {}

    for char in text:
        if char in count.keys():
            count[char] += 1
        else:
            count[char] = 1

    return count


text_to_check = input('Enter a text: ')
print(char_count(text_to_check))
