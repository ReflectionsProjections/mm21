#!/usr/bin/env python2

import pygame as pg
import sys
sys.path.append("../map-generation")
sys.path.append("..")
import json
import time
import math
import vis_constants as const


class Visualizer(object):

    def __init__(self):
        self.screenHeight = const.screenHeight
        self.screenWidth = const.screenWidth
        self.title = const.title
        self.fps = const.FPStgt
        self.running = True
        pg.init()
        self.setup()

    def setup(self):
        pg.display.set_caption(self.title)
        pg.display.set_mode(self.screenHeight, self.screenWidth)
        self.gameClock = pg.time.Clock()

    def runFile(self, filename):
        try:
            with open(filename) as json_file:
                print "GG EASY"
        except:
            print "We fucked up " + filename + "! JK, the file doesn't exist!"
            sys.exit(69)


# Just for now
vis = Visualizer()
