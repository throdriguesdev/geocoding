Data Science: Automação de Consultas e Geocodificação 🌐
Descrição do Projeto
Este repositório contém um aplicativo Python desenvolvido para automatizar consultas e registros de CNPJ, além de implementar a geocodificação de endereços utilizando as APIs do Google (Geocoding e Address Validation). O objetivo é transformar dados brutos em informações visualmente representativas, permitindo uma análise eficiente e a criação de mapas interativos no PowerBI.

Funcionalidades
Automatização de Consultas de CNPJ: O aplicativo facilita a obtenção de informações de CNPJ, permitindo a extração e registro de dados de mais de 9 mil CNPJs de forma eficiente.

Geocodificação de Endereços: Utilizando as APIs do Google, o projeto transforma dados de endereço em coordenadas geográficas, possibilitando uma visualização precisa em mapas no PowerBI.

Integração com o PowerBI: Os dados processados podem ser facilmente visualizados e explorados no PowerBI, proporcionando uma representação visual eficaz das informações geográficas.

Bibliotecas Utilizadas
Pandas: Utilizada para a manipulação e organização eficiente dos dados extraídos.

Requests: Utilizada para realizar as requisições às APIs do Google.

Google Geocoding API e Address Validation API: Implementadas para a geocodificação dos endereços.

Dados Estatísticos das Consultas
Total de Consultas: 9000+
Erros Diretos: 0 (Situações em que a API não conseguiu localizar o endereço)
Erros de Coordenadas: 1 (Coordenada incompatível com o endereço)


Como Usar
Clone este repositório em sua máquina local.


Copy code
git clone https://github.com/throdriguesdev/geocoding.git
Instale as bibliotecas necessárias.

Copy code
pip install -r requirements.txt
Execute o aplicativo.


Copy code
python main.py
Explore os resultados e visualize os dados no PowerBI.
