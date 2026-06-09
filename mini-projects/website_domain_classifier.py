URL=input("Enter a website URL : ").lower().strip()

if URL.endswith(".com"):
    type="Commercial"
elif URL.endswith(".org"):
    type="Organisation"
elif URL.endswith(".edu"):
    type="Educational"
elif URL.endswith(".in"):
    type="Indian Domain"
else:
    type="Unknown domain type"

print(f"'{URL}' is a {type} website.")