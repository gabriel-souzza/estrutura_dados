from stack import Stack

if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        """
        Adiciona o item na pilha principal e, se for o novo mínimo (ou igual ao atual),
        adiciona também na pilha de mínimos.
        """
        # CORREÇÃO: Faltava adicionar na pilha principal!
        main_stack.push(data)
        
        # Se a pilha de mínimos estiver vazia ou o novo dado for menor/igual ao topo
        if min_stack.is_empty() or data <= min_stack.peek():
            min_stack.push(data)

    def pop_aux():
        """
        Remove o item da pilha principal e sincroniza com a pilha de mínimos.
        """
        if main_stack.is_empty():
            return None
            
        popped_value = main_stack.pop()
        
        # Se o valor que saiu da principal for o mínimo atual, removemos da min_stack
        if not min_stack.is_empty() and popped_value == min_stack.peek():
            min_stack.pop()
        
        return popped_value

    def get_min():
        """
        Retorna o valor mínimo em tempo O(1) apenas olhando o topo da min_stack.
        """
        if min_stack.is_empty():
            raise IndexError("A pilha está vazia")
        return min_stack.peek()

    # --- Testes ---
    print("Empilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Adicionado 5 -> Min atual: {get_min()}")

    push_aux(3)
    print(f"Adicionado 3 -> Min atual: {get_min()}")

    push_aux(7)
    print(f"Adicionado 7 -> Min atual: {get_min()}")

    push_aux(2)
    print(f"Adicionado 2 -> Min atual: {get_min()}")

    push_aux(8)
    print(f"Adicionado 8 -> Min atual: {get_min()}")

    print("\nDesempilhando e monitorando o mínimo:")
    
    val = pop_aux() # Remove 8
    print(f"Removeu {val} -> Min atual: {get_min()}")

    val = pop_aux() # Remove 2 (o antigo mínimo)
    print(f"Removeu {val} -> Min atual: {get_min()}")

    val = pop_aux() # Remove 7
    print(f"Removeu {val} -> Min atual: {get_min()}")

    val = pop_aux() # Remove 3 (outro mínimo)
    print(f"Removeu {val} -> Min atual: {get_min()}")

    val = pop_aux() # Remove 5
    print(f"Removeu {val}")

    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado ao tentar ler pilha vazia: {e}")