#!/usr/bin/env python
# coding: utf-8

# ### 01 - Teste de gravidez
# Escreva uma célula com controle de fluxos que tem como premissa a existência das seguintes variáveis:
# 
# - ```sexo``` como ```str``` indicando os valores '**M**' para masculino e '**F**' para feminino  
# - ```beta_hcg``` que indica a quantidade do beta-HCG no sangue em mUI/mL.
# 
# A sua tarefa é escrever um código que imprima como resultado "indivíduo do sexo masculino" quando sexo = 'M', caso sexo = 'F', se o valor de beta-HCG for maior que 5, retorne "Positivo" indicando que a paciente está grávida, e retorne "Negativo" caso contrário.
# 
# Não mexa nos valores da variável ```sexo``` nem em ```beta_hcg```, e escreva um código que funcione para quaisquer valores possíveis de ambos: ```sexo``` = '**M**' ou '**F**' e ```beta_hcg``` assumindo valores inteiros positivos.

# In[13]:


sexo = 'F'
beta_hcg = 5

# seu código vem abaixo desta linha
if sexo=='M':
    print("indivíduo do sexo masculino")
elif((sexo=='F') and (beta_hcg>5)):
    print('Positivo')
else:
    print('Negativo')


# In[10]:


# seu código vem abaixo desta linha
sexo = str(input('Informe o sexo: '))
beta_hcg = int(input('Valor do BetaHCG: '))
if sexo=='M':
    print("indivíduo do sexo masculino")
elif((sexo=='F') and (beta_hcg>5)):
    print('Positivo')
else:
    print('Negativo')


# ### 02 - Renomeando variáveis
# 
# Vamos ver adiante que uma forma de renomear variáveis de um conjunto de dados é através de dicionários - o dicionário deve conter como chave o nome original, associando a cada chave um único valor (tipo *str*) que contenha o nome novo.
# 
# A sua tarefa é escrever um dicionário que possa ser utilizado para traduzir as variáveis ```name``` (nome), ```age``` (idade) e ```income``` (renda). Ou seja, esse dicionário deve relacionar as chaves *name, age* e *income* às suas respectivas traduções.

# In[15]:


dic_renomeacao = {'': ''}
dic_renomeacao


# In[16]:


dic_renomeacao = {'name': 'nome','age':'idade','income':'renda'}
dic_renomeacao


# ### 03 - É divisível?
# A sua tarefa é escrever um código que indique se um número ```N``` é divisível por um número P. Escreva um programa que faça essa verificação para quaisquer combinações de ```N``` e ```M``` e devolva uma mensagem indicativa no output.

# In[18]:


N = 42
M = 7
#Seu código
N = int(input('informe o numerador: '))
M = int(input('informe o divisor: '))        
if N % M == 0:
    print ('Divisível')
else:
    print('Não divisível')


# ### 04 - Números primos
# > Um número **N** é primo se e somente se é divisível por 1, -1, por **N** e por -**N**.  
# 
# Escreva um script que verifica se ```N``` é um número primo, verificando se ```N``` é divisível por todos os números de ```1``` a ```N-1```. Você vai precisar usar alguma ferramenta de *loop* que você aprendeu para isto. No final, devolva uma mensagem no output indicando se o número é primo ou não.

# In[23]:


n=98
primos=[]
for value in range(1,n):
    if n % value == 0:
        primos.append(value)        
if len(primos)==1:
    print(f"{n} é um número primo")
else:
    print(f"{n} não é um número primo, pois também pode ser dividido por ") 
    print(primos)


# In[154]:


