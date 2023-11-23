import pandas as pd


planilha = pd.read_excel("PLANILHA-FINAL.xlsx")

planilha_filtrada = planilha[~planilha['Situação'].isin(['INAPTA', 'SUSPENSA', 'BAIXADA'])]


planilha_filtrada.to_excel("PLANILHA-FINAL-FILTRADA.xlsx", index=False)
