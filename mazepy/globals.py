import math

VERSION = "0.4.0"

# Game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

PLAYER_SPEED = 0.003
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60

MOUSE_SENSITIVITY = 0.0002
MOUSE_MAX_REL = 40
MOUSE_BOARDER_LEFT = 100
MOUSE_BOARDER_RIGHT = WIDTH - MOUSE_BOARDER_LEFT

FLOOR_COLOR = (30, 30, 30)

# Ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 250
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2