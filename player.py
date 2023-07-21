import pygame


class Player:
    """Класс игрок"""
    def __init__(self):
        self.image = pygame.image.load("image/player.png")  # загрузка изображения игрока
        self.rect = self.image.get_rect()  # получение прямоугольника, описывающего изображение игрока
        self.rect.center = (400, 30)  # установка игрока в точку старта
        self.speed = 5  # установка скорости игрока

    # метод для перемещения игрока
    def move(self):
        # Получаем состояние клавиш на клавиатуре
        keys = pygame.key.get_pressed()
        # Если нажата клавиша влево
        if keys[pygame.K_LEFT]:
            # Перемещаем игрока влево
            self.rect.x -= self.speed
            # Если игрок вышел за левую границу экрана, то устанавливаем его координату x равной 0
            if self.rect.left < 0:
                self.rect.left = 0
        # Если нажата клавиша вправо
        if keys[pygame.K_RIGHT]:
            # Перемещаем игрока вправо
            self.rect.x += self.speed
            # Если игрок вышел за правую границу экрана, то устанавливаем его координату x равной 800
            if self.rect.right > 800:
                self.rect.right = 800
        # Если нажата клавиша вверх
        if keys[pygame.K_UP]:
            # Перемещаем игрока вверх
            self.rect.y -= self.speed
            # Если игрок вышел за верхнюю границу экрана, то устанавливаем его координату y равной 0
            if self.rect.top < 0:
                self.rect.top = 0
        # Если нажата клавиша вниз
        if keys[pygame.K_DOWN]:
            # Перемещаем игрока вниз
            self.rect.y += self.speed
            # Если игрок вышел за нижнюю границу экрана, то устанавливаем его координату y равной 600
            if self.rect.bottom > 600:
                self.rect.bottom = 600
