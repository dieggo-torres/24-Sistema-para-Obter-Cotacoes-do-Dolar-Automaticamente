# Importação da biblioteca os
import os

# Importação da biblioteca dotenv
from dotenv import load_dotenv

# Importação de métodos da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Importação da biblioteca time
import time

# Carrega as variáveis de ambiente
load_dotenv()

# Obtenção das credenciais
nome_usuario = os.getenv('NOME_USUARIO')
senha = os.getenv('SENHA')

# Cria uma instância do navegador Google Chrome
driver = webdriver.Chrome()

# Acessa o site especificado
driver.get('https://br.investing.com/currencies/usd-brl-historical-data')


def esperar_elemento_aparecer(elemento):
    """Enquanto o elemento não aparece na tela, aguarda 1 segundo."""

    while len(elemento) == 0:
        time.sleep(1)


# Espera o botão dos termos de privacidade do site aparecer na tela antes de clicar
botao_aceitar = driver.find_elements(By.ID, 'onetrust-accept-btn-handler')
esperar_elemento_aparecer(botao_aceitar)

# Espera 1s antes de clicar no botão
time.sleep(1)

# Clica no botão para aceitar os termos de privacidade
botao_aceitar[0].click()

# Clicar no botão para baixar a planilha
botao_baixar_dados = driver.find_element(
    By.CSS_SELECTOR, '#column-content div a')
botao_baixar_dados.click()

# Preencher campos do formulário de login
# E-mail
campo_email = driver.find_elements(By.ID, 'loginFormUser_email')
esperar_elemento_aparecer(campo_email)
time.sleep(1)
campo_email[0].send_keys(nome_usuario)

# Senha
campo_senha = driver.find_element(By.ID, 'loginForm_password')
campo_senha.send_keys(senha)

# Enviar formulário
driver.find_element(By.CSS_SELECTOR, '#loginPopup a.orange.newButton').click()

# Clica novamente no botão para baixar a planilha
botao_baixar_dados = driver.find_element(
    By.CSS_SELECTOR, '#column-content div a')
botao_baixar_dados.click()
