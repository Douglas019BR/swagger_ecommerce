
[Swagger e-commerce](https://douglas019br.github.io/swagger_ecommerce/)

# Contexto
Esse é um exercício da disciplina INF332 (Arquitetura Orientada a Serviços - SOA & WebServices: Conceitos e Práticas) do curso de Engenharia de Software da Unicamp, turma de 2024.

Integrantes:
- [Douglas Sermarini](https://www.github.com/Douglas019BR)
- [Gabriel](https://www.github.com/gcesario203)
- [Vitor Gomes](https://www.github.com/vitorgomes)
- [Joiseto](https://www.github.com/JoseitoOliveira)
- [Stephenson](https://www.github.com/stephensonsn)

# Enunciado

## Contexto
Loja virtual com milhares de produtos e milhões de consumidores. 
Muitas empresas externas procuram por parcerias de negócio, mas o modelo atual dificulta o fechamento de contratos. 
Dominou por muito tempo o mercado e agora está perdendo espaço para os concorrentes, pois não tem suporte adequado para fomentar parcerias digitais.

## Gaps levantados
- Poucas APIs disponíveis
- APIs existentes com design ruim e difíceis de serem consumidas
- Pouco engajamento com a comunidade de desenvolvedores
- Portal de desenvolvedores inexistente
- Modelo comercial de parceria antigo e não aderente a estratégias digitais

## Ações
- Lançamento de ações de marketing prometendo ser o melhor parceiro por meio de APIs em um futuro breve
- Contratação de empresas especializadas em relacionamento com desenvolvedores (benefícios, eventos, parcerias, etc.)
- Contratação de empresas especializadas no desenvolvimento de portais para desenvolvedores
- Formação de um time focado em reformular o modelo comercial de parcerias para aderir às necessidades digitais

## Principais parcerias discutidas
- Buscadores que comparam preços
- Aplicativos de alertas de descontos
- Redes de afiliados para revenda de produtos em promoções
- Sites de tendências de consumo interessados nas listas dos artigos mais vendidos em diversas categorias

## Recursos disponibilizados por meio de APIs
### Relacionados a PRODUTOS:
- Facilitar a busca por:
    - Nome e categoria do produto
    - Faixa de preço
    - Produtos com descontos
- Facilitar a ordenação por:
    - Menor e maior preço
    - Produtos mais vendidos
    - Produtos em lançamento

### Relacionados a AFILIADOS:
- Criação
- Edição
- Exclusão
- Listagem por identificador e outros filtros

# Como usar

1. **Crie e ative o ambiente virtual:**

    No Windows:
    ```sh
    python -m venv env
    .\env\Scripts\activate
    ```

    No Linux/MacOS:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

2. **Instale as dependências:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Gere a documentação HTML a partir do arquivo YAML:**

    ```sh
    python swagger-yaml-to-html.py < open_api.yaml > index.html
    ```

4. **Abra o arquivo HTML gerado no navegador:**

    ```sh
    start index.html  # Para Windows
    open index.html   # Para MacOS
    xdg-open index.html  # Para Linux
    ```