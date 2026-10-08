import pygame
import random
import math

# ============================================================
# NEUROCHASE
# Human Intelligence vs Artificial Intelligence
# ============================================================

pygame.init()

# -------------------- WINDOW --------------------

WIDTH = 1100
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEUROCHASE - Adaptive AI Game")

clock = pygame.time.Clock()

# -------------------- COLORS --------------------

BACKGROUND = (12, 18, 30)
WHITE = (240, 245, 250)
GREY = (100, 110, 125)
GREEN = (50, 220, 150)
BLUE = (60, 160, 255)
RED = (240, 70, 90)
YELLOW = (250, 210, 70)
PURPLE = (180, 100, 255)
DARK_PANEL = (20, 28, 45)
WALL = (45, 60, 80)

# -------------------- FONTS --------------------

font_big = pygame.font.SysFont("Arial", 32, bold=True)
font_medium = pygame.font.SysFont("Arial", 22, bold=True)
font_small = pygame.font.SysFont("Arial", 17)

# ============================================================
# MAZE
# ============================================================

CELL = 40

MAZE = [
    "########################",
    "#P     #       #       #",
    "# ###  # ##### # ##### #",
    "#      #     # #       #",
    "###### ##### # ######  #",
    "#          #            #",
    "# ######## # #########  #",
    "#        #              #",
    "# ###### ########### ## #",
    "#      #        #       #",
    "#####  # ###### # ##### #",
    "#      #      # #       #",
    "# ####### ### # ####### #",
    "#         #   #         #",
    "# ####### # ####### ### #",
    "#       #       #       #",
    "# ### # ####### # ##### #",
    "#     #         #       #",
    "########################"
]

# Convert maze into coordinates

walls = []
player_start = None

for row, line in enumerate(MAZE):
    for col, character in enumerate(line):

        x = col * CELL
        y = row * CELL

        if character == "#":
            walls.append(pygame.Rect(x, y, CELL, CELL))

        elif character == "P":
            player_start = pygame.Vector2(
                x + CELL / 2,
                y + CELL / 2
            )

# Game area is slightly smaller than screen
GAME_WIDTH = len(MAZE[0]) * CELL
GAME_HEIGHT = len(MAZE) * CELL

PANEL_X = GAME_WIDTH + 15


# ============================================================
# PLAYER
# ============================================================

