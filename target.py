import pygame


class Target:
    """Класс препятствия"""

    def __init__(self, x, y, screen_width):
        self.image = pygame.image.load("image/target.png")  # загружаем изображение цели
        self.image = pygame.transform.scale(self.image, (70, 80))  # задаем размер цели
        self.rect = self.image.get_rect()  # получаем прямоугольник, описывающий границы изображения
        self.rect.center = (400, 560)  # устанавливаем центр прямоугольника в заданные координаты
        self.screen_width = screen_width  # добавляем атрибут ширины экрана

    def collides_with(self, player):
        """Метод проверки столкновение с игроком"""
        return self.rect.colliderect(player.rect)  # возвращаем результат проверки столкновения
