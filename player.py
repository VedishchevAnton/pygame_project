import pygame


class Player:
    """Класс игрок"""
    def __init__(self):
        self.image = pygame.image.load("player.png")  # загрузка изображения игрока
        self.rect = self.image.get_rect()  # получение прямоугольника, описывающего изображение игрока
        self.rect.center = (400, 300)  # установка центра прямоугольника в координаты (400, 300)
        self.speed = 5  # установка скорости игрока

    # метод для перемещения игрока
    def move(self):
        """Метод для перемещения игрока"""
        # получение списка нажатых клавиш
        keys = pygame.key.get_pressed()
        # если нажата клавиша влево, переместить игрока влево
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        # если нажата клавиша вправо, переместить игрока вправо
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # если нажата клавиша вверх, переместить игрока вверх
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        # если нажата клавиша вниз, переместить игрока вниз
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
