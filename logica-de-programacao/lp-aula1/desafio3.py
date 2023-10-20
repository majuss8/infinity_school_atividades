tamanhoArquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidadeLink = float(input('Informe a velocidade do link em Mbps: '))
tempoDownloadEmSegs = tamanhoArquivo * velocidadeLink
tempoDownloadEmMins = tempoDownloadEmSegs / 60
print(f'O tempo aproximado de download do arquivo usando esse link será de: {tempoDownloadEmMins:,.1f} minuto(s)')
