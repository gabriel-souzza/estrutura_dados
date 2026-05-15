def h_index_linear_decrescente(citacoes):
    h = 0
    for i in range(len(citacoes)):
        if citacoes[i] >= i + 1:
            h = i + 1
        else:
            break 
    return h

def h_index_binaria_decrescente(citacoes):
    start = 0
    end = len(citacoes) - 1
    h = 0
    while start <= end:
        middle = (start + end) // 2
        if citacoes[middle] >= middle + 1:
            h = middle + 1
            start = middle + 1
        else:
            end = middle - 1
    return h
            
        





citacoesExemplo = [1, 1]

citacoesLazaro = [43, 24, 6, 3, 3, 2, 1, 1]
citacoesFelizardo = [30, 16, 14, 9, 6, 6, 5, 4, 2, 2, 2]
citacoesEduardo = [39, 24, 20, 13, 12, 9, 7, 6, 6, 5, 2, 2, 2, 0, 0, 0, 0, 0, 0]

print("Busca Linear (h-index) Exemplo:", h_index_linear_decrescente(citacoesExemplo))
print("Busca Binária (h-index) Exemplo:", h_index_binaria_decrescente(citacoesExemplo))
print()
print("Busca Linear (h-index) Felizardo:", h_index_linear_decrescente(citacoesFelizardo))
print("Busca Binária (h-index) Felizardo:", h_index_binaria_decrescente(citacoesFelizardo))
print()
print("Busca Linear (h-index) Lazaro:", h_index_linear_decrescente(citacoesLazaro))
print("Busca Binária (h-index) Lazaro:", h_index_binaria_decrescente(citacoesLazaro))
print()
print("Busca Linear (h-index) Eduardo:", h_index_linear_decrescente(citacoesEduardo))
print("Busca Binária (h-index) Eduardo:", h_index_binaria_decrescente(citacoesEduardo))