n=input("Enter a Password : ")
if len(n)>=8:
    len_score=1
else:
    len_score=0
if any(char.isupper() for char in n):
    lower_score=1
else:
    lower_score=0
if any(char.islower() for char in n):
    upper_score=1
else:
    upper_score=0
if any(char.isdigit() for char in n):
    num_score=1
else:
    num_score=0
has_special = any(not (char.isalnum() or char.isspace()) for char in n)
if has_special:
    char_score=1
else:
    char_score=0
score=len_score+lower_score+upper_score+num_score+char_score
if score>=5:
    print("Password Strength : Highly Strong")
elif score==4:
    print("Password Strength : Strong")
elif score>=2:
    print("Password Strength : Medium")
else:
    print("Password Strength : Weak")
#suggestion
print("Suggestion: ")
if len(n) < 8:
    print("-Increase password length")
if not any(char.isdigit() for char in n):
    print("-Add a number")
if not any(char.isupper() for char in n):
    print("-Add atleast one upper case")
if not any(char.islower() for char in n):
    print("-Add atleast one lower case")
if not has_special:
    print("-Add a special character")