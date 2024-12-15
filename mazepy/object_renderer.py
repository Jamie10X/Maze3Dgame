import pygame
from globals import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        image_path = f"resources/textures/{self.game.map.sky}"
        self.celling_image = self.get_texture(image_path, (WIDTH, HALF_HEIGHT))
        self.floor_color = self.game.map.floor
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.celling_image, (-self.sky_offset, 0))
        self.screen.blit(self.celling_image, (-self.sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, self.floor_color, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture("resources/textures/1.png"),
            2: self.get_texture("resources/textures/2.png"),
            3: self.get_texture("resources/textures/3.png"),
            4: self.get_texture("resources/textures/4.png"),
            8: self.get_texture("resources/textures/8.png"),
            9: self.get_texture("resources/textures/9.png"),
        }