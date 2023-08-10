from termcolor import colored 

def сложение(a,b):
    return a + b

def вычитание(a,b):
    return a - b

def умножение(a,b):
    return a * b

def деление(a,b):
    if b == 0:
        print("Это дибилизм!!! Математику не знают.")
        return ""
    return a / b

def разделитель(пример):
    for i in пример:
        if i in '+-*/':
            index = пример.index(i)
            a = int(пример[:index])
            s = пример[index]
            b = int(пример[index+1:])
            return a, s, b
ЗНАКИ = {
    '+':сложение,
    "-":вычитание,
    "*":умножение,
    "/":деление
}
def main():
    правило = """НЕ ИСПОЛЬЗУЙТЕ СКОБКИ, БУКВЫ И ПРОБЕЛЫ"""

    print(colored(правило, 'red'))
    пример = input("Введите пример:")
    a, s, b = разделитель(пример)
    математическая_функция = ЗНАКИ.get(s)
    ответ = математическая_функция(a, b)
    print(ответ)

main()