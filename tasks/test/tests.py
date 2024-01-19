from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pytest
import os

# Test para la vista de Tareas
# Comprobamos si la vista task_detail carga la tarea correcta


class TestTareas(TestCase, LiveServerTestCase):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    title = driver.title

    def setUp(self):
        # Iniciamos el navegador y configuramos
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        self.driver.get('http://127.0.0.1:8000/signin/')

    def tearDown(self) -> None:
        return super().tearDown()

    def test_form(self):
        # Iniciamos sesion con el selenium
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'id_username'))).send_keys('admin')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'id_password'))).send_keys('123')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/form/button'))).click()
        # Vamos a la vista de tareas
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/ul/li[1]/a'))).click()
        # Extraemos el input de la vista de la tarea
        input_titulo = self.driver.find_element(by=By.ID, value='id_title')
        # Guardamos el contenido del input en una variable
        resultado = input_titulo.get_attribute('value')
        # Comprobamos si el contenido del input es el esperado
        self.assertEqual(resultado, 'Tarea')


if __name__ == '__main__':
    # Ejecutar las pruebas
    unittest.main()
