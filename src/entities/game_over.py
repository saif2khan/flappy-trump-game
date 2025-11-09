import pygame

from ..utils import GameConfig
from .entity import Entity


class GameOver(Entity):
    def __init__(self, config: GameConfig) -> None:
        super().__init__(
            config=config,
            image=config.images.game_over,
            x=(config.window.width - config.images.game_over.get_width()) // 2,
            y=int(config.window.height * 0.2),
        )
        # Load the Trump meme image (JPG doesn't have alpha, use convert())
        self.trump_meme = pygame.image.load(
            "assets/sprites/Donald-Trump-mad-meme-4.jpg"
        ).convert()
        # Scale the meme image to fit nicely (adjust size as needed)
        meme_width = min(200, config.window.width * 0.6)
        meme_height = int(self.trump_meme.get_height() * (meme_width / self.trump_meme.get_width()))
        self.trump_meme = pygame.transform.scale(self.trump_meme, (int(meme_width), meme_height))
        # Position the meme below the gameover image
        self.trump_meme_x = (config.window.width - self.trump_meme.get_width()) // 2
        self.trump_meme_y = self.y + self.h + 20  # 20 pixels spacing below gameover

    def draw(self) -> None:
        # Draw the gameover image
        if self.image:
            self.config.screen.blit(self.image, self.rect)
        # Draw the Trump meme below it
        self.config.screen.blit(self.trump_meme, (self.trump_meme_x, self.trump_meme_y))
