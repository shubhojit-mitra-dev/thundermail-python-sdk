from thundermail.thundermail import ThunderMail

mail = ThunderMail("tim_2d7b0a21a482e7b52a95370d34bd4ca9")

try:
    # response = mail.send(
    #     from_email="mitrashubhojit2005@gmail.com",
    #     to="shubhojitmitra1011@gmail.com",
    #     subject="Thundermail-python v0.0.1",
    #     html="<strong>it works!</strong>",
    # )
    response = mail.get("545e97f2-601f-4118-91b8-fd12e134s245")

    print(response)

except Exception as e:
    print(e)
