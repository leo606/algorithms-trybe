def merge_sort(word):
    word = list(word)
    # caso base: se já atingiu a menor porção (1):
    if len(word) <= 1:
        return word

    # calculo do pivot: índice que indica onde a palavra será particionada
    # no caso, metade:
    mid = len(word) // 2

    # para cada metade da palavra
    # chama a função merge_sort de forma recursiva:
    left, right = merge_sort(word[:mid]), merge_sort(word[mid:])

    # mistura as partes que foram divididas:
    return merge(left, right, word.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    # enquanto nenhuma das partes é percurrida por completo:
    while left_cursor < len(left) and right_cursor < len(right):
        # compara os dois itens das partes,
        # e insere na lista de mistura o menor:
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # o while acima vai inserir os elementos de forma ordenada

    # quando uma das partes termina devemos garantir
    # que a outra será totalmente inserida na lista de mistura

    # itera sobre os elemtnso restantes na partição "esquerda"
    # inserindo-os na lista de mistura
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    # itera sobre os elemtnos restantes na partição "direita"
    # inserindo-os na string de mistura
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return ''.join(merged)
