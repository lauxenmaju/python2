print (" Programa Expresso\n")
print ("1 Cadastrar Restaurante")
print ("2 Listar Restaurante")
print ("3 Ativar Restaurente")
print ("4 Sair\n")


opcao_digitada = int(input("Escolha uma opção"))
print ("Você selecionou:",opcao_digitada, "\n")

if(opcao_digitada==1):
    print ("Voce escolheu Cadastrar Restaurante\n")
elif(opcao_digitada==2):
    print ("Voce escolheu Listar Restaurante\n")
elif(opcao_digitada==3):
    print ("Voce escolheu Ativar Restaurante\n")
else:
    print ("Voce escolheu sair\n")
