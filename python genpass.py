import random
def genpass():
    alphabet="abcdefghijklmnopqrstuvwxyz0123456789"
    password=""

    for i in range(6):
        password+=random.choice(alphabet)

    return password

print(genpass())
print(genpass())
print(genpass())

