# -*- coding: utf-8 *-*
'''
Created on 02/06/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import pygame
# -----------
# Constantes
# -----------
apagarW = "shutdown /s /f /t 01"
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import os
import sys
import ConfigView
import Usercontroller
import Admincontroller
import DBcontroller
import Modcontroller
import Apagarcontroller
# ------------------------------
# Funcion principal del Programa
""" Controlador de la Interfaz del Usuario"""
# ------------------------------


class controlador:
    def __init__(self,sistemaop):
        # Guardamos el SO
        self.sistemaop = sistemaop    
                
        # Instancia para la VISTA
        self.vista = ConfigView.ConfigView(sistemaop)

        # Instancia de los Controladores de cada SubVista
        self.user_controller = Usercontroller.UserController(self.sistemaop)
        self.admin_controller = Admincontroller.AdminController(self.sistemaop)
        self.db_controller = DBcontroller.DBController(self.sistemaop)
        self.mod_controller = Modcontroller.ModController(self.sistemaop)
        self.apagar_controller = Apagarcontroller.ApagarController(self.sistemaop)

        # Cargamos todo lo relacionado a pygame
        pygame.init() 

    """---------------------------------------Metodos-------------------------------------------------------"""
    def crear_interfaz(self):
        self.vista.crear_interfaz()
        
    def ApagarEquipo(self):
     #   "Click en Boton Apagar Equipo"
        os.system(apagarW)    


    """--------------------------------------Eventos-------------------------------------------------------"""
    def eventos_config(self):
        "Metodo para Los Eventos en la Vista del Usuario"
        access = "Config"
        res = ""
        while True:
            # Empezamos a capturar la lista de Eventos
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Dependiendo de la zona donde se hizo click se realiza una accion 
                    x, y = event.pos
                    if self.vista.super_usuario.collidepoint(x, y):
                        # Click en Boton Config. Super Usuario
                        self.user_controller.crear_interfaz()
                        self.user_controller.eventos_config()
                        self.crear_interfaz()

                    elif self.vista.admin.collidepoint(x, y):
                        # Click en Boton Config. Admin
                        self.admin_controller.crear_interfaz()
                        self.admin_controller.eventos_config()
                        self.crear_interfaz()

                    elif self.vista.bd.collidepoint(x, y):
                        # Click en Boton Config. BD
                        self.db_controller.crear_interfaz()
                        self.db_controller.eventos_config()
                        self.crear_interfaz()

                    elif self.vista.mod.collidepoint(x, y):
                        # Click en Boton Config. Modulo
                        self.mod_controller.crear_interfaz()
                        self.mod_controller.eventos_config()
                        self.crear_interfaz()
                        
                    elif self.vista.Apagar.collidepoint(x, y):
                        # Click en Boton Config. Modulo
                        self.ApagarEquipo()
                        
                    elif self.vista.apagar.collidepoint(x, y):
                        # Click en Boton Config. Modulo
                        self.apagar_controller.crear_interfaz()
                        self.apagar_controller.eventos_config()
                        self.crear_interfaz()

                    elif self.vista.salir.collidepoint(x, y):
                        # Click en Boton Cerrar Sesion
                        access = "Login"
                        return access
            self.vista.surface()
            self.vista.refresh_display()