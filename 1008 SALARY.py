id_emp = int(input())
hor_worked = int(input())
amount_received_per_hw = float(input())

salary = hor_worked*amount_received_per_hw

print(f'NUMBER = {id_emp}\nSALARY = U$ {salary:.2f}')