import requests
import json
import os

# URL da API que retorna os dados
url = "http://127.0.0.1:8000/gerar_compras/10"  # alterar para a quantidade desejada de requisições

# Fazendo a requisição GET para pegar os dados
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Convertendo a resposta em JSON

    # Definindo o nome do arquivo JSON
    json_filename = './data/compras.json'

    # Criando o diretório caso ele não exista
    os.makedirs(os.path.dirname(json_filename), exist_ok=True)

    # Salvando os dados no arquivo JSON
    with open(json_filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Dados salvos no arquivo {json_filename} com sucesso!")

else:
    print(f"Erro ao obter os dados: {response.status_code}")
