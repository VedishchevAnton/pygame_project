import pygame


class Obstacle:
    """Класс препятствия"""

    def __init__(self, x, y, screen_width):
        self.image = pygame.image.load("image/obstacle.png")  # загружаем изображение препятствия
        self.image = pygame.transform.scale(self.image, (70, 80))  # задаем размер препятствия
        self.rect = self.image.get_rect()  # получаем прямоугольник, описывающий границы изображения
        self.rect.center = (x, y)  # устанавливаем центр прямоугольника в заданные координаты
        self.screen_width = screen_width  # добавляем атрибут ширины экрана
        self.direction = 1  # добавляем атрибут направления движения

    def collides_with(self, player):
        """Метод проверки столкновение с игроком"""
        return self.rect.colliderect(player.rect)  # возвращаем результат проверки столкновения

    def move(self, speed):
        """Метод движения препятствия"""
        self.rect.x += speed * self.direction  # изменяем координату x с учетом направления движения
        if self.rect.right >= self.screen_width:  # если достигли правого края экрана
            self.direction = -1  # меняем направление движения на обратное
        elif self.rect.left <= 0:  # если достигли левого края экрана
            self.direction = 1  # меняем направление движения на обратное
