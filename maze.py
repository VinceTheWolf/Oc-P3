#! /usr/bin/venv python3
# coding: utf-8

import pygame
from pygame.locals import *
import variables
from variables import *
import random

class Maze:
    #On recupere le fichier du labyrinthe
    def __init__(self, file):
        self.file = variables.model
        self.structure = 0

    #On parcourt le fichier model en analisant chaque sprite de chaque ligne
    def analyse(self):
        with open(self.file, "r") as file:
            structure_level = []
            #Analise des lignes
            for line in file:
                line_level = []
                #Analise des sprites
                for sprite in line:
                    #Si plus de sprite, on passe a la ligne suivante
                    if sprite != '\n':
                        line_level.append(sprite)
                structure_level.append(line_level)
            self.structure = structure_level
        
    def map(self, fullwindow):
        #Chargement des murs
        wall = pygame.image.load(variables.wall).convert()
        wall = pygame.transform.scale(wall, (60, 60))
        guardian = pygame.image.load(variables.guardian).convert()
        guardian = pygame.transform.scale(guardian, (60, 60))
        
        #On parcourt de nouveau le fichier model pour trouver les positions des murs
        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * 60
                y = num_line * 60
                if sprite == 'm':
                    fullwindow.blit(wall, (x,y))
                if sprite == 'a':
                    fullwindow.blit(guardian, (x,y))
                num_case += 1
            num_line += 1