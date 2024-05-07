def meu_imc (peso, altura):

  imc = peso / (altura * altura)
  return imc

def resultado_imc (imc):

  if imc < 18:
    print("Você está abaixo do peso")
  elif imc < 25:
    print("Você está com o peso normal")
  elif imc < 30:
    print("Você está com sobrepeso")
  else:
    print("Obesidade registrada")

def tmb_homem (peso,altura,idade):

  tmb_h = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
  return tmb_h

def tmb_mulher (peso,altura,idade):

  tmb_m = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
  return tmb_m

def main ():

  print("Olá! Seja bem vindo ao programa de cálculo de IMC e TMB!")
  print("Para começar, precisamos saber qual o seu interesse.")
  print("Por favor, escolha uma das opções abaixo: ")
  escolha = float(input("Escolha 1 para calcular o seu IMC e 2 para calcular o seu TMB: "))

  if escolha == 1:

    print("Você escolheu calcular o seu IMC!")
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = meu_imc(peso, altura)
    resultado_imc(imc)
    print("Seu IMC é: ", imc)

  elif escolha == 2:
    print("Você escolheu calcular o seu TMB!")
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em centímetros: "))
    idade = float(input("Digite sua idade em anos: "))
    sexo = input("Digite seu sexo (H ou M): ")
    if sexo == "H".upper():
      tmb_h = tmb_homem (peso,altura,idade)
      print("Sua Taxa Metabólica Basal é: ", tmb_h)
    elif sexo == "M":
      tmb_m = tmb_mulher (peso,altura,idade)
      print("Sua Taxa Metabólica Basal é: ", tmb_m)
      imc = meu_imc(peso, altura)
      return imc
    else:
      print("Opção incorreta")

  else:
    print("Opção incorreta!")

    
  