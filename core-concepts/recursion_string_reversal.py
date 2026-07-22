def reverse_string(text):
    if not text:
        return ""

    return reverse_string(text[1:]) + text[0]


text = input("Enter the text: ")
reversed_text = reverse_string(text)

print(f"Original String: {text}")
print(f"Original String: {reversed_text}")
