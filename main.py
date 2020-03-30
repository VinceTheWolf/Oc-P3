#! /usr/bin/env python3
# coding: utf-8

"""This script is using classes from other script to generate maze, place characters & items
and move MacGyver
"""
# pylint: disable=no-member
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
import pygame
from pygame.locals import *
from items import Items
from maze import Maze
from character import Charac
import variables

pygame.init()

def main():
    # pylint: disable=undefined-variable
    """Main function
    """
    #Load Window
    fullwindow = pygame.display.set_mode((900, 900))
    fond = pygame.image.load('ressources/fond5.jpg').convert()
    fond = pygame.transform.scale(fond, (900, 900))

    #level structure
    level = Maze()
    level.analyse()
    level.map(fullwindow)

    #Items
    allitems = Items(variables.SYRINGE, variables.NEEDLE, variables.ETHER, level, fullwindow)

    #Character
    mac = Charac(variables.MAC, level)
    pygame.display.flip()

    continuer = 1
    game = mac.game
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = 0
            if game != 0:

                #Items Counter
                itemsget = str(len(mac.inventory))
                font = pygame.font.SysFont("comicsansms", 18)
                text = font.render("Items: " + itemsget, True, (255, 0, 0))

                fullwindow.blit(fond, (0, 0))
                level.map(fullwindow)
                if 's' not in mac.inventory:
                    fullwindow.blit(allitems.setitem1, (allitems.item1x, allitems.item1y))
                if 'n' not in mac.inventory:
                    fullwindow.blit(allitems.setitem2, (allitems.item2x, allitems.item2y))
                if 'e' not in mac.inventory:
                    fullwindow.blit(allitems.setitem3, (allitems.item3x, allitems.item3y))
                fullwindow.blit(mac.macg, (mac.pos_x, mac.pos_y))
                fullwindow.blit(text, (0, 0))

                pygame.display.flip()

                #Moves of MacGyver
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        mac.move('droite')
                        mac.getitems(fullwindow)
                    elif event.key == K_LEFT:
                        mac.move('gauche')
                        mac.getitems(fullwindow)
                    elif event.key == K_UP:
                        mac.move('haut')
                        mac.getitems(fullwindow)
                    elif event.key == K_DOWN:
                        mac.move('bas')
                        mac.getitems(fullwindow)
                game = mac.game

if __name__ == "__main__":
    main()
