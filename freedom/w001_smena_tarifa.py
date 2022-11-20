import telnetlib
import time

def input_data():
    sw_domen = input("Введите домен свитча =         ")
    sw_port = input(int("Введите порт клиента =         "))
    tariff = input(int("Введите тариф 100/200/500 =         "))
    sw_type = input(int("Введите тип свитча QSW(введите 1) или D-Link(2) =         "))
    pass


def start_terminal():
    """запуск самого терминала"""
    print("Script Start")
    pass


def sw_command_100():
    """Ввод самих команд"""
"""D-link"""
    """config ports X capability_advertised 10_half 10_full 100_half 100_full
    config bandwidth_control X rx_rate no_limit tx_rate no_limit
    save
    y"""
"""QSW"""
    """    conf
    interface ethernet 1/0/x     x берем порт клиента
    speed-duplex auto 10 100
    no bandwidth control
    write
    y"""
    pass


def sw_command_200():
    """Ввод самих команд"""
"""D-link"""
    """config ports X capability_advertised 10_half 10_full 100_half 100_full 1000_full
    config bandwidth_control X rx_rate 215040 tx_rate 215040
    save
    y"""
"""QSW"""
    """conf
    interface ethernet 1/0/x     x берем порт клиента
    no speed-duplex
    bandwidth control 215040 both
    write
    y"""
    pass


def sw_command_500():
    """Ввод самих команд"""
"""D-link"""
    """config ports X """
    """config ports X capability_advertised 10_half 10_full 100_half 100_full 1000_full
    config bandwidth_control X rx_rate 537600 tx_rate 537600
    save
    y"""
"""QSW"""
    """    conf
    interface ethernet 1/0/x     x берем порт клиента
    no speed-duplex
    bandwidth control 537600 both
    write
    y"""
    pass


def sw_end():
"""выводит лог команды проверки смены тарифа"""
print("Дружочек, я всё")
print("Script End")
    pass


input_data()