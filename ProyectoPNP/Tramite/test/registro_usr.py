#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class AgregarUsuario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_nombre_usuario(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        usr = driver.find_element_by_id("uname").send_keys("Andre")
        pss = driver.find_element_by_id("psw").send_keys("Andre12345")
        time.sleep(2)
        login = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div/button").click()
        driver.get("http://127.0.0.1:8000/admin/")
        time.sleep(2)
        url = driver.find_element_by_xpath("//*[@id='content']/div/div/div[1]/div/div/div[2]/div[2]/a").click()
        add_user = driver.find_element_by_xpath("//*[@id='content-main']/ul/li/div/a").click()
        time.sleep(2)
        usr = driver.find_element_by_id("id_username").send_keys("Pepito~")
        pss2 = driver.find_element_by_id("id_password1").send_keys("hola12345")
        pss2_c = driver.find_element_by_id("id_password2").send_keys("hola12345")

        time.sleep(2)
        guardar = driver.find_element_by_name("_save").click()
        error_m = driver.find_element_by_xpath("//*[@id='user_form']/div/div/fieldset/div[1]/ul").text

        self.assertEqual(error_m, "Introduzca un nombre de usuario válido. Este valor solo puede contener letras, números y los caracteres @/./+/-/_.",
                         "Por favor, vuelva a ingresar un nombre de usuario.")
        time.sleep(3)

    def test_password(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        usr = driver.find_element_by_id("uname").send_keys("Andre")
        pss = driver.find_element_by_id("psw").send_keys("Andre12345")
        time.sleep(2)
        login = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div/button").click()
        driver.get("http://127.0.0.1:8000/admin/")
        time.sleep(2)
        url = driver.find_element_by_xpath("//*[@id='content']/div/div/div[1]/div/div/div[2]/div[2]/a").click()
        add_user = driver.find_element_by_xpath("//*[@id='content-main']/ul/li/div/a").click()
        time.sleep(2)
        usr = driver.find_element_by_id("id_username").send_keys("Pepito")
        pss2 = driver.find_element_by_id("id_password1").send_keys("hola12")
        pss2_c = driver.find_element_by_id("id_password2").send_keys("hola12")

        time.sleep(2)
        guardar = driver.find_element_by_name("_save").click()
        error_m = driver.find_element_by_xpath("//*[@id='user_form']/div/div/fieldset/div[3]/ul/li[1]").text

        self.assertEqual(error_m, "La contraseña es demasiado corta. Debe contener por lo menos 8 caracteres.",
                         "Por favor, vuelva a ingresar una contraseña")
        time.sleep(3)

    def test_coincidencia_pssw(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        usr = driver.find_element_by_id("uname").send_keys("Andre")
        pss = driver.find_element_by_id("psw").send_keys("Andre12345")
        time.sleep(2)
        login = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div/button").click()
        driver.get("http://127.0.0.1:8000/admin/")
        time.sleep(2)
        url = driver.find_element_by_xpath("//*[@id='content']/div/div/div[1]/div/div/div[2]/div[2]/a").click()
        add_user = driver.find_element_by_xpath("//*[@id='content-main']/ul/li/div/a").click()
        time.sleep(2)
        usr = driver.find_element_by_id("id_username").send_keys("Pepito")
        pss2 = driver.find_element_by_id("id_password1").send_keys("hola12345")
        pss2_c = driver.find_element_by_id("id_password2").send_keys("hola122345")

        time.sleep(2)
        guardar = driver.find_element_by_name("_save").click()
        error_m = driver.find_element_by_xpath("//*[@id='user_form']/div/div/fieldset/div[3]/ul/li").text

        self.assertEqual(error_m, "Los dos campos de contraseñas no coinciden entre si.",
                         "Por favor, vuelva a confirmar su contraseña.")
        time.sleep(3)

    def test_registro_exitoso(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        usr = driver.find_element_by_id("uname").send_keys("Andre")
        pss = driver.find_element_by_id("psw").send_keys("Andre12345")
        time.sleep(2)
        login = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div/button").click()
        driver.get("http://127.0.0.1:8000/admin/")
        time.sleep(2)
        url = driver.find_element_by_xpath("//*[@id='content']/div/div/div[1]/div/div/div[2]/div[2]/a").click()
        add_user = driver.find_element_by_xpath("//*[@id='content-main']/ul/li/div/a").click()
        time.sleep(2)
        usr = driver.find_element_by_id("id_username").send_keys("Pepito")
        pss2 = driver.find_element_by_id("id_password1").send_keys("hola12345")
        pss2_c = driver.find_element_by_id("id_password2").send_keys("hola12345")

        time.sleep(2)
        guardar = driver.find_element_by_name("_save").click()
        time.sleep(2)
        error_m = driver.find_element_by_xpath("//*[@id='toast-container']/div").text

        self.assertEqual(error_m, "Se agregó con éxito usuario \"Pepito\". Puede modificarlo/a nuevamente mas abajo.",
                         "No se pudo crear el usuario.")
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/admin/")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
