
arquivo_entrada = 'dados.txt'


arquivo_saida = 'dados_formatados.txt'


with open(arquivo_entrada, 'r', encoding='utf-8') as f:
    linhas = f.readlines()


linhas_formatadas = ['"{0}",\n'.format(linha.strip()) for linha in linhas]


with open(arquivo_saida, 'w', encoding='utf-8') as f:
    f.writelines(linhas_formatadas)

print(f"Linhas formatadas foram salvas em {arquivo_saida}")
