import math as m
import argparse


def three_arg():
    if None in all_num:
        all_num.remove(None)
        if None in all_num:
            print("Incorrect parameters")
            return True
        return False


def interest_in():
    if loan_interest is None:
        print("Incorrect parameters")
        return True
    return False


def not_minus():
    for num in all_int_num:
        if num < 0:
            print("Incorrect parameters")
            return True
    return False


def test():
    if three_arg() or not_minus() or interest_in():
        return True


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")  # principal
parser.add_argument("--periods")  # number
parser.add_argument("--interest")  # load interest
parser.add_argument("--payment")  # monthly payment

args = parser.parse_args()
stop = 0
all_num = [args.principal, args.periods, args.interest, args.payment]
all_int_num = []

func_type = args.type
if all_num[0] is not None:
    principal = int(all_num[0])
    all_int_num.append(principal)
else:
    principal = None

if all_num[1] is not None:
    number = int(all_num[1])
    all_int_num.append(number)
else:
    number = None

if all_num[2] is not None:
    loan_interest = float(all_num[2])
    all_int_num.append(loan_interest)
else:
    loan_interest = None

if all_num[3] is not None:
    monthly_payment = float(all_num[3])
    all_int_num.append(monthly_payment)
else:
    monthly_payment = None

if func_type == "annuity":
    if not test():
        i = (loan_interest / 100) / 12
        if principal is None:
            first_temp = m.pow(1 + i, number)
            second_temp = (i * first_temp) / (first_temp - 1)

            principal = round(monthly_payment / second_temp)
            print(f"Your loan principal = {principal}!")
        elif monthly_payment is None:
            temp = m.pow(1 + i, number)

            monthly_payment = m.ceil(principal * ((i * temp) / (temp - 1)))
            print(f'Your annuity payment = {monthly_payment}!')
            print(f'Overpayment = {principal - monthly_payment * number}')
        else:
            temp_a = monthly_payment / (monthly_payment - i * principal)
            temp_b = 1 + i

            number = m.ceil(m.log(temp_a, temp_b))
            if (number % 12) == 0:
                year = number // 12
                print(f'It will take {year} years to repay this loan!')

            print(f'Overpayment = {principal - monthly_payment * number}')
elif func_type == "diff":
    if not test():
        if monthly_payment is not None:
            print("Incorrect parameters")
        else:
            i = (loan_interest / 100) / 12
            month = 1
            temp = 0
            for j in range(number):
                diff_payment = m.ceil((principal / number) + i * (principal - (principal * (month - 1)) / number))
                temp += diff_payment
                month += 1
                print(f"Month {j+1}: payment is {diff_payment}")
            print(f'\nOverpayment = {-principal + temp}')

else:
    print("Incorrect parameters")
