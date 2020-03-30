#! /usr/bin/env python3
# coding: utf-8
"""This script will place items in the maze"""
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
import random
import pygame
from pygame.locals import *


class Items:
    """Load and place items"""
    def __init__(self, item1, item2, item3, level, fullwindow):
        """Load items image"""
        self.item_x = ''
        self.item_y = ''
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
        """Place items"""
        items = 1
        pos_x = 0
        pos_y = 0

        while items < 4:
            while self.level.structure[pos_y][pos_x] != '0':
                pos_x = random.randint(0, 14)
                pos_y = random.randint(0, 14)
            self.item_x = pos_x * 60
            self.item_y = pos_y * 60
            if items == 1:
                self.level.structure[pos_y][pos_x] = 's'
                fullwindow.blit(self.setitem1, (self.item_x, self.item_y))
                self.item1x = self.item_x
                self.item1y = self.item_y
            if items == 2:
                self.level.structure[pos_y][pos_x] = 'n'
                fullwindow.blit(self.setitem2, (self.item_x, self.item_y))
                self.item2x = self.item_x
                self.item2y = self.item_y
            if items == 3:
                self.level.structure[pos_y][pos_x] = 'e'
                fullwindow.blit(self.setitem3, (self.item_x, self.item_y))
                self.item3x = self.item_x
                self.item3y = self.item_y
            items += 1
