import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}


def get_slot_machine_spins(rows, cols, symbols):
    all_symbols = []
    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)

    colums = [[], [], []]


def deposit():
    while True:
        amount = input("What would like to deposite? =>Rs.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a number")
    return amount


def get_numbers_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Enter a number")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line => Rs.")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between Rs.{MIN_BET} - Rs.{MAX_BET}")
        else:
            print("Please enter amount within a range")
    return amount


def main():
    balance = deposit()
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not sufficent balance, your current balance Rs.{balance}")
        else:
            break

    print(f"You are betting {bet} on {lines}. Total bets is = Rs.{total_bet}")


main()
