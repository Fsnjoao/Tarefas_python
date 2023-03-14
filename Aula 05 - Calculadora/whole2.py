contador = 0


while contador <= 100:
    print(contador)
    contador = contador + 1

    if contador == 24:
        print("Não vou Exibir o numero 24")
        continue   
print("Acabou")