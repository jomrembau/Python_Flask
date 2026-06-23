from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "password"

hashed_pw = bcrypt.generate_password_hash(password=password)

print(hashed_pw)

# checking hashed password
check = bcrypt.check_password_hash(hashed_pw, "random_wrong_password")

print(check)

