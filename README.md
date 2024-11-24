# Contexto
Esse é um exercicio da disciplina INF332 (Arquitetura Orientada a Serviços - SOA & WebServices: Conceitos e Práticas) do curso de engenharia de software da Unicamp turma de 2024

Integrantes :
- [Douglas Sermarini](www.github.com/Douglas019BR)
- Gabriel
- Vitor gomes
- Joiseto
- Stephenson

# Enunciado

## Contexto
Loja virtual com milhares de produtos e milhões de consumidores
Muitas empresas externas procuram para fazer parcerias de negócio mas o modelo aplicado dificulta o fechamento de contratos
Dominou por muito tempo o mercado e agora está perdendo espaço para os concorrentes pois não tem suporte adequado para fomentar parcerias digitais
## Gaps levantados
Poucas APIs
APIs existentes difíceis de serem consumidas (design ruim)
Pouco engajamento com a comunidade de desenvolvedores
Portal de developers inesistente
Modelo comercial de parceria antigo e não aderente a estratégias digitais
## Ações
e-Commerce Compra Fácil lança ações de marketing no mercado com a promessa de ser o melhor parceiro por meio de APIs em um futuro breve
Contratação de empresas especializadas em relacionamento com desenvolvedores (aqui discute-se benefícios, participação em eventos, parceria com a comunidade, etc)
Contratação de empresas especializadas no desenvolvimento de portais de developers
Time focado em reformular o modelo comercial de parcerias para aderir às necessidades digitais
## Principais parcerias discutidas
Buscadores que comparam preços
Apps de alertas de descontos
Redes de afiliados para revenda de produtos (e-Commerce Compra Fácil) em promoções
Sites de tendências de consumo interessados nas listas dos artigos mais vendidos em diversas categorias
## Disponibilizar através de APIs para parceiros
Recurso relacionado a PRODUTOS para:
-   facilitar a busca por:
    -   nome e categoria do produto
    -   faixa de preço
    -   produtos com descontos
-   facilitar a ordenação por:
    -   menor e maior preço
    -   produtos mais vendidos
    -   produtos em lançamento
## Disponibilizar através de APIs para parceiros
-   Recurso relacionado a AFILIADOS para:
    -   criação
    -   edição 
    -   exclusão
    -   listagem por identificador e outros filtros


# Como usar
```sh
    pip install -r requirements.txt
```

```sh
    python swagger-yaml--to-html.py < open_api.yaml > index.html
```

