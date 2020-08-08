#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class EliminarUsuario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_verificar_usuario(self):
        global eliminar
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
        time.sleep(2)

        error = eliminar = driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[2]/th/a").text

        self.assertNotEqual(error,"Pepito","No se encontro usuario")

        time.sleep(3)

    def test_eliminar_usuario(self):
        global eliminar
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
        time.sleep(2)

        error = driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[2]/th/a").click()
        eliminar = driver.find_element_by_xpath("//*[@id='user_form']/div/div/div[1]/div/div/a").click()
        eliminar = driver.find_element_by_xpath("//*[@id='content-main']/div/div/div/div/form/div/button").click()
        time.sleep(3)

        error_m = driver.find_element_by_xpath("// *[ @ id = 'toast-container'] / div").text
        self.assertEqual(error_m,"Se eliminó con éxito usuario \"Pepito\".","Se elimino al usuario")

        #self.assertNotEqual(error,"Pepito","No se encontro usuario")

        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