N = 30
primos=[]
for i in range(2, N):
    primo = True
    for j in range(2, i // 2 + 1): # só preciso ir até a metade do número
        if i % j == 0:
            primo = False
            
    if primo:
        print(f"{i} é um número primo")  
    


# In[37]:


N = 30
primos=[]
for i in range(2, N):
    primo = True
    for j in range(2, i // 2 + 1): # só preciso ir até a metade do número
        if i % j == 0:
            primo = False
            
    if primo:
        primos.append(i)
print(primos)
        
   


# ### 05 - Desafio
# O algorítmo do exercício anterior não é o mais eficiente. O que você pode fazer para deixá-lo mais eficiente? Ou seja, executar menos comparações, portanto consumir menos tempo.
# 1. Será que precisamos correr o loop até o final sempre?
# 2. Será que precisamos mesmo verificar **todos** os números?
# 3. Será que precisamos ir até N-1?
# 
# Essas perguntas levam ao tipo de pensamento voltado a deixar um algoritmo mais eficiente. Veja se você consegue melhorar o seu.

# In[155]:


N = 98

# seu código aqui
primos=[]
for x in range(1,N+1):
    cont=0
    for y in range(1,x+1):
        if x%y==0:
            cont+=1
    if cont<=2:
        primos.append(x)
print(primos)  


# ### 06 - Peso ideal 1
# O IMC (índice de massa corpórea) é um indicador de saúde mais bem aceito que o peso. Ele é calculado como:
# 
# $$ IMC = \dfrac{peso}{altura^2}$$
# 
# Segundo a OMS, valores *normais* são entre 18.5 e 24.9.
# 
# Sua tarefa é encontrar o ponto médio dessa faixa.

# In[74]:


imc_ideal = (18.5 + 24.9) / 2
imc_ideal


# ### 07 - Peso ideal 2
# Recebendo um valor de altura, encontre o peso '*ideal*' dessa pessoa, que fornece o IMC encontrado acima

# In[76]:


altura = 1.70

# Seu código
peso_ideal = round(imc_ideal*(altura**2),2)
peso_ideal


# ### 08 - Peso ideal 3
# Dada uma lista contendo as alturas de pacientes, crie uma nova lista que contenha o peso '*ideal*' (que fornece o IMC calculado em **Peso ideal 1**) desses pacientes.

# In[77]:


lista_alturas = [1.95, 2.05, 1.70, 1.65]

lista_peso_ideal = []


# seu código
for p in lista_alturas:
    p_ideal=round(imc_ideal*(p**2),2)
    lista_peso_ideal.append(p_ideal)
print(lista_peso_ideal)
   


# ### 09 - Peso ideal 4
# Dada uma lista de tuplas - cada elemento da lista é uma tupla contendo altura e peso de um paciente - crie uma nova lista com o IMC desses pacientes.

# In[78]:


altura_peso = [(1.80, 90), (1.65, 75), (1.91, 70)]
p1 = list(altura_peso[0])
p2 = list(altura_peso[1])
p3 = list(altura_peso[2])

pacientes = []
for p in p1:
    round(p1[1]/(p1[0]**2),2)
#    pacientes.append(p1)
print(pacientes)


# In[ ]:


print(type(pacientes)) # 'list' 
print(pacientes)
pacientes[0]


# ### 10 - Peso ideal 5
# Dada uma lista de **listas** - cada elemento da lista é uma **lista** contendo altura e peso de um paciente, adicione mais um elemento à lista de cada paciente contendo o IMC do paciente. Verifique também se é 'baixo', 'normal' ou 'alto' segundo os padrões da OMS em que normal é entre 18.5 e 24.9.
# 
# Reflexão: por que no problema anterior temos que criar uma nova lista, e não podemos adicionar os dados de cada indivíduo à tupla?

# In[79]:


altura_peso = [[1.80, 90], [1.65, 75], [1.91, 70]]

# seu código

altura_peso


# In[85]:


a,b,c = altura_peso


# In[40]:


altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2
 
print("Seu IMC é: %.2f" % imc)
 
if imc < 18.5:
	print("Abaixo do peso normal")
elif imc < 24.9:
	print("Peso normal")
elif imc < 29.9:
	print("Excesso de peso")
elif imc < 34.9:
	print("Obesidade classe I")
elif imc < 39.9:
	print("Obesidade classe II")
elif imc > 40:
	print("Obesidade Classe III")
#else:
#	print("Obesidade Grau III (mórbida)")

