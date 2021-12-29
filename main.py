import  locale
locale.setlocale(locale.LC_MONETARY,'pt_br')

from mortgage import Loan

from helpers import juros_compostos

if __name__=='__main__':
    quantia_a_emprestar = float(input("Digite um valor a emprestar: "))
    taxa_de_juros_anual = float(input("Digite o valor da taxa de juros anual: "))
    prazo = int(input("Digite o prazo em anos: "))

valor_final_a_pagar = juros_compostos(quantia_a_emprestar,taxa_de_juros_anual,prazo)
print(f"O montante total calculado é: {locale.currency(valor_final_a_pagar,grouping=True)}.")
print()
#Usando Mortgege Loan
financiamento = Loan(quantia_a_emprestar,taxa_de_juros_anual/100,prazo,currency='R$')
print(financiamento.summarize)
