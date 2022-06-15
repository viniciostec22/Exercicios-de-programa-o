#Faça um programa que receba o salário de um funcionário e o percentual de aumento.
#Calcule e mostre o novo salário e o valor de aumento.

salario = float(input('Digite o vslor do salario: R$'))
aumento = float(input('Digite o percentual do aumento em % '))

novo_salario = salario + (salario * aumento / 100)
print('Seu novo salario é R${:.2f} '.format(novo_salario)) 
print('O funcionario teve um aumento de R${:.2f}'.format(novo_salario - salario)) 