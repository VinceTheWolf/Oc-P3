#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
import variables
import random

class Items:
    def __init__(self, item1, item2, item3, level, fullwindow):
        self.case_x = 0
        self.case_y = 0
        self.item1x = ''
        self.item1y = ''
        self.item2x = ''
        self.item2y = ''
        self.item3x = ''
        self.item3y = ''

        self.level = level
        
        self.setitem1 = pygame.image.load(item1).convert()
        self.setitem1 = pygame.transform.scale(self.setitem1, (60, 60))

        self.setitem2 = pygame.image.load(item2).convert()
        self.setitem2 = pygame.transform.scale(self.setitem2, (60, 60))

        self.setitem3 = pygame.image.load(item3).convert()
        self.setitem3 = pygame.transform.scale(self.setitem3, (60, 60))

        self.itemplace(fullwindow)

    def itemplace(self, fullwindow):
        item1case_x = 0
        item1case_y = 0
        item2case_x = 0
        item2case_y = 0
        item3case_x = 0
        item3case_y = 0


        #SYRINGE
        while self.level.structure[item1case_y][item1case_x] != '0':
            item1case_x = random.randint(0, 14)
            item1case_y = random.randint(0, 14)
        
        self.level.structure[item1case_y][item1case_x] = 's'
        self.item1x = item1case_x * 60
        self.item1y = item1case_y * 60
        fullwindow.blit(self.setitem1, (self.item1x, self.item1y))


        #NEEDLE
        while self.level.structure[item2case_y][item2case_x] != '0':
            item2case_x = random.randint(0, 14)
            item2case_y = random.randint(0, 14)
        
        self.level.structure[item2case_y][item2case_x] = 'n'
        self.item2x = item2case_x * 60
        self.item2y = item2case_y * 60
        fullwindow.blit(self.setitem2, (self.item2x, self.item2y))

        #ETHER
        while self.level.structure[item3case_y][item3case_x] != '0':
            item3case_x = random.randint(0, 14)
            item3case_y = random.randint(0, 14)
        
        self.level.structure[item3case_y][item3case_x] = 'e'
        self.item3x = item3case_x * 60
        self.item3y = item3case_y * 60
        fullwindow.blit(self.setitem3, (self.item3x, self.item3y))
