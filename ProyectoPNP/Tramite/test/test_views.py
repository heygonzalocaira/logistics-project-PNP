from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.test import TestCase, Client

class testViews(TestCase):

    def test_login_user(self):
        c=Client()
        response = c.get(reverse('login_user'))
        #respuesta de 200 indica que la respuesta esta ok
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'vistas/login.html')

    def test_index_tramite(self):
        c=Client()
        response = c.get(reverse('logout_user'))
        #dado que el usuario debe estar logeo para deslogearse no bota con un valor !=200
        self.assertEquals(response.status_code,302)
