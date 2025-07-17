# Считываем результат из last_result.txt
with open('last_result.txt', 'r', encoding='utf-8') as f:
    result = f.read()

# Записываем этот результат в results.txt
with open('results.txt', 'a', encoding='utf-8') as file:
    file.write(result + '\n')
