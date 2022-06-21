import random

import pygame
from sys import exit
from random import randint, choice


class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_W1 = pygame.image.load("player_walk_1.png").convert_alpha()  # player surface and image 1
        player_W2 = pygame.image.load("player_walk_2.png").convert_alpha()  # player surface and image 2
        self.player_WK = [player_W1, player_W2]
        self.player_I = 0  # player index
        self.player_JUMP = pygame.image.load("jump.png").convert_alpha()  # player surface

        self.image = self.player_WK[self.player_I]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_mp3 = pygame.mixer.Sound("audio_jump.mp3")
        self.jump_mp3.set_volume(0.5)

    def player_in(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_mp3.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def anime_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_JUMP
        else:
            self.player_I += 0.1
            if self.player_I >= len(self.player_WK):
                self.player_I = 0
            self.image = self.player_WK[int(self.player_I)]

    def update(self):
        self.player_in()
        self.apply_gravity()
        self.anime_state()


class OBstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly1_S = pygame.image.load("Fly1.png").convert_alpha()  # fly surface and image 1
            fly2_S = pygame.image.load("Fly2.png").convert_alpha()  # fly surface and image 2
            self.frames = [fly1_S, fly2_S]
            y_pos = 210
        else:
            snail1_S = pygame.image.load("snail1.png").convert_alpha()  # snail surface and image 1
            snail2_S = pygame.image.load("snail2.png").convert_alpha()  # snail surface and image 2
            self.frames = [snail1_S, snail2_S]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def anime_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.anime_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    current_T = int(pygame.time.get_ticks() / 1000) - start_T  # current time
    score_S = test_F.render(str(current_T), False, "black")  # score surface
    score_R = score_S.get_rect(center=(400, 50))  # score surface rectangle
    screen.blit(score_S, score_R)
    return current_T


def obstacle_move(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail1_S, obstacle_rect)
            else:
                screen.blit(fly1_S, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if
                         obstacle.x > -100]  # deleting rectangles if they left the screen

        return obstacle_list
    else:
        return []


def collisions(player, obstacels):
    if obstacels:
        for obstacle_rect in obstacels:
            if player.colliderect(obstacle_rect):
                return False
    return True


def collide_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


def player_animations():
    global player_SURF, player_I

    if player_R.bottom < 300:
        player_SURF = player_JUMP
    else:
        player_I += 0.1
        if player_I >= len(player_WK):
            player_I = 0
        player_SURF = player_WK[int(player_I)]


pygame.init()  # initialization of window
screen = pygame.display.set_mode((800, 400))  # display window
pygame.display.set_caption("sponcered by abibas")  # window name
clock = pygame.time.Clock()  # frame rate managing
test_F = pygame.font.Font("Pixeltype.ttf", 50)  # title font
game_A = False
start_T = 0
score = 0

bg_mp3 = pygame.mixer.Sound("music.wav")
bg_mp3.play(loops=-1)

player = pygame.sprite.GroupSingle()
player.add(PLayer())

obstacle_group = pygame.sprite.Group()

test_S = pygame.image.load("Sky.png").convert()  # background image 1
gro_S = pygame.image.load("ground.png").convert()  # background image 2

snail1_S = pygame.image.load("snail1.png").convert_alpha()  # snail surface and image 1
snail2_S = pygame.image.load("snail2.png").convert_alpha()  # snail surface and image 2
snail_FRM = [snail1_S, snail2_S]
snail_FI = 0
snail_SURF = snail_FRM[snail_FI]

fly1_S = pygame.image.load("Fly1.png").convert_alpha()  # fly surface and image 1
fly2_S = pygame.image.load("Fly2.png").convert_alpha()  # fly surface and image 2
fly_FRM = [fly1_S, fly2_S]
fly_FI = 0
fly_SURF = [fly_FRM]

obstacle_rect = []  # obstacle rectangle list

player_W1 = pygame.image.load("player_walk_1.png").convert_alpha()  # player surface and image 1
player_W2 = pygame.image.load("player_walk_2.png").convert_alpha()  # player surface and image 2
player_WK = [player_W1, player_W2]
player_I = 0  # player index
player_JUMP = pygame.image.load("jump.png").convert_alpha()  # player surface

player_R = player_W1.get_rect(midbottom=(80, 300))  # player rectangle
player_G = 0  # player gravity

player_SURF = player_WK[player_I]
player_ST = pygame.image.load("player_stand.png").convert_alpha()  # player stand
player_ST = pygame.transform.rotozoom(player_ST, 0, 2)  # player stand scaled
player_STR = player_ST.get_rect(center=(400, 200))

game_N = test_F.render("RUN MODI RUN", False, (111, 196, 169))  # game name
game_NR = game_N.get_rect(center=(400, 80))  # game name rectangle

game_msg = test_F.render("Press Space To Run", False, (111, 196, 169))
game_msgR = game_msg.get_rect(center=(400, 340))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_anime_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_anime_timer, 500)

fly_anime_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_anime_timer, 200)

while True:  # window will not close immediately
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # to check if 'X' is clicked
            pygame.quit()
            exit()

        if game_A:  # game active
            if event.type == pygame.MOUSEBUTTONDOWN:  # 2nd way to get mouse position
                if player_R.collidepoint(event.pos):
                    player_G = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_R.bottom >= 300:
                    player_G = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_A = True
                start_T = int(pygame.time.get_ticks() / 1000)

        if game_A:
            if event.type == obstacle_timer:
                obstacle_group.add(OBstacle(choice(["fly", "snail", "snail", "snail", "fly"])))
                if randint(0, 2):
                    obstacle_rect.append(snail1_S.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect.append(fly1_S.get_rect(bottomright=(randint(900, 1100), 210)))

            if event.type == snail_anime_timer:
                if snail_FI == 0:
                    snail_FI = 1
                else:
                    snail_FI = 0
                snail_SURF = snail_FRM[snail_FI]

            if event.type == fly_anime_timer:
                if fly_FI == 0:
                    fly_FI = 1
                else:
                    fly_FI = 0
                fly_SURF = fly_FRM[fly_FI]

    if game_A:
        screen.blit(test_S, (0, 0))  # display of surface
        screen.blit(gro_S, (0, 300))

        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_A = collide_sprite()

    else:
        screen.fill("#3c5775")  # endgame screen background color
        screen.blit(player_ST, player_STR)
        obstacle_rect.clear()  # restart from emty list
        player_R.midbottom = (80, 300)  # re Postioning

        score_msg = test_F.render(f"Your Score: {score}", False, (111, 196, 169))
        score_msgR = score_msg.get_rect(center=(400, 330))
        screen.blit(game_N, game_NR)

        if score == 0:
            screen.blit(game_msg, game_msgR)
        else:
            screen.blit(score_msg, score_msgR)
    pygame.display.update()
    clock.tick(60)  # frame rate