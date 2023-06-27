import configparser
from time import sleep
from selenium.webdriver import Firefox
import utils.current_month as current_month
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constantes para acesso ao sistema
URL_INLOG = 'http://marquise.inlog.com.br:8092/Coleta/Apresentacao/Account/Login/'
PARSER = configparser.ConfigParser()
PARSER.read('pipeline.conf')
USERNAME = PARSER.get('access_credentials_inlog', 'username')
PASSWORD = PARSER.get('access_credentials_inlog', 'password')
TOKEN_DASHBOARD = PARSER.get('access_credentials_inlog', 'token')
MES_ATUAL = current_month.get_current_month()
                      
# Abrindo a página do sistema
browser = Firefox()
browser.get(URL_INLOG)

# Preenchendo os campos de login
browser.find_element(By.CLASS_NAME, 'input-text').send_keys(USERNAME)
browser.find_element(By.ID, 'senha').send_keys(PASSWORD)

# Clicando no botão Entrar
browser.find_element(By.ID, 'entrar').click()

# Acessando "Dashboard"
# Refatoração necessária: garantir o acesso sem um tempo de espera e adquirindo a URL diretamente da tag HTML
sleep(6)
browser.get('http://marquise.inlog.com.br:8092/dashboard//Account/Login?token='+TOKEN_DASHBOARD)

# Clicando na aba "Relatórios"
browser.find_element(By.ID, 'abaReportsList').click()

# Selecionando relatório "Contestação Analitico Prefeitura"
browser.find_element(By.CSS_SELECTOR, 'span.title').click()

# Selecionando o período
#sleep(6)
#browser.find_element(By.ID, 'dataInicio').click()



