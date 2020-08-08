#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class TramiteDocumentario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.errors = []

    def test_tramite_registro_clasificado(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        usr = driver.find_element_by_id("uname").send_keys("Andre")
        pss = driver.find_element_by_id("psw").send_keys("Andre12345")
        login = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div/button").click()
        time.sleep(2)
        tipo = driver.find_element_by_xpath("//*[@id='clasificacion_index']/option[2]").click()
        nro_hoja = driver.find_element_by_id("n_hoja_index").send_keys(1)
        fecha_ingreso = driver.find_element_by_id("f_ingreso_index").send_keys("08/06/2020")
        #fecha_salida = driver.find_element_by_id("f_ingreso_index").send_keys("08/06/2020")
        unidad_remitente = driver.find_element_by_id("u_remitente_index").send_keys("Andre")
        remitente = driver.find_element_by_id("remitente_index").send_keys("Andre")
        area_destino = driver.find_element_by_id("a_destino_index").send_keys("Andre")
        unidad_destino = driver.find_element_by_id("u_destino_index").send_keys("Andre")
        encargado = driver.find_element_by_id("encargado_index").send_keys("Andre")
        doc_salida = driver.find_element_by_id("d_salida_index").send_keys("08/06/2020")
        tipo_doc = driver.find_element_by_xpath("//*[@id='Form_add_registro']/div[5]/div[1]/select/option[3]").click()
        unidad_destino2 = driver.find_element_by_id("u_destino_2").send_keys("asdsa")
        encargado2 = driver.find_element_by_id("encargado_2").send_keys("Andre")
        asunto = driver.find_element_by_id("t_asunto").send_keys("sadasdsadasd")
        #obs = driver.find_element_by_id("t_observaciones").send_keys("sadasdsadasd")
        time.sleep(1)
        registrar = driver.find_element_by_xpath("//*[@id='Form_add_registro']/div[7]/button").click()

        time.sleep(1)

    def test_tramite_registro_comun(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        usr = driver.find_element_by_id("uname").send_keys("Andre")
        pss = driver.find_element_by_id("psw").send_keys("Andre12345")
        login = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div/button").click()
        time.sleep(2)
        tipo = driver.find_element_by_xpath("//*[@id='clasificacion_index']/option[2]").click()
        nro_hoja = driver.find_element_by_id("n_hoja_index").send_keys(1)
        fecha_ingreso = driver.find_element_by_id("f_ingreso_index").send_keys("08/06/2020")
        #fecha_salida = driver.find_element_by_id("f_ingreso_index").send_keys("08/06/2020")
        unidad_remitente = driver.find_element_by_id("u_remitente_index").send_keys("Andre")
        remitente = driver.find_element_by_id("remitente_index").send_keys("Andre")
        area_destino = driver.find_element_by_id("a_destino_index").send_keys("Andre")
        unidad_destino = driver.find_element_by_id("u_destino_index").send_keys("Andre")
        encargado = driver.find_element_by_id("encargado_index").send_keys("Andre")
        doc_salida = driver.find_element_by_id("d_salida_index").send_keys("08/06/2020")
        tipo_doc = driver.find_element_by_xpath("//*[@id='Form_add_registro']/div[5]/div[1]/select/option[3]").click()
        unidad_destino2 = driver.find_element_by_id("u_destino_2").send_keys("asdsa")
        encargado2 = driver.find_element_by_id("encargado_2").send_keys("Andre")
        asunto = driver.find_element_by_id("t_asunto").send_keys("sadasdsadasd")
        #obs = driver.find_element_by_id("t_observaciones").send_keys("sadasdsadasd")
        time.sleep(1)
        registrar = driver.find_element_by_xpath("//*[@id='Form_add_registro']/div[7]/button").click()



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
