import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
from alertaemail import send_mail

load_dotenv()

# Parametros padrões para uso no código.
default = ("00428963 _SA_ 1ª VIA - HISTÓRICO ESCOLAR DIGITAL DE CONCLUSÃO: PÓS-GRADUAÇÃO CIÊNCIAS DE DADOS E "
           "INTELIGÊNCIA ARTIFICIAL Fechado 19/02/2024 Taxa de solicitação deste serviço isenta")
uninter_login = os.getenv("UNINTER_LOGIN")
uninter_password = os.getenv("UNINTER_PASSWORD")
url = "https://solicitacaoservico.uninter.com"

# Configurações iniciais
options = Options()
options.add_argument("--headless=new")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
driver.get(url)


driver.implicitly_wait(5)

form_login = driver.find_element(By.ID, "formLogin")

login = form_login.find_element(By.ID, "userName")
password = form_login.find_element(By.ID, "senha")
submit_button = form_login.find_element(By.ID, "Login")

login.send_keys(uninter_login)
password.send_keys(uninter_password)
time.sleep(2)
submit_button.click()

time.sleep(2)

btn_service = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div/div/div/div[1]/div[1]/div[1]/div/button")
btn_service.click()

time.sleep(2)

list_services = driver.find_element(By.ID, "webGridDivFeaturesPermission")

padrao = list_services.find_element(By.TAG_NAME, "tbody")

time.sleep(2)

novo_default = padrao.find_element(By.TAG_NAME, "tr")

if novo_default.text != default:
    send_mail()
else:
    print("Nenhuma alteração encontrada")

driver.quit()
