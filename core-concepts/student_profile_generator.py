def create_profile(**details):
    if not details:
        print("No profile details provided")
        return
    
    print("======= Student rofile  =======")

    for key,value in details.items():
        print(f"{key} --> {value}")
    
create_profile(
    name="Ashok",
    age=19,
    branch = "AI & DS",
    college = "BGSCET",
    city = "Bengaluru"
    )
