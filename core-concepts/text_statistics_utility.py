def text_statistics(text):
    words = text.split()

    uppercase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())

    return {
       "Total characters": len(text),
       "Total words": len(words),
       "Uppercase letters": uppercase_count,
       "lowercase letters": lowercase_count
   }

text = input("Enter the text: ")

stats = text_statistics(text)

print(f"Total characters: {stats['Total characters']}")
print(f"Total words: {stats['Total words']}")
print(f"Uppercase letters: {stats['Uppercase letters']}")
print(f"lowercase letters: {stats['lowercase letters']}")