#! /usr/bin/venv python3
# coding: utf-8
"""All the needed variables for other scripts"""
import pygame

WINDOW_LENGTH = 900
WINDOW_WIDTH = 1200
SPRITE_NUMBER = 15
SIZE_SPRITE = WINDOW_LENGTH / SPRITE_NUMBER
MODEL = 'model.txt'
FENETRE = pygame.display.set_mode((900, 900))  # Définition de la fenêtre
SYRINGE = ('ressources/seringue.png')
NEEDLE = ('ressources/aiguille.png')
ETHER = ('ressources/ether.png')
MAC = ('ressources/MacGyver.png')
GUARDIAN = ('ressources/Gardien.png')
WALL = ('ressources/mur.jpg')
