from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.test import TestCase, Client

class testViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login = reverse('login_user')
        self.logout = reverse('logout_user')

    def test_login_user(self):
        response = self.client.get(self.login)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'vistas/login.html')

    def test_index_tramite(self):
        response = self.client.get(self.logout)
        self.assertEquals(response.status_code,302)
