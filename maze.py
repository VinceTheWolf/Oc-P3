#! /usr/bin/venv python3
# coding: utf-8
"""This whole script manages the generation of the labyrinth
"""
import pygame
from pygame.locals import *
import variables

class Maze:
    """Analyse the model and place walls
    """
    #On recupere le fichier du labyrinthe
    def __init__(self):
        self.file = variables.model
        self.structure = 0

    def analyse(self):
        """This function traverses the model file
        by analyzing each line and each sprite"""
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
        """Placing wall
        """
        wall = pygame.image.load(variables.wall).convert()
        wall = pygame.transform.scale(wall, (60, 60))
        guardian = pygame.image.load(variables.guardian).convert()
        guardian = pygame.transform.scale(guardian, (60, 60))

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                posx = num_case * 60
                posy = num_line * 60
                if sprite == 'm':
                    fullwindow.blit(wall, (posx, posy))
                if sprite == 'a':
                    fullwindow.blit(guardian, (posx, posy))
                num_case += 1
            num_line += 1
