def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    # if operation == '+':
    #     print(f'Результат: {operand_1 + operand_2}')
    # if operation == '-':
    #     print(f'Результат: {operand_1 - operand_2}')
    # if operation == '*':
    #     print(f'Результат: {operand_1 * operand_2}')
    # if operation == '//':
    #     print(f'Результат: {operand_1 // operand_2}')
    # if operation == '%':
    #     print(f'Результат: {operand_1 % operand_2}')
    # if operation == '/':
    #     print(f'Результат: {operand_1 / operand_2}')


with open('calc.txt') as file:
    a = 0
    cnt = 0
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            a += 1
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в линии {cnt}, не хватает данных для ответа')
            else:
                print(f'Ошибка в линии {cnt}, нельзя перевести в число')

print('Количество ошибок в документе: ', a)