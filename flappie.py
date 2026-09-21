# Making a flappy bird clone using presets in python.
import pygame as py

class Bird:
    def __init__(self, preset: str, initial_position: py.Vector2, radius: int):

        self.preset = preset
        self.radius = radius

        self.initial_position = initial_position

        self.delta_time = 1 / 60
        self.gravity = 500 * self.delta_time
        self.position = py.Vector2(self.initial_position)

    def drawing_birdie(self, screen_surface: py.Surface) -> py.Rect:
        """Drawing the bird and his presets"""
        # Work in progress
        return py.draw.circle(screen_surface, self.preset, self.position, self.radius)

    def birdie_has_lost(self, screen_height: int, radius: int) -> bool:
        """It checks if the player has lost"""
        if self.position.y <= 0 or self.position.y + radius > screen_height:
            self.position = py.Vector2(self.initial_position)
            self.gravity = 0
            return False
        else :
            return True

    def birdie_jump(self) -> None:
        """It applies the jump"""
        self.reset_gravity()
        self.position.y -= 100

    def reset_gravity(self) -> float:
        """Resets the gravity to its original value"""
        self.gravity = 500 * self.delta_time
        return self.gravity

    def applying_gravity(self, state: bool):
        """Applying gravity but just at the Y axis"""
        if state:
            self.position.y += self.gravity * self.delta_time

def main():
    screen_bounds_width: int = 500
    screen_bounds_height: int = 800

    py.init()
    screen = py.display.set_mode((screen_bounds_width, screen_bounds_height))

    player_pos = py.Vector2(150, 400)
    bird = Bird( "#e35524", player_pos, 20)

    while True:

        for event in py.event.get():
            if event.type == py.QUIT:
                return True
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    bird.birdie_jump()

        screen.fill("Black")

        bird.drawing_birdie(screen)
        bird.applying_gravity(bird.birdie_has_lost(screen_bounds_height, 20))

        py.display.flip()

py.quit()

if  __name__ == "__main__":
    main()
