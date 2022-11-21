def is_acceptable_password(password: str) -> bool:
    a = any(map(str.isalpha, password))
    print(a)
    b = any(map(str.isdigit, password))
    print(b)
    password = password.lower()
    if password.find("password") >= 0:
        return False
    """если пароль длиннее 9 - предыдущее правило (около одной цифры), не требуется."""
    if len(password) > 9:
        return True
    if 9 > len(password) > 6:
        if a == True and b == True:
            return True
        else:
            return False
    else:
        return False


"""строка ни в коем случае не должна содержать слово «пароль»."""
password = "short54"
x = is_acceptable_password(password)
print(x)
# password = "muchlonger"
# password = "ashort"
# password = "muchlonger5"
# password = "sh5"
# password = "1234567"