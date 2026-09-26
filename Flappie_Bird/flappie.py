# Making a flappy bird clone using presets in python.
import pygame as py
import pathlib as path
import os

class Bird:
    def __init__(self, preset: str, initial_position: py.Vector2, radius: int):

        self.preset = preset
        self.radius = radius

        # Game const
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
            self.reset() # it resets the player values
            return False
        else :
            return True
    # Actions from the player
    def birdie_jump(self) -> None:
        """It applies the jump"""
        self.reset_gravity()
        self.position.y -= 100
    # Resets
    def reset_gravity(self) -> float:
        """Resets the gravity to its original value"""
        self.gravity = 500 * self.delta_time
        return self.gravity

    def reset(self):
        """Resets"""
        self.position = py.Vector2(self.initial_position)
        self.gravity = 0

    def applying_gravity(self, state: bool):
        """Applying gravity but just at the Y axis"""
        if state:
            self.position.y += self.gravity * self.delta_time

# class to deal with the files.
class Files:
    def __init__(self, directory: str):
        self.directory = directory

        self.__directory_list = []

    def checking_files(self, path_assets: str) -> list[str]:
        """Checking if the path obtained of the file exist"""
        target_directory = path.Path(path_assets)

        if not target_directory.exists():
            print(f"The directory {target_directory} was not found.")

        for asset_file in os.listdir(target_directory):
            try:
                if not os.path.isfile(asset_file):
                    raise FileNotFoundError("This files does not exits.")
                elif not asset_file.endswith(".png"):
                    raise FileExistsError(f"The file {asset_file} is not PNG.")
                else:
                    self.__directory_list.append(asset_file)
            except FileNotFoundError as error:
                raise error

        return self.__directory_list

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
