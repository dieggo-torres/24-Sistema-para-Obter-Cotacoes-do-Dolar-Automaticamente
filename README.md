# [Avançado] Automação Web: Obtenção de CSV com Cotação Histórica do Dólar (USD-BRL)
Neste projeto, usei a biblioteca __selenium__ para criar uma automação web que acessa o site da [Investing.com](https://br.investing.com/) e que baixa um arquivo CSV
com as cotações do dólar americano. Esse arquivo pode ser baixado nesta [página](https://br.investing.com/currencies/usd-brl-historical-data), clicando no botão __baixar dados__.

Porém, para baixar esse arquivo, é necessário fazer login no site através de um formulário de autenticação. Meus dados de autenticação foram salvos num arquivo _.env_, o qual
foi listado no arquivo _.gitignore._ No arquivo _main.py_, usei a biblioteca __dotenv__ para carregar as variáveis de ambiente e a biblioteca __os__ para acessá-las. Assim,
caso você queira usar este projeto, crie seu próprio arquivo _.env_ e liste suas credenciais lá.


