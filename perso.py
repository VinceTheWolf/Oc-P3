#! /usr/bin/venv python3
# coding: utf-8

import pygame
from pygame.locals import *
import variables
from variables import *
import random


class Perso:
    def __init__(self, mg, level, fullwindow):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.macg = pygame.image.load(mg).convert()
        self.macg = pygame.transform.scale(self.macg, (60, 60))
        self.inventory = []
        self.count = len(self.inventory)
        pygame.display.flip()
        self.level = level
        self.game = 1

    def deplacer(self, direction, fullwindow):
        if direction == 'droite':
            if self.case_x < (sprite_number - 1):
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    self.case_x += 1
                    self.x = self.case_x * size_sprite

        if direction == 'gauche':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * size_sprite

        if direction == 'haut':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * size_sprite

        if direction == 'bas':
            if self.case_y < (sprite_number - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * size_sprite
        
        if self.level.structure[self.case_y][self.case_x] == 's':
            self.inventory.append('s')
            self.level.structure[self.case_y][self.case_x] = '0'
            self.count = len(self.inventory)

        if self.level.structure[self.case_y][self.case_x] == 'n':
            self.inventory.append('n')
            self.level.structure[self.case_y][self.case_x] = '0'
            self.count = len(self.inventory)

        if self.level.structure[self.case_y][self.case_x] == 'e':
            self.inventory.append('e')
            self.level.structure[self.case_y][self.case_x] = '0'
            self.count = len(self.inventory)

        if self.level.structure[self.case_y][self.case_x] == 'a':
            if self.count != 3:
                lose = pygame.image.load('ressources/Youlose.png').convert()
                lose = pygame.transform.scale(lose, (900,900))
                fullwindow.blit(lose, (0,0))
                pygame.display.flip()
                self.game = 0
            
            elif self.count == 3:
                win = pygame.image.load('ressources/YouWin.png').convert()
                win = pygame.transform.scale(win, (900,900))
                fullwindow.blit(win, (0,0))
                pygame.display.flip()
                self.game = 0