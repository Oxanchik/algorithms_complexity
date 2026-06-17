import stack_lifo


def check_balance(expression):
    """Проверяет сбалансированность скобок в строке."""
    stack = stack_lifo.Stack()
    # Словарь соответствия закрывающих и открывающих скобок
    pairs = {')': '(', ']': '[', '}': '{'}
    # Набор открывающих скобок для быстрой проверки
    opening_brackets = set(pairs.values())

    for char in expression:
        if char in opening_brackets:
            # Если скобка открывающая, добавляем в стек
            stack.push(char)
        elif char in pairs:
            # Если скобка закрывающая
            if stack.is_empty():
                return "Несбалансированно"

            top = stack.pop()
            # Проверяем, соответствует ли закрывающая скобка последней открытой
            if top != pairs[char]:
                return "Несбалансированно"

    # Если стек пуст после обработки всей строки, то скобки сбалансированы
    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


# Примеры использования
if __name__ == "__main__":
    test_cases = [
        "(((([{}]))))",  # Сбалансированно
        "[([])((([[[]]])))]{()}",  # Сбалансированно
        "{{[()]}}",  # Сбалансированно
        "}{}",  # Несбалансированно
        "{{[(])]}}",  # Несбалансированно
        "[[{())}]"  # Несбалансированно
    ]

    for test in test_cases:
        result = check_balance(test)
        print(f"{test} -> {result}")

    # Раскомментируйте строку ниже для ввода пользователем
    # user_input = input("\nВведите строку со скобками: ")
    # print(f"{user_input} -> {check_balance(user_input)}")
