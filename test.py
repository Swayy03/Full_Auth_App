from werkzeug.security import generate_password_hash,check_password_hash

password1 = "Samson"
password2 = "Samson"

hashed_password1 = generate_password_hash(password1)
if check_password_hash(hashed_password1, password2):
    print("They are same")
else:
    print("A lie")

