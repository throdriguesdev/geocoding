import pandas as pd
import requests
chave_api = "XXXXXXXXX"
enderecos = [
    "ST BANCARIO SUL QUADRA 04	34	70.092-900	ASA SUL	BRASILIA	DF",
]
df = pd.DataFrame({'Endereco': enderecos, 'Latitude': None, 'Longitude': None})
def obter_coordenadas(endereco):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={chave_api}"
    resposta = requests.get(url)
    dados = resposta.json()
    if dados["results"]:
        latitude = dados["results"][0]["geometry"]["location"]["lat"]
        longitude = dados["results"][0]["geometry"]["location"]["lng"]
        return latitude, longitude
    else:
        return None, None
for index, row in df.iterrows():
    endereco = row['Endereco']
    latitude, longitude = obter_coordenadas(endereco)
    df.at[index, 'Latitude'] = latitude
    df.at[index, 'Longitude'] = longitude
    
df.to_excel('coordenadas.xlsx', index=False)
print("Coordenadas foram adicionadas ou atualizadas na coordenadas.xlsx")
