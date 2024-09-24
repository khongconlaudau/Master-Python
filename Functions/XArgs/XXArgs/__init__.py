def save_user(**user):    # This is called Dictionary **
    print(user["id"])
    print(user["name"])
    print(user)

save_user(id=1, name="Mason", age=20)