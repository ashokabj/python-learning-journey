name=input("Enter Driver name : ").strip().title()
vehicle=input("Entr vehicle number : ").strip().upper()
violation=input("Entr violation(Speed / Signal / Parking / drunk) : ").lower()

if violation == "speed":
    fine = 1000
    reason = "Over speed limit" 
elif violation == "signal":
    fine = 500
    reason = "Jumped red signal"
elif violation == "parking":
    fine = 300
    reason = "Illegal parking"
elif violation == "drunk":
    fine = 5000
    reason = "Drunk driving"
else:
    fine = 0
    reason = "No violtion found"

if fine > 0:
    print(f"\n=============== TRAFFIC CHALLAN ==============")
    print(f"Driver name : {name}")
    print(f"Vehicle number : {vehicle}")
    print(f"Offense : {reason}")
    print(f"Fine : {fine}")
    print(f"Status : Challan Issued")

else:
    print(f"No violation recorded for {name}.")