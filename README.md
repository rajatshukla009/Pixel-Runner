[![Python](https://img.shields.io/badge/Python-v3.x-green.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-powered-yellow.svg)](https://www.pygame.org/)



# 2D Game in Python using Pygame library
This is a simple 2D game implemented in Python using the Pygame library. The game features a player sprite that moves left to right across the screen and must avoid obstacles such as flies and snails. The player sprite is animated using two different walking animations and a jumping animation. The game also features a timer that keeps track of the time the player has been playing.

Here's an overview of the code:
- The Player class extends the pygame.sprite.Sprite class and sets up the player sprite with its images, rectangles, and sound effects.
- The Obstacle class extends the pygame.sprite.Sprite class and sets up the obstacle sprite with its images and rectangles.
- The display_score function displays the current time the player has been playing.
- The obstacle_move function moves the obstacles across the screen.
- The collisions function checks for collisions between the player sprite and the obstacle sprites.
- The main game loop updates the player sprite and obstacle sprites and checks for collisions.

Overall, this code provides a basic template for creating a 2D platformer game in Python using Pygame.
