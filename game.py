import pygame
from player import Player
from obstacle import Obstacle


class Game:
    def __init__(self):  # конструктор класса
        self.screen_width = 800  # задаем ширину экрана
        self.screen_height = 600  # задаем высоту экрана
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # создаем экран
        pygame.display.set_caption("My Game")  # задаем заголовок окна
        self.clock = pygame.time.Clock()  # создаем объект Clock
        self.running = True  # устанавливаем флаг работы игры
        self.player = Player()  # создаем объект класса Player
        self.obstacles = []

        self.obstacle1 = Obstacle(150, 200)  # создаем 1 объект класса Obstacle
        self.obstacle2 = Obstacle(550, 300)  # создаем 2 объект класса Obstacle
        self.obstacle3 = Obstacle(250, 450)  # создаем 3 объект класса Obstacle

    def run(self):
        """Метод запуска игры"""
        while self.running:  # цикл игры
            self.clock.tick(60)  # устанавливаем частоту обновления экрана
            for event in pygame.event.get():  # обработка событий
                if event.type == pygame.QUIT:  # если пользователь закрыл окно
                    self.running = False  # останавливаем игру

            self.player.move()  # перемещаем игрока
            if self.obstacle1.collides_with(self.player) or self.obstacle2.collides_with(
                    self.player) or self.obstacle3.collides_with(self.player):  # если игрок столкнулся с препятствием
                self.running = False  # останавливаем игру
                print("Game Over")  # выводим сообщение о конце игры

            self.screen.fill((255, 255, 255))  # заливаем экран белым цветом
            self.screen.blit(self.player.image, self.player.rect)  # отображаем игрока на экране
            self.screen.blit(self.obstacle1.image, self.obstacle1.rect)  # отображаем первое препятствие на экране
            self.screen.blit(self.obstacle2.image, self.obstacle2.rect)  # отображаем второе препятствие на экране
            self.screen.blit(self.obstacle3.image, self.obstacle3.rect)  # отображаем третье препятствие на экране

            pygame.display.flip()  # обновляем экран
