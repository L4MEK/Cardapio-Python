#Menu
Pizza = 23.99
Lasanha = 36.99
Feijoada = 41.99
#
nome = input("""Cardápio L4MEK
Qual seu nome?
R= """)

#Porção
por = int(input(f"""
{nome}, uma porção para Criança ou Adulto?
[1] Adulto
[2] Criança
R= """))

#Escolha do cliente
if por == 1:
	prato = int(input(f"""
{nome}, você escolheu porção para Adulto. Digite o número de seu pedido:
[1] Pizza
[2] Lasanha
[3] Feijoada
R= """))

#Adulto Pizza
if por == 1 and prato == 1:
	qt = int(input(f"{nome}, você escolheu Pizza. Quantas você deseja?\nR= "))
	print("O valor será R${}".format(int(Pizza * qt)))
	
#Adulto Lasanha
elif por == 1 and prato == 2:
	qt = int(input(f"{nome}, você escolheu Lasanha. Quantas você deseja?\nR= "))
	print("O valor será R${}".format(int(Lasanha * qt)))
	
#Adulto Feijoada
elif por == 1 and prato == 3:
  qt = int(input(f"{nome}, você escolheu Feijoada. Quantas você deseja?\nR= "))
  print("O valor será R${}".format(int(Feijoada * qt)))
  
  
#Criança Pizza
if por == 2:
	prato = int(input(f"""
{nome}, você escolheu porção para Adulto. Digite o número de seu pedido:
[1] Pizza
[2] Lasanha
[3] Feijoada
R= """))
	prato == 1
if por == 2 and prato == 1:
	qt = int(input(f"{nome}, você escolheu Pizza. Quantas você deseja?\nR= "))
	print("O valor será R${}".format(int(Pizza * qt / 2)))
	
#Criança Lasanha
elif por == 2 and prato == 2:
	qt = int(input(f"{nome}, você escolheu Lasanha. Quantas você deseja?\nR= "))
	print("O valor será R${}".format(int(Lasanha * qt / 2)))
	
#Criança Feijoada
elif por == 2 and prato == 3:
  qt = int(input(f"{nome}, você escolheu Feijoada. Quantas você deseja?\nR= "))
  print("O valor será R${}".format(int(Feijoada * qt / 2)))
  
else:
	print(f"{nome}, insira um valor válido!")
