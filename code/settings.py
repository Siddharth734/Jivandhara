import pygame
from os import walk
from os.path import join,exists
from pytmx.util_pygame import load_pygame
from math import sin
from debug import Debug
from random import randint,choice,uniform

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
TILESIZE = 64
FPS = 60

HITBOX_OFFSET = {
    'player': -26,
    'objects': -40,
    'grass': -10,
    'invisible': 0}

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = join('graphics','font','joystix.ttf')
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOUR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOUR_ACTIVE =  'gold'

TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

weapons_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': ('graphics','weapons','sword','full.png')},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': ('graphics','weapons','lance','full.png')},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': ('graphics','weapons','axe','full.png')},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': ('graphics','weapons','rapier','full.png')},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': ('graphics','weapons','sai','full.png')}
}

magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': ('graphics','particles','flame','fire.png')},
    'heal': {'strength': 20, 'cost': 10, 'graphic': ('graphics','particles','heal','heal.png')}
}

monster_data = {
    'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':('audio', 'attack', 'slash.wav'),
             'speed': 2, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':('audio', 'attack', 'claw.wav'),
            'speed': 1, 'resistance': 1, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':('audio', 'attack', 'fireball.wav'),
             'speed': 3, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':('audio', 'attack', 'slash.wav'),
             'speed': 2, 'resistance': 100, 'attack_radius': 50, 'notice_radius': 300}}