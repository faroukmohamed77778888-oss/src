email = "Amit_ml@gmail.edu"

if email.count("@") != 1:
    print("Invalid email")
else:
    username = email.split("@")[0]
    part = email.split("@")[1]

    if "." not in part:
        print("Invalid email")
    else:
        domain = part.split(".")[-2]

        print("Username:", username)
        print("Domain:", domain)

        if email.endswith(".com"):
            print("Commercial Domain")
        elif email.endswith(".edu"):
            print("Educational Domain")
        else:
            print("Other Domain")


message = "mocleW EPGTQ"

words = message.split()

word1 = words[0][::-1]
word2 = words[1]

print(word1, word2)


message = "gnirtS PLIO"

words = message.split()

word1 = words[0][::-1]
word2 = words[1]

word2 = word2.replace("I", "E")
word2 = word2.replace("O", "U")

print(word1, word2)


message = "yalpstcejorp EPUVT"

words = message.split()

word1 = words[0][::-1]
word2 = words[1]

word2 = word2.replace("E", "A")
word2 = word2.replace("U", "O")

print(word1, word2)