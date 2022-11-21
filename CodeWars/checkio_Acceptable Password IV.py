def is_acceptable_password(password: str) -> bool:
    a = any(map(str.isalpha, password))
    b = any(map(str.isdigit, password))
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


password = "short"
password = "muchlonger"
password = "ashort"
password = "muchlonger5"
password = "sh5"
password = "1234567"