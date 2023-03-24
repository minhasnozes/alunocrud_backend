import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import asyncio


class WebDriver:
    def __init__(self):
        self.executable_path = 'C:\chromedriver_win32\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")

    async def start(self):
        self.driver = webdriver.Chrome(executable_path=self.executable_path, options=self.options)

    async def navigate(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def return_driver(self):
        return self.driver


class BaseForm():

    def __init__(self, driver):
        self.driver = driver

    async def preencher_campo(self, text, locator, locator_str):
        if locator == By.CSS_SELECTOR:
            locator_str = f'input[formControlName="{locator_str}"]'

        field = self.driver.find_element(locator, locator_str)
        field.send_keys(text)

    async def submit(self, time_until=5, link_text=None):
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        try:
            # Espera até 10 segundos pelo elemento "header" da página de destino
            app = WebDriverWait(self.driver, time_until).until(
                EC.presence_of_element_located((By.LINK_TEXT, link_text))
            )
            print(f'{link_text} found!')
        except TimeoutException:
            print(f'{link_text} Not found!')

    async def click(self, locator, locator_str, time_until=5, link_text=None):
        element = self.driver.find_element(locator, locator_str)
        element.click()
        try:
            app = WebDriverWait(self.driver, time_until).until(
                EC.presence_of_element_located((By.LINK_TEXT, link_text))
            )
            print(f'{locator_str} found')
        except TimeoutException:
            print(f'{locator_str} Not found')

    async def login(self, username=None, password=None):
        await self.preencher_campo('admin', By.ID, 'username')
        await self.preencher_campo('admin', By.ID, 'password')
        await self.click(By.ID, 'btnLogin', time_until=2, link_text='page-not-found works!')


async def main():
    # instância do driver
    driver = WebDriver()
    await driver.start()

    # Navega para localhost
    await driver.navigate("http://localhost:4200")

    screen = BaseForm(driver.return_driver())

    # realiza login
    await screen.login('admin', 'admin')

    # Navega para tela de aluno
    await driver.navigate("http://localhost:4200/aluno")

    await cadastrar_aluno(screen, nome='Marcus', sobrenome='Soares', data_nascimento='1993-03-02')
    await cadastrar_aluno(screen, nome='Alexandre', sobrenome='Soares', data_nascimento='1993-03-02')
    await cadastrar_aluno(screen, nome='Luiz', sobrenome='Soares', data_nascimento='1993-03-02')

    driver.quit()


async def cadastrar_aluno(screen, nome=None, sobrenome=None, data_nascimento=None):
    # Clica botão adiciona novo aluno
    await screen.click(By.ID, 'btnAddNovoAluno', time_until=2, link_text='Aluno')
    # Preenche campos novo aluno
    await screen.preencher_campo(nome, By.CSS_SELECTOR, 'nome')
    await screen.preencher_campo(sobrenome, By.CSS_SELECTOR, 'sobrenome')
    await screen.preencher_campo(data_nascimento, By.CSS_SELECTOR, 'data_nascimento')
    await screen.submit(time_until=2, link_text='Listagem de alunos')


if __name__ == '__main__':
    asyncio.run(main())
