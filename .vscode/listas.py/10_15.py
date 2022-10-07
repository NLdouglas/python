def nested_sum(list_sum):
    total = 0
    for elemento in list_sum:
        total += sum(elemento)
        return total

input_listas = [[1,2], [3], [4,5,6]]
print(nested_sum(input_listas))