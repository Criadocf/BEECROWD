name = input()
salary = float(input())
sale_total = float(input())
final_salary = (((15/100)*(sale_total))+(salary))

print(f'TOTAL = R$ {final_salary:.2f}')