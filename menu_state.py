import pygame
from enum import Enum
from menu_sprites import MenuSprite, LogoSprite, StartButtonSprite, ExitButtonSprite

INACTIVE = 0
ACTIVE = 1


class States(Enum):
    GAME = 1
    MENU = 2
    EXIT = 3


class MenuState:
    def __init__(self, screen_width, screen_height):
        self.menu_sprite = MenuSprite(screen_width, screen_height)
        self.logo_sprite = LogoSprite(screen_width)
        self.start_button_sprite = StartButtonSprite(screen_width, screen_height)
        self.exit_button_sprite = ExitButtonSprite(screen_width, screen_height)

        self.menu_sprites_list = pygame.sprite.Group()
        self.background_sprite_list = pygame.sprite.Group()
        self.background_sprite_list.add(self.menu_sprite)
        self.menu_sprites_list.add(self.logo_sprite, self.start_button_sprite, self.exit_button_sprite)
        self.new_state = States.MENU

    def menu(self):
        self.menu_sprites_list.update()
        mouse_position = pygame.mouse.get_pos()
        self.start_button_sprite.set_state(INACTIVE)
        self.exit_button_sprite.set_state(INACTIVE)
        if self.start_button_sprite.rect.collidepoint(mouse_position):
            self.start_button_sprite.set_state(ACTIVE)
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                self.new_state = States.GAME

        if self.exit_button_sprite.rect.collidepoint(mouse_position):
            self.exit_button_sprite.set_state(ACTIVE)
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                self.new_state = States.EXIT

        return self.new_state

    def draw(self, screen):
        self.background_sprite_list.draw(screen)
        self.menu_sprites_list.draw(screen)

