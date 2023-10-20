valorHora = float(input('Valor da hora trabalhada: '))
horaPorMes = float(input('Número de horas trabalhadas no mês: '))
salarioBruto = valorHora * horaPorMes
impostoDeRenda = 0.11 * salarioBruto
inss = 0.08 * salarioBruto
sindicato = 0.05 * salarioBruto
descontos = impostoDeRenda + inss + sindicato
salarioLiquido = salarioBruto - descontos
print(f'Salário Bruto: R${salarioBruto:.2f}\nIR (11%): R${impostoDeRenda:.2f}\nINSS (8%): R${inss:.2f}\nSindicato: R${sindicato:.2f}\nDescontos: R${descontos:.2f}\nSalário Líquido: R${salarioLiquido:.2f}')