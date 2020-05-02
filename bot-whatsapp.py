# GUSTAVO SOARES SILVA [1st may, 2020]

# REFS.:
'''
[1] CARVALHO, Juan. Simple bot whatsapp (Python 3 + Selenium), 2019. Medium.
Disponível em <https://medium.com/@juan.carvalho82/simple-bot-whatsapp-python-3-selenium-4e5bae30ed9a>.
Acesso em 01 maio 2020.

[2] DEV Aprender. COMO CRIAR UM BOT(robô) NO WHATSAPP de Mensagens Dev Aprender. 2019.
(21min26s). Disponível em <https://www.youtube.com/watch?v=ISYHWfWvp3E>. Acesso em 01 maio 2019  

'''

from selenium import webdriver
import time
import os
from random import randint

class chromeBot:

  dir_path = os.getcwd()
  chromedriver = os.path.join(dir_path, "chromedriver.exe")
  profile = os.path.join(dir_path, "profile", "wpp") 

  def __init__(self):
    self.mensagens = ["mensagem", "message"]
    self.grupos = ["nome dos grupos ou contato", "name of groups or contacts"]

    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

  def procurarNome(self, nome):
    try:
      self.driver.find_element_by_xpath("//span[@data-icon='search']").click()
      time.sleep(2)
      label_search = self.driver.find_element_by_xpath("//div[@id='side']/div[1]/div/label/div/div[2]")
      label_search.send_keys(nome)
      time.sleep(2)
    except Exception:
      return False

  def enviaMidia(self, fileToSend):
      try:
        self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
        time.sleep(2)
        attach = self.driver.find_element_by_css_selector("input[type='file']")
        attach.send_keys(fileToSend)
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[contains(@class, 'yavlE')]").click()
      except Exception as e:
        print('Erro ao enviar mídia ', e)

  def enviarMensagens(self):
    # <span dir="auto" title="EU " class="_1wjpf _3NFp9 _3FXB1">EU </span>
    # <div tabindex="-1" class="_1Plpp">
    # <span data-icon="send" class="">

    self.driver.get('https://web.whatsapp.com/')
    
    time.sleep(25)

    # crie uma pasta para adicionar os arquivo que queira enviar (de forma aleatória)
    # create a file to add the archives you want send (randomly)
    pasta = "bom-dia"
    foto = ["msgm1.jpg", "msgm2.jpg", "msgm3.jpg","msgm4.jpg", "msgm5.jpg", "msgm6.gif", "msgm7.gif", "msgm8.gif"]

    for grupo in self.grupos:
      self.procurarNome(grupo)
      time.sleep(2)
      grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
      grupo.click()
      chatBox = self.driver.find_element_by_class_name('_1Plpp')
      time.sleep(2)
      for mensagem in self.mensagens:
        chatBox.click()
        chatBox.send_keys(mensagem)
        botao = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(4)
        botao.click()

        rand = randint(0,len(foto)-1)
        imagem = bot.dir_path + f"\{pasta}\{foto[rand]}"

        self.enviaMidia(imagem)
      time.sleep(1)

bot = chromeBot()
bot.enviarMensagens()
