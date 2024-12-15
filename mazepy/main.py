import pygame
from globals import *
from maps import Map
from object_renderer import ObjectRenderer
from player import Player
from raycasting import RayCasting


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        pygame.display.set_caption("3D Maze Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.delta_time = 1

        # Initialize game components
        self.map = Map()  # Load the single map from map-data
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.exit_position = self.find_exit()

    def find_exit(self):
        """Find the exit position (marked by '9') in the map grid."""
        for pos, value in self.map.world_map.items():
            if value == 9:
                return pos
        return None

    def update(self):
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)

    def draw(self):
        self.object_renderer.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

        # Check if the player reached the exit (proximity check)
        exit_x, exit_y = self.exit_position
        player_x, player_y = self.player.pos  # Player's precise coordinates

        if abs(player_x - exit_x) < 0.5 and abs(player_y - exit_y) < 0.5:  # Check proximity
            print("You Win! Congratulations!")
            self.running = False

    def run(self):
        print("Game Started! Navigate through the maze and find the exit.")
        while self.running:
            self.check_events()
            self.update()
            self.draw()
        pygame.quit()


def main():
    print("Welcome to the 3D Maze Game!")
    game = Game()
    game.run()
    print("Game Over. Thanks for playing!")


if __name__ == "__main__":
    main()