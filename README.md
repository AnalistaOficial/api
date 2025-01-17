<h1 align="center">Projeto API</h1>

### Objetivo

O objetivo do projeto é criar uma API robusta, com foco na criação de endpoints que permitam a manipulação e o consumo de dados de forma eficiente. A API será projetada para fornecer funcionalidades específicas, permitindo que os dados sejam acessados, alterados e consumidos por sistemas externos de maneira fluida e segura. O projeto está utilizando a FastAPI do Python para a criação da API e, para testar suas funcionalidades, está gerando dados fake. Esses dados simulados serão apresentados pela API, permitindo a validação e o exercício dos endpoints criados, garantindo que a comunicação entre os componentes e o consumo de dados ocorram de maneira eficaz e segura.

![](https://dkrn4sk0rn31v.cloudfront.net/uploads/2020/11/consumindo-api-python.png)

### Amostar dos dados

[
  {
    "client": "Lisa Collins",
    "creditcard": "VISA 16 digit",
    "product": "Up",
    "ean": 8245789631456,
    "price": 14.84,
    "clientPosition": [
      "36.02506",
      "-86.77917",
      "Brentwood Estates",
      "US",
      "America/Chicago"
    ],
    "store": 11,
    "dateTime": "2015-04-07T19:33:05"
  }
]


### Dependências
                
                * Pandas 2.2.3
                * Faker 33.3.1
                * Fastapi 0.115.6
                * Requests 2.32.3