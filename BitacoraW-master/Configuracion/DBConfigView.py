'''
Created on 04/06/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import pygame
from pygame.locals import *
# -----------
# Constantes
# -----------
S_WIDTH = 480
S_HEIGHT = 250
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import Clases.eztext
# ------------------------------
# Descripcion de la Clase
""" Clase para la Interfaz de la Conexion a BD"""
# ------------------------------

class DBConfigView():
    def __init__(self,sistemaop):
        "Definimos los Atributos de la Clase"
        # Guardamos el SO
        self.sistemaop = sistemaop
        
        # Cargamos todo lo relacionado a pygame
        pygame.init()
        
        # Cargamos el Tipo de Fuente a Usar
        self.fuente = pygame.font.SysFont("Arial", 14, bold=True, italic=False)
        
    def crear_interfaz(self):
        self.dimencionar_ventana()
        self.cargar_imagenes()
        self.cargar_textbox()
        self.cargar_botones()

    def cargar_imagenes(self):
        "Metodo para Cargar las Imagenes a la Interfaz"
        # Cargamos el fondo y las imagenes para la Ventana UserView
        if self.sistemaop == "linux2":
            imagenconfig_interface = "/opt/BitacoraL/src/images/root-03.png"
            imagenbGuardar = "/opt/BitacoraL/src/images/Guardar.png"
            imagenbRegresar = "/opt/BitacoraL/src/images/Regresar.png"
            imagenEtiqueta = "/opt/BitacoraL/src/images/Etiqueta.png"            
        else:
            imagenconfig_interface = "C:/Program Files/Bitacora/src/images/root-03.png"
            imagenbGuardar = "C:/Program Files/Bitacora/src/images/Guardar.png"
            imagenbRegresar = "C:/Program Files/Bitacora/src/images/Regresar.png"
            imagenEtiqueta = "C:/Program Files/Bitacora/src/images/Etiqueta.png"
                        
        self.config_interface = pygame.image.load(imagenconfig_interface).convert()

        self.tag1 = pygame.image.load(imagenEtiqueta).convert_alpha()
        self.tag2 = pygame.image.load(imagenEtiqueta).convert_alpha() 
        self.tag3 = pygame.image.load(imagenEtiqueta).convert_alpha()
        self.tag4 = pygame.image.load(imagenEtiqueta).convert_alpha()
        self.tag5 = pygame.image.load(imagenEtiqueta).convert_alpha()
        
        self.bactualizar = pygame.image.load(imagenbGuardar).convert_alpha()
        self.bregresar = pygame.image.load(imagenbRegresar).convert_alpha()         
        
    def cargar_textbox(self):
        "Metodo para cargar TextBox y Textos a la Interfaz"
        # Cargamos Item para los Mensajes al Usuario
        self.titulo = Clases.eztext.Input(x=25, y=15, font = self.fuente, maxlength=20, color=(109,110,113), prompt='Configuracion de Conexion a Base de Datos')
        self.t_host = Clases.eztext.Input(x=188, y=42, font = self.fuente, maxlength=20, color=(109,110,113))
        self.t_puerto = Clases.eztext.Input(x=188, y=70, font = self.fuente, maxlength=20, color=(109,110,113))
        self.t_usuario = Clases.eztext.Input(x=188, y=99, font = self.fuente, maxlength=20, color=(109,110,113))
        self.t_pwd = Clases.eztext.Input(x=188, y=128, font = self.fuente, maxlength=20, color=(109,110,113))
        self.t_db = Clases.eztext.Input(x=188, y=155, font = self.fuente, maxlength=20, color=(109,110,113))
        self.mensaje = Clases.eztext.Input(x=50, y=200, font = self.fuente, maxlength=20, color=(255,0,0), prompt='')

    def cargar_botones(self):
        "Metodo para cargar Botones a la Interfaz"
        # Cargamos los Botones para la Interfaz
        self.actualizar = self.bactualizar.get_rect(center=(210,208 ))
        self.regresar = self.bregresar.get_rect(center=(350, 208))

    def dimencionar_ventana(self):
        "Metodo Para Dimencionar la Ventana"
        # Modo Resizable para Usuario
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Configuracion de Conexion a Base de Datos")

    def refresh_display(self):
        # refresh the display
        pygame.display.flip()
            
    def surface(self):
        "Metodo para Agregar los Surface a la Ventana Usuario"
        self.screen.blit(self.config_interface, (0,0))
        #self.screen.blit(self.tag1, (188,42))
        #self.screen.blit(self.tag2, (188,70))
        #self.screen.blit(self.tag3, (188,99))
        #self.screen.blit(self.tag4, (188,128))
        #self.screen.blit(self.tag5, (188,155))
        #self.screen.blit(self.bactualizar, self.bactualizar.get_rect(center=(210, 208)))
        #self.screen.blit(self.bregresar, self.bregresar.get_rect(center=(350, 208)))
        #self.titulo.draw(self.screen)
        self.t_host.draw(self.screen)
        self.t_puerto.draw(self.screen)
        self.t_usuario.draw(self.screen)
        self.t_pwd.draw(self.screen)
        self.t_db.draw(self.screen)
        self.mensaje.draw(self.screen)