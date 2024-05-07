import requests
import json

def calculo_milhas (fatura, cotacao_dolar, ponto_cartao):
  milhas = (fatura / cotacao_dolar) * ponto_cartao
  return milhas


def main():
  print("Olá, seja bem vindo ao nosso sistema de calculo de milhas!")
  print("Para começar vamos precisar das seguintes informações: Valor da sua fatura do cartão de crédito e a pontuação de milhas do seu cartão.")
  fatura = float(input("Digite o valor da sua fatura: "))
  ponto_cartao = float(input("Digite a pontuação de milhas do seu cartão: "))
  cotacao_dolar = dolar()
  minhas_milhas = calculo_milhas(fatura, cotacao_dolar, ponto_cartao)
  minhas_milhas_formatada = "{:.2f}".format(minhas_milhas)
  print("O valor de milhas que você tem é: ",  minhas_milhas_formatada)

def dolar():
  cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
  cotacoes = cotacoes.json()
  cotacao_dolar = cotacoes['USDBRL']["bid"]
  return float(cotacao_dolar)
 
  

main ()
  
  
  
  