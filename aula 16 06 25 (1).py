# print("Boa noite")
# print(5+10)
# print((5+10)/3)
# print(7 | 5)
# print(~10)
# print(~33)
# print(~9)
# print(~3)
# a=2
# b=3
# if a==b:
#     print("sim")
# elif(a!=b):
#     print("não")
# else:
#     print("Fim")
# git clone \\caminho\ para copiar um arquivo
# git add .   
# git commit -m "Comentario"
# git push
# _nome = 'Jr'
# nome ='jr'
# nome2 = 'jr'
# nome_2 = 'jr'
# calculo = 5 ** 25 /2 - 2 + 10
# calculo1 = 10** 2 + 3
# print(calculo)
# print(calculo1)
# idade = int(input(' >> ')) # tipo texto
# tipo =  type(idade) 
# print(idade, tipo)
# idade =  float(input('2'))
# idade2 = float(input('3'))
# print("boa noite")

# Exrecicio 1
# nota1 =int(input("primeira nota"))
# print("Coloque a primeira nota")
# nota2 =int(input("segunda nota"))
# print("Coloque a segunda nota")
# nota3 =int(input("primeira nota"))
# print("Coloque a primeira nota")
# print((nota1+nota2+nota3)/3)
# media =((nota1+nota2+nota3)/3)
# if media >7:
#     print("Passou")
# else :
#     print("Reprovado")

# Exercicio 2
# IMC = peso / altura.2
# peso =int(input("Informe o peso"))
# print("coloque o peso")
# altura =int(input("Informe a altura"))
# print("Informe a altura")
# print(((altura*2) / peso))

# Exercicio 3
# print("*** Seja bem vindo  ***")
# valorcompra= float(input('Informe o valor da compra: '))
# desconto= 0.50
# print("desconto")
# valorfinal= float(valorcompra-(valorcompra*desconto))
# if valorcompra > 100:
#     print('Valor com desconto de: ', valorfinal)
# else:
#         print('Valor sem desconto: ', valorcompra)
# ValorDesconto = (valorcompra*desconto)


# Exercicio 4
# print(" Papel Pedra Tesoura")
# Pedra= "Pedra"
# Tesoura= "tesoura"
# Papel= "papel"
#




#jogo de pedra,papel, tesoura. 
#a = (input("papel pedra ou tesoura"))
#b = (input("papel pedra ou tesoura"))

#if a == "papel" and b == "pedra":
#    print("papel ganha")
#elif a == "papel" and b == "papel":
#    print("empate")
#elif a == "papel" and b == "tesoura":
#    print("tesoura ganha")
#elif a == "tesoura" and b == "pedra":
#    print("pedra ganha")
#elif a == "tesoura" and b == "tesoura":
#    print("empate")
#elif a == "tesoura" and b == "papel":
#    print("papel ganha")
#elif a == "pedra" and b == "papel":
#    print("papel ganha")
#elif a == "pedra" and b == "tesoura":
#    print("pedra ganha")
#elif a == "pedra" and b == "pedra":
#    print("empate")

# contador = 0
# while contador <= 10:


    
# (contador % 2 == 0)
# contador=True
#         print("impar")
# contador=False                                        preciso rever este codigo e corrigilo
#         print("par")
#         print(contador)
#      contador += 1

#
# for com range()  repetição com numeros 
# esse é o mais comun para contagem:
#a = range(o,5)
#print(a)

# 1° inicio 
# 2° fim
# 3° contador 
#sacola_de_feira = ("maça", "laranja", "abacate", "banana")
#for i in sacola_de_feira:   
#    print(i)

#sacola_de_feira = ("1°","2°","3°","4°","5°")
#for i in sacola_de_feira:   
#    print(i)

#j=1
#sacola_de_feira = ["maça","banana","abacate","kiwi","melancia","cachorro", "papagaioa","teste"]
#sacola_de_feira.sort()# (sort.()) faz a lista em ordem alfabética 
#for i in sacola_de_feira:   
#    print("item n°"+str(j)+" = "+str(i))  
#    j+=1 


#Tupla 
#imutável
# a =(1,2,3,4,5,6,7,8,9)
# print(a) # busca o conjunto 

# for item in a: # busca item por item 
#     print(item)


# frutas = ["maça", "bana", "uva"]

# for i, fruta in enumerate(frutas): #este codigo numera uma lista do pacote de variavel conforme descrito
#         print(f"{i+1}: {fruta}") 
#para uma listagem com dados em colunas alinha cada um
# #



#  5.for com dicidionario

# dados={8:"nome",3:"ana",7:"idade"}

# #print(dados.values())


# for chave in dados:
#     print(chave) # só a chave 

# for valor in dados. values():
#     print(valor)# só ovalor 

# for chave, valor in dados . items():
#     print (f"{chave} -~ {valor}:)") #chave e valor 

# 6. for com ist coprehension(forma compacta)
#forma curta de crirar lista com for
# lista = [0,1,2,3,4,5,6]
# dicionario = {1:"a" , 2:"b", 3:"c"}
# quadrados = [x for x in range(0,500, 10)]
# quadrados = [(r,a) for r,a in dicionario.items()]
# print( quadrados)
# print (dicionario)


# x=1
# y=3

# for i in range (x,y+1): #para cada (i =elemento)
#     print(i)#escreva a variavel +1


# x=15+1
# y=0
# t=3

# for i in range(y,x,t):
#     print(i)

# x=[1,2,3]
# for i in x:
#      print(i)


# frutas=("banana", "maça", "abacate")

# for i in frutas:
#      print(i)

# frutas=("banana", "maça", "abacate")
# for  i in reversed (frutas):
#       print(i)

# frutas=("banana", "maça", "abacate")
# for i in enumerate  (frutas):
#     print(i)

# frutas=('banana', 'maça', 'abacate',"melancia")
# etiqueta=("1°","2°","3°","4°")
# preço=("R$3,99", "R$2,99","R$1,99", "R$4,99")
# for i,j,a in zip (etiqueta,frutas,preço):
# #    print(f"{i:<5},{j:<10},{a:<10}")




 # #✅ 1. Com range() Enunciado: Imprima todos os números pares de 0 a 200 e pule de 11 à 11. 


# for num in range(0, 201,11):#para cada numero (em range de 0 á 201 pule 11 em 11 )
#     if num % 2 == 0:  # condição de numeros par , função de cada numero (numeros par =%2==0)
#          print(num)


# #✅ 2. Com lista Enunciado: Dada a lista de animais = ["gato", "cachorro", "pássaro", “tigre”],
# #  imprima cada animal com a frase: "Animal: " antes do nome.
# animais=("Gato", "Cachorro", "Pássaro", "Tigre")# tipo=("Animal","Animal","Animal")
# for i,a in zip ( animais, tipo ):
#      print  (f"{i:<5},{a:<5}" ) 


# # ✅ 3. Com enumerate()
# # Enunciado: Imprima os índices e nomes da lista ["Ana", "Bruno", "Carlos"].
# # Depois faça o mesmo exercício invertendo os elementos.
# nomes= ("Ana", "Bruno", "Carlos")
# for i in zip (nomes):
#      print(i)    

# for i in reversed  (nomes):
#      print(i)             


# ✅ 4. Com zip()
#  Enunciado: Dadas duas listas produtos = ["Arroz", "Feijão", “Café”, “Leite”] e precos = [5.20, 4.50, 4.57, 5.3], imprima o nome do produto seguido do preço.
# produtos=("Arroz","Feijão","Cafe", "Leite")
# preços = ( 5.20,  4.50,  4.57,  5.3)
# real=("R$", "R$","R$","R$")
# qualidade= ("alta", "média", "baixa","sub")          
# for i,a,j,t in zip (produtos,real,preços, qualidade,):
#      print(f"{i:<10}, {a:<1} , {j:<5},{t:<5}")           





# ✅ 5. Com string
# Enunciado: Imprima cada letra da palavra "Python é a melhor linguagem do mundo" em uma linha.

# linguagen = ("Python é a melhor linguagem do mundo")
# for i in (linguagen):
#      print(i)
# a=3

# def imprimir( ):
#     a=4
#     print(a)
    
# imprimir( )
# print(a)    

# a=3
# b=4
# def soma(x,y):
#      c=a+b
#      print(c)


# def multiplicacao (d,f):
#      c=a*b
#      print(c)   


# def subtracao (d,f):
#         c=a-b
#         print(c)   


# def divisao (d,f):
#     c=a/b
#     print(c)   

# multiplicacao(a,b)


# a=3
# b=4
# def soma(x,y):
#      c=a+b
#      print(c)   #retona o resultado para usalo novamente como variavel


# def multiplicacao (d,f):
#      c=a*b
#      print(c)
#      return c #retona o resultado para usalo novamente como variavel  


# def subtracao (d,f):
#         c=a-b
#         print(c)   
#         return c #retona o resultado para usalo novamente como variavel


# def divisao (d,f):
#     c=a/b
#     print(c)   #retona o resultado para usalo novamente como variavel





# resultado=multiplicacao(a,b)
# print(resultado)

# Exercícios Função aula 11/06/2025
# 1. Verificação de E-mails Válidos
# Crie uma função que receba um e-mail e verifique se ele contém @ e .com. Caso
# contrário, diga "E-mail inválido".

# email = input("Digite seu E-mail: ")
# caracteres="@" 

# def verificaEmail(texto):
#     if caracteres in email:
#         print("Email registrado")
#     else:
#         print ("Email inválido") 
#         print ("Digite seu e-mail novamente")   

# validar = verificaEmail(email)   
# print("\n")                                 



# 2. Sistema de Ponto
# Use input() para receber os horários de entrada e saída. Calcule as horas
# trabalhadas e diga se bateu a carga horária mínima (8h).

# entra = float (input ("horario de entrada "))
# saida = float (input(" horário de saida "))
  
# def horario (a,b):
#     hor=(a-b)
#     printf("h_trabalhadas")



# 3. Geração de Relatórios
# Crie uma função que receba uma lista de vendas por funcionário e calcule a média
# de vendas. Depois, diga se a média está acima de 1000 (meta atingida) ou não.





# lista =["a","b","c","d"]
# print(lista[3])
# print (dir(lista))


# for a in range(0,101,3):
#     print (a)

# c= 10
# while c>0:
#     print (c)
#     c = c-1    

# e-commerce////////////////////////////////////////////////

# cadastrar

#

    #//////////////////////////////////////////////////////
    # e-commerce

# cadastrar
# def e_commerce():
#     dados = {}
#     print('Cadastre-se: ')
#     email = input('E-mail: ')
#     senha = input('senha: ')

#     dados['e-mail'] = email
#     dados['senha'] = senha

#     # acesso ao sistema

#     print('---' * 20)
#     print('Seja bem vindo(a) ao e-commerce ZZZ')
#     print('Acesse a aplicação')

#     chances = 3

#     carrinho = []
#     meu_total = []
#     lista_prod = ['','pipoca','arroz','milho','quentão']
#     valor_prod = ['',2.0,10.0,20.0,15.50]
#     while chances > 0:
#         email_acesso = input('Digite seu e-mail')
#         senha_acesso = input('Digite sua senha')

#         if email_acesso == dados['e-mail'] and senha_acesso == dados['senha']:
#             print('Sejam bem vindo a sua conta ')
#             acesso  = input('Deseja pedir? s/n')
#             print(lista_prod)
#             # escolher produto
#             while acesso == 's':
#                 pedido = int(input('Digite o ID do produto 1 -2 -3 -4')) 
#                 carrinho.append(lista_prod[pedido])
#                 meu_total .append(valor_prod[pedido])
#                 print(carrinho)
#                 soma =  sum(meu_total)
#                 print('R$',soma)
#                 acesso  = input('Deseja pedir? s/n')
#             else:
#                 print('Obrigado volte sempre')
#                 print('Total  -  R$',soma)
                        
#                 lista_pag = ('','PIX','CC','CD')
#                 print(lista_pag)
#                 forma_pag = int(input('Digite o ID forma de pagamentoId 1 - 2 - 3'))
#                 print(lista_pag[forma_pag])
#             break    
#         else:
#             print('Erro de digitação')
#             chances = chances -1    
#     else:
#         print('Bloqueio de conta ')


# while True:
#       e_commerce()

# V = input("Digite enterpara sair")      


# /////////////////////////////////////////////////////////
# def somar(a,b):
#     return a+b

# def subtar(a,b):
#     return a-b

# def mult(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# def calculadora():
#     n1 = float(input("="))
#     escolha =  input('operação - + | - | * | /')
#     if escolha == '+':
#         n2 = float(input('='))
#         soma = somar(n1,n2)
#         print('=',soma)
#     elif escolha == '-':
#         n2 = float(input('='))
#         sub = subtar(n1,n2)
#         print('=',sub)  
#     elif escolha == '*':
#         n2 = float(input('='))
#         mul = mult(n1,n2)
#         print('=',mul)   
#     elif escolha == '/':
#         n2 = float(input('='))
#         di = div(n1,n2)
#         print('=',di) 
#     else:
#         print('Digite algo válido')       

# while True:                               
#       calculadora()


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# def hora_normal(salario,carga):
#     calculo  = salario/carga
#     return calculo

# def hora_extra(hora_normal):
#     calculo = hora_normal * 1.5
#     return calculo

# def quantas_horas_extras(quantidade, hora_extra):
#     calculo =  quantidade * hora_extra
#     return calculo

# def salario_total(salario, quantidade_extra):
#     calculo =  salario + quantidade_extra
#     return calculo

# def sistema_sal():
#     salario = float(input('Digite seu salario: '))
#     carga = float(input('Digite sua carga: '))
#     hora_colaborador  = hora_normal(salario,carga)
#     print('R$', round(hora_colaborador,2) )
#     hora_extra1 = hora_extra(hora_colaborador)
#     print('R$', round(hora_extra1,2))
#     quantidade_extra = float(input('Horas extras:  '))
#     quantas = quantas_horas_extras(quantidade_extra, hora_extra1)
#     print('R$', round(quantas,2))
#     salario_total_ = salario_total(salario, quantas)
#     print('R$', round(salario_total_,2))

#impar =1,3,5,7,9
#par = 0,2,4,6,8,
#





#def numero():
    #num=float(input("digite 1 numero"))
    #print(num)
    #return
 #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////                
# Definimos um número para testar. Você pode mudar este valor!
# numero = 7

# Usamos a estrutura condicional 'if' e 'else'
# if (numero % 2 == 0):
#     print(f"O número {numero} é PAR.")
# else:
#     print(f"O número {numero} é ÍMPAR.")

# # Você pode testar com outros números:
# numero = 10
# if (numero % 2 == 0):
#     print(f"O número {numero} é PAR.")
# else:
#     print(f"O número {numero} é ÍMPAR.")

# possiveis erros com expcept
# def teste():
#   try:  
    
#     n = int(input('Digite um valor inteiro ' ))
#     n2 = int(input('Digite um valor inteiro ' ))
#     print(n/n2)
#     n3 = int(input('Digite um valor inteiro ' ))
#     s = n + n3
#     print(s)
    
#   except ZeroDivisionError as erro:
#     print(erro )
#   except ValueError as erro:
#     print(erro )   
#   else:
#     print('Isso tb pode ser que carregue...  ' )  

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
# # teste()   

# def teste ():
#     try:

#         a = int(input("digite um numero"))
#         b = int(input("digite 2° mumero"))

#         print (a/b)
#         y = a/b 
#     except ZeroDivisionError as erro:
#      print(erro ) 
#     else:
#       print('Isso tb pode ser que carregue...  ' )
# teste()   

#correção:   
# def teste():
#     try:
#         numero = int(input('Numero: '))
#         print(numero)
#     except TypeError as erro:
#         print(erro) 
#     except ValueError  as erro:
#         print(erro)         
#     else:
#         print('Erro não identificado')
#     finally:
#         print('Fim de carregamento... ')    
# teste()


# numero = int(input('Numero: '))
# print(numero)
#/////////////////////////////////////////////////////////////////////////

# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
   
# def div():
#   try:  
#     n1  =  int(input('Numero 1:'))
#     n2  =  int(input('Numero 1:'))
#     d = n1 / n2
#   except ZeroDivisionError as erro:
#     print('Erro',erro)
#   except ValueError as erro:
#     print(erro)
# #   else:
# #     print('Erro não identificado') 


#   finally:
#    print('fim de carregamento')


# div()
 #////////////////////////////////////////////////
# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o parameter elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista)
# def ativida3():
#    try: 
#     lista = [1,2,3]
#     indice = int(input('indice: '))
#     lista[indice]
#    except IndexError as erro:
#      print(erro)
#    except ValueError as erro:
#      print(erro)
#    else:
#      print(lista[indice])   
#    finally:
#      print('Fim de carregamento...')  


# ativida3()     
# # l = [1,2,3]
# # print(l[5])


#////////////////////////////////////////////////////////////////
#

# estruturas de dados
# variáveis  - listas []-  tuplas ()  
# conjuntos{} -  dicinario {chave: valor}


# nome  =  
# estruturas de fluxo de controle


# if elif else - escolhas
# while for  - loops
# try and except - tratar possiveis erros
    
# nome <condição>



# funções def nome(): momento esta sendo criando
# nome() -  chamando para funcionar
# print() input() 
    

