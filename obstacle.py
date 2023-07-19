import pygame


class Obstacle:
    """Класс препятствия """

    def __init__(self, x, y):
        self.image = pygame.image.load("obstacle.png")  # загружаем изображение препятствия
        self.image = pygame.transform.scale(self.image, (70, 80))  # задаем размер препятствия
        self.rect = self.image.get_rect()  # получаем прямоугольник, описывающий границы изображения
        self.rect.center = (x, y)  # устанавливаем центр прямоугольника в заданные координаты

    def collides_with(self, player):
        """Метод проверки столкновение с игроком"""
        return self.rect.colliderect(player.rect)  # возвращаем результат проверки столкновения
