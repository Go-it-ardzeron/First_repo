is_active =  bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access? "))

if is_admin:
    access = True
else:
    access = is_active and is_permission

print(access)