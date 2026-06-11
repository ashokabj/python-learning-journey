boy_name=input("Enter boy name : ")
boy_age=int(input("Enter boy age : "))
girl_name=input("Enter girl name : ")
girl_age=int(input("Enter girl age : "))
age_diff=abs(boy_age-girl_age)  # sometimes boy might be younger so we used absolute
print(f"Boy name : {boy_name}")
print(f"Girl name : {girl_name}")
print(f"Age differene : {age_diff}")
print(boy_name+" loves "+girl_name+" and their age difference is "+str(age_diff)) #Normal concatination method
#can only concatenate str (not "int") to str,so we wrote str(age_diff)
print(f"{boy_name} loves {girl_name} and their age difference is {age_diff}")  # formated string method
'''We use tripple quotes
 for multiline comment'''