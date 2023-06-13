import configparser
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

# Constantes para acesso ao sistema
URL_INLOG = 'http://marquise.inlog.com.br:8092/Coleta/Apresentacao/Account/Login/'
parser = configparser.ConfigParser()
parser.read('pipeline.conf')
USERNAME = parser.get('access_credentials_inlog', 'username')
PASSWORD = parser.get('access_credentials_inlog', 'password')

# Abrindo a página do sistema
browser = Firefox()
browser.get(URL_INLOG)

# Preenchendo os campos de login
browser.find_element(By.CLASS_NAME, 'input-text').send_keys(USERNAME)
browser.find_element(By.ID, 'senha').send_keys(PASSWORD)

# Clicando no botão Entrar
browser.find_element(By.ID, 'entrar').click()
