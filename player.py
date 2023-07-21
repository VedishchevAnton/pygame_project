import pygame


class Player:
    """Класс игрок"""
    def __init__(self):
        self.image = pygame.image.load("image/player.png")  # загрузка изображения игрока
        self.rect = self.image.get_rect()  # получение прямоугольника, описывающего изображение игрока
        self.rect.center = (400, 300)  # установка центра прямоугольника в координаты (400, 300)
        self.speed = 5  # установка скорости игрока

    # метод для перемещения игрока
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.left < 0:
                self.rect.left = 0
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.right > 800:
                self.rect.right = 800
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.rect.top < 0:
                self.rect.top = 0
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.rect.bottom > 600:
                self.rect.bottom = 600
