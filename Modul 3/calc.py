import tkinter as tk


def plus():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 + num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)


def minys():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 - num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)


def multiply():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 * num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)


def divide():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 / num2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)



window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)
button_plus = tk.Button(window, text='+', width=5, height=3, command=plus)
button_plus.place(x=100, y=200)
button_minys = tk.Button(window, text='-', width=5, height=3, command=minys)
button_minys.place(x=150, y=200)
button_multiply = tk.Button(window, text='*', width=5, height=3, command=multiply)
button_multiply.place(x=200, y=200)
button_divide = tk.Button(window, text='/', width=5, height=3, command=divide)
button_divide.place(x=250, y=200)
number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=100, y=75)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=100, y=50)
number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=100, y=130)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=100, y=100)
answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=100, y=285)
answer = tk.Label(window, text='Результат:')
answer.place(x=100, y=260)

window.mainloop()