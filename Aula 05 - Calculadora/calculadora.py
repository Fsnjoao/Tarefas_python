sair = "sair"

while True:
    numero1 = input ("Escreva o primeiro numero: ")
    numero2 = input ("Escreva o segundo numero: ")
    operador = input ("Digite o operador (+-*/): ")

    numero1_float = 0
    numero2_float= 0
    try: #Tentar executar o codigo
        numero1_float = float(numero1)
        numero2_float = float (numero2)

    except: #Caso tenha que executar o codigo
        numero_valido = False

        if numero_valido == False:
            print("Numero invalido. ")

        operador_aceito= ("+-*/")
        if operador not in operador_aceito:
            print("Operador não aceito")



    sair = input ("deseja sair? ").lower().startswith("s")
    if sair is True:
        break


