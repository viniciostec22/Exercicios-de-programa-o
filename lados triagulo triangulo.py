#Faça um programa que receba três valores X, Y e Z e verifique se eles podem ser os
#comprimentos dos lados de um triângulo e, se forem, verifique se é um triângulo
#equilátero, isósceles ou escaleno. Escreva uma mensagem informando o tipo de
#triângulo ou se não forma um triângulo. Considere as regras:
#a. O comprimento de cada lado de um triângulo é menor que a soma dos outros
#dois lados;
#b. Equilátero é o triângulo com três lados iguais
#c. Isósceles é o triângulo com apenas dois lados iguais
#d. Escaleno é o triângulo com três lados diferentes

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor valor: '))
c = float(input('Digite o terceiro valor: '))

if(a + b > c and  a + c > b and b + c > a):
  if(a == b and a == c):
    print('Forma um triangulo Equilatero')
  elif(a == b or a == c or b == c):
    print('Forma um triangulo Isósceles ')
  else:
    print('Forma um triangulo escaleno')  
else:
  print('Não forma um triangulo')