l="Ashdeit@12"
upper=False
lower=False
digit=False
special=False
space=False
for i in l:
    if i.isupper():
        upper=True
    elif i.islower():
        lower=True
    elif i.isdigit():
        digit=True
    elif i==" ":
        space=True
    else:
        special=True
if len(l)>=8 and upper and lower and digit and special and not space:
    print("valid password")
else:
    print("invalid password")

