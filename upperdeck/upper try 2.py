import time
import random
import requests

def pass_txt():
    open_file = open("pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    return login, password


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


login, password = pass_txt()


