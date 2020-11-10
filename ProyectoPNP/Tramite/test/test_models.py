from django.test import TestCase
from Tramite.models import MUser, MUserGrado
from django.db import models
from django.contrib.auth.models import User

class testModels(TestCase):

    def setUp(self):
        self.MUserGrado1 = MUserGrado.objects.create(
            Grado = 'grado1',
            Clase = 'clase1'
        )
        self.MUserRol1 = MUserRol.objects.create(
            rol = 'rol1'
        )
        self.MUser1 = MUser.objects.create(
            Nombres='asdasd',
            ApeMaterno='pppppp'
        )
        self.MtipoDocumento1 = MtipoDocumento.objects.create(
            Documento = 'documento1',
            nombre_corto = 'doc1'
        )
        self.MAreaORI1 = MAreaORI,objects.create(
            area = 'area1'
        )

    def test_MUserGrado (self):
        self.assertEquals(self.MUserGrado1,'grado1')


    def test_MUserRol (self):
        self.assertEquals(self.MUserRol1,'grado1')

    def test_MUser(self):
        self.assertEquals(self.MUser1,'asdasd')

    def test_MtipoDocumento(self):
        self.assertEquals(self.MtipoDocumento1,'documento1')

    def test_MAreaORI(self):
        self.assertEquals(self.MAreaORI1,'area1')