class Player:

    def __init__(self):
        self.position = player_start.copy()
        self.radius = 12
        self.speed = 3.5

        self.last_direction = None

    def reset(self):
        self.position = player_start.copy()
        self.last_direction = None

    def move(self, dx, dy):

        direction = None

        if dx > 0:
            direction = "RIGHT"
        elif dx < 0:
            direction = "LEFT"
        elif dy > 0:
            direction = "DOWN"
        elif dy < 0:
            direction = "UP"

        if direction:
            self.last_direction = direction

        # Horizontal movement
        new_position = pygame.Vector2(
            self.position.x + dx * self.speed,
            self.position.y
        )

        if not self.collides(new_position):
            self.position.x = new_position.x

        # Vertical movement
        new_position = pygame.Vector2(
            self.position.x,
            self.position.y + dy * self.speed
        )

        if not self.collides(new_position):
            self.position.y = new_position.y

    def collides(self, position):

        player_rect = pygame.Rect(
            position.x - self.radius,
            position.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        for wall in walls:
            if player_rect.colliderect(wall):
                return True

        return False

    def draw(self):

        pygame.draw.circle(
            screen,
            BLUE,
            (int(self.position.x), int(self.position.y)),
            self.radius
        )

        # Small direction indicator
        pygame.draw.circle(
            screen,
            WHITE,
            (int(self.position.x + 4), int(self.position.y - 4)),
            3
        )


# ============================================================
# AI LEARNING SYSTEM
# ============================================================

class LearningAI:

    def __init__(self):

        # Number of times the player has moved
        self.moves = {
            "UP": 0,
            "DOWN": 0,
            "LEFT": 0,
            "RIGHT": 0
        }

        # Situations → actions
        self.patterns = {}

        self.total_experience = 0

        self.last_prediction = "UNKNOWN"

        self.correct_predictions = 0
        self.prediction_attempts = 0

    # --------------------------------------------------------

    def learn(self, situation, action):

        if action is None:
            return

        # Record general movement
        self.moves[action] += 1

        # Record movement for a particular situation
        if situation not in self.patterns:

            self.patterns[situation] = {
                "UP": 0,
                "DOWN": 0,
                "LEFT": 0,
                "RIGHT": 0
            }

        self.patterns[situation][action] += 1

        self.total_experience += 1

        # Check whether previous prediction was correct
        if self.last_prediction != "UNKNOWN":

            self.prediction_attempts += 1

            if self.last_prediction == action:
                self.correct_predictions += 1

    # --------------------------------------------------------

    def predict(self, situation):

        # If we don't know anything yet,
        # choose a random direction.

        if situation not in self.patterns:

            available = ["UP", "DOWN", "LEFT", "RIGHT"]

            prediction = random.choice(available)

        else:

            data = self.patterns[situation]

            # Find the most common movement
            prediction = max(
                data,
                key=data.get
            )

            # If all values are zero
            if data[prediction] == 0:
                prediction = random.choice(
                    ["UP", "DOWN", "LEFT", "RIGHT"]
                )

        self.last_prediction = prediction

        return prediction

    # --------------------------------------------------------

    def confidence(self):

        total = sum(self.moves.values())

        if total == 0:
            return 0

        largest = max(self.moves.values())

        return int((largest / total) * 100)

    # --------------------------------------------------------

    def accuracy(self):

        if self.prediction_attempts == 0:
            return 0

        return int(
            self.correct_predictions /
            self.prediction_attempts * 100
        )

    # --------------------------------------------------------

    def most_common_move(self):

        if self.total_experience == 0:
            return "UNKNOWN"

        return max(
            self.moves,
            key=self.moves.get
        )


# ============================================================
# AI ROBOT
# ============================================================

class AIEnemy:

    def __init__(self):

        self.position = pygame.Vector2(
            GAME_WIDTH - 80,
            GAME_HEIGHT - 80
        )

        self.radius = 14

        self.speed = 1.8

        self.ai = LearningAI()

        self.predicted_direction = "UNKNOWN"

    # --------------------------------------------------------

    def reset(self):

        self.position = pygame.Vector2(
            GAME_WIDTH - 80,
            GAME_HEIGHT - 80
        )

        self.ai.last_prediction = "UNKNOWN"

    # --------------------------------------------------------

    def get_situation(self, player):

        dx = player.position.x - self.position.x
        dy = player.position.y - self.position.y

        horizontal = "RIGHT" if dx > 0 else "LEFT"
        vertical = "DOWN" if dy > 0 else "UP"

        distance = math.sqrt(dx * dx + dy * dy)

        if distance < 160:
            danger = "CLOSE"

        elif distance < 300:
            danger = "MEDIUM"

        else:
            danger = "FAR"

        return (
            horizontal,
            vertical,
            danger
        )

    # --------------------------------------------------------

    def update(self, player):

        situation = self.get_situation(player)

        self.predicted_direction = self.ai.predict(
            situation
        )

        # Target prediction

        predicted_position = player.position.copy()

        prediction_distance = 90

        if self.predicted_direction == "UP":
            predicted_position.y -= prediction_distance

        elif self.predicted_direction == "DOWN":
            predicted_position.y += prediction_distance

        elif self.predicted_direction == "LEFT":
            predicted_position.x -= prediction_distance

        elif self.predicted_direction == "RIGHT":
            predicted_position.x += prediction_distance

        # Move towards predicted position

        direction = (
            predicted_position -
            self.position
        )

        if direction.length() > 0:
            direction = direction.normalize()

        new_position = (
            self.position +
            direction * self.speed
        )

        # Don't walk through walls
        if not self.collides(new_position):

            self.position = new_position

        else:

            # If prediction causes collision,
            # move directly toward player.

            direction = (
                player.position -
                self.position
            )

            if direction.length() > 0:
                direction = direction.normalize()

            new_position = (
                self.position +
                direction * self.speed
            )

            if not self.collides(new_position):
                self.position = new_position

    # --------------------------------------------------------

    def collides(self, position):

        enemy_rect = pygame.Rect(
            position.x - self.radius,
            position.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        for wall in walls:

            if enemy_rect.colliderect(wall):
                return True

        return False

    # --------------------------------------------------------

    def draw(self):

        pygame.draw.circle(
            screen,
            RED,
            (int(self.position.x),
             int(self.position.y)),
            self.radius
        )

        # Robot eyes

        pygame.draw.circle(
            screen,
            WHITE,
            (int(self.position.x - 5),
             int(self.position.y - 3)),
            3
        )

        pygame.draw.circle(
            screen,
            WHITE,
            (int(self.position.x + 5),
             int(self.position.y - 3)),
            3
        )


# ============================================================
# GAME OBJECTS
# ============================================================

player = Player()
enemy = AIEnemy()

score = 0
lives = 3

game_over = False

last_player_direction = None

# ============================================================
# FUNCTIONS
# ============================================================

def draw_maze():

    for wall in walls:

        pygame.draw.rect(
            screen,
            WALL,
            wall
        )

        pygame.draw.rect(
            screen,
            (65, 85, 110),
            wall,
            1
        )


# ------------------------------------------------------------

def draw_panel():

    panel = pygame.Rect(
        GAME_WIDTH,
        0,
        WIDTH - GAME_WIDTH,
        HEIGHT
    )

    pygame.draw.rect(
        screen,
        DARK_PANEL,
        panel
    )

    # Title

    title = font_big.render(
        "AI BRAIN",
        True,
        GREEN
    )

    screen.blit(
        title,
        (PANEL_X, 25)
    )

    # Divider

    pygame.draw.line(
        screen,
        GREY,
        (PANEL_X, 70),
        (WIDTH - 20, 70),
        1
    )

    y = 90

    def text(label, value, colour=WHITE):

        nonlocal y

        line = font_small.render(
            f"{label}: {value}",
            True,
            colour
        )

        screen.blit(
            line,
            (PANEL_X, y)
        )

        y += 27

    # AI information

    text(
        "EXPERIENCE",
        enemy.ai.total_experience
    )

    text(
        "AI CONFIDENCE",
        f"{enemy.ai.confidence()}%"
    )

    text(
        "PREDICTION",
        enemy.predicted_direction,
        YELLOW
    )

    text(
        "ACCURACY",
        f"{enemy.ai.accuracy()}%",
        PURPLE
    )

    text(
        "MOST COMMON",
        enemy.ai.most_common_move(),
        GREEN
    )

    y += 10

    pygame.draw.line(
        screen,
        GREY,
        (PANEL_X, y),
        (WIDTH - 20, y),
        1
    )

    y += 20

    heading = font_medium.render(
        "PLAYER BEHAVIOUR",
        True,
        WHITE
    )

    screen.blit(
        heading,
        (PANEL_X, y)
    )

    y += 40

    total = sum(enemy.ai.moves.values())

    directions = [
        ("UP", BLUE),
        ("DOWN", BLUE),
        ("LEFT", BLUE),
        ("RIGHT", BLUE)
    ]

    for direction, colour in directions:

        count = enemy.ai.moves[direction]

        if total > 0:
            percentage = int(
                count / total * 100
            )
        else:
            percentage = 0

        label = font_small.render(
            f"{direction:<6} {percentage}%",
            True,
            WHITE
        )

        screen.blit(
            label,
            (PANEL_X, y)
        )

        # Progress bar

        bar_x = PANEL_X + 100
        bar_y = y + 4

        pygame.draw.rect(
            screen,
            GREY,
            (bar_x, bar_y, 130, 12)
        )

        pygame.draw.rect(
            screen,
            colour,
            (
                bar_x,
                bar_y,
                int(130 * percentage / 100),
                12
            )
        )

        y += 35

    y += 10

    pygame.draw.line(
        screen,
        GREY,
        (PANEL_X, y),
        (WIDTH - 20, y),
        1
    )

    y += 20

    status = "LEARNING"

    if enemy.ai.total_experience > 50:
        status = "ADAPTING"

    if enemy.ai.total_experience > 120:
        status = "PREDICTING"

    text(
        "STATUS",
        status,
        GREEN
    )

    text(
        "SCORE",
        score,
        YELLOW
    )

    text(
        "LIVES",
        lives,
        RED
    )

    y += 15

    controls = [
        "WASD / ARROWS = MOVE",
        "R = RESTART",
        "ESC = QUIT"
    ]

    for instruction in controls:

        line = font_small.render(
            instruction,
            True,
            GREY
        )

        screen.blit(
            line,
            (PANEL_X, y)
        )

        y += 25


# ============================================================
# COLLISION
# ============================================================

def enemy_catches_player():

    distance = player.position.distance_to(
        enemy.position
    )

    return distance < 28


# ============================================================
# RESTART
# ============================================================

def restart_game():

    global score
    global lives
    global game_over

    player.reset()
    enemy.reset()

    score = 0
    lives = 3

    enemy.ai = LearningAI()

    game_over = False


# ============================================================
# MAIN GAME LOOP
# ============================================================

running = True

while running:

    clock.tick(60)

    # --------------------------------------------------------
    # EVENTS
    # --------------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_r:
                restart_game()

    # --------------------------------------------------------
    # KEYBOARD
    # --------------------------------------------------------

    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -1

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = 1

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -1

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = 1

    # Prevent diagonal movement from being faster

    if dx != 0 and dy != 0:

        dx *= 0.707
        dy *= 0.707

    # --------------------------------------------------------
    # PLAYER MOVEMENT
    # --------------------------------------------------------

    player.move(dx, dy)

    # --------------------------------------------------------
    # LEARNING
    # --------------------------------------------------------

    if player.last_direction:

        if (
            player.last_direction
            != last_player_direction
        ):

            situation = enemy.get_situation(
                player
            )

            enemy.ai.learn(
                situation,
                player.last_direction
            )

            last_player_direction = (
                player.last_direction
            )

    # --------------------------------------------------------
    # AI UPDATE
    # --------------------------------------------------------

    if not game_over:

        enemy.update(player)

    # --------------------------------------------------------
    # COLLISION WITH PLAYER
    # --------------------------------------------------------

    if enemy_catches_player():

        lives -= 1

        if lives <= 0:

            game_over = True

        else:

            player.reset()
            enemy.reset()

    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    screen.fill(BACKGROUND)

    draw_maze()

    player.draw()
    enemy.draw()

    draw_panel()

    # --------------------------------------------------------
    # GAME OVER
    # --------------------------------------------------------

    if game_over:

        overlay = pygame.Surface(
            (GAME_WIDTH, GAME_HEIGHT)
        )

        overlay.set_alpha(210)

        overlay.fill(
            (5, 8, 15)
        )

        screen.blit(
            overlay,
            (0, 0)
        )

        game_over_text = font_big.render(
            "AI HAS LEARNED YOUR MOVEMENT!",
            True,
            RED
        )

        screen.blit(
            game_over_text,
            (
                130,
                280
            )
        )

        restart_text = font_medium.render(
            "Press R to challenge the AI again",
            True,
            WHITE
        )

        screen.blit(
            restart_text,
            (
                170,
                330
            )
        )

    pygame.display.flip()


pygame.quit()
