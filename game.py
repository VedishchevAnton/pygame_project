import pygame
from player import Player
from obstacle import Obstacle
from target import Target

import pygame
import pygame.mixer


class Game:
    def __init__(self):
        # конструктор класса
        self.screen_width = 800  # задаем ширину экрана
        self.screen_height = 600  # задаем высоту экрана
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # создаем экран
        pygame.display.set_caption("My Game")  # задаем заголовок окна
        self.clock = pygame.time.Clock()  # создаем объект Clock
        self.running = True  # устанавливаем флаг работы игры
        self.player = Player()  # создаем объект класса Player

        self.obstacle1 = Obstacle(150, 150, self.screen_width)  # создаем 1 объект класса Obstacle
        self.obstacle2 = Obstacle(550, 300, self.screen_width)  # создаем 2 объект класса Obstacle
        self.obstacle3 = Obstacle(250, 400, self.screen_width)  # создаем 3 объект класса Obstacle
        self.target = Target(400, 600, self.screen_width)  # создаем объект класса Target
        self.obstacle_speed = 2  # задаем скорость препятствий

        # Фон игры
        background_image = pygame.image.load("image/background.png")
        self.background_resized = pygame.transform.scale(background_image, (self.screen_width, self.screen_height))

        self.score = 0  # переменная для хранения количества секунд, которые игрок прожил

    @staticmethod
    def play_music():
        """Метод реализации звуковой темы игры"""
        pygame.mixer.init()
        theme_music = pygame.mixer.Sound("music/theme.mp3")
        theme_music.play(-1)

    def run(self):
        """Метод запуска игры"""
        start_ticks = pygame.time.get_ticks()  # запоминаем время начала игры
        self.play_music()  # запускаем музыку
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

            self.obstacle1.move(self.obstacle_speed)  # двигаем первое препятствие
            self.obstacle2.move(self.obstacle_speed)  # двигаем второе препятствие
            self.obstacle3.move(self.obstacle_speed)  # двигаем третье препятствие

            self.screen.blit(self.background_resized, (0, 0))  # отображаем фоновое изображение на экране
            self.screen.blit(self.player.image, self.player.rect)  # отображаем игрока на экране
            self.screen.blit(self.obstacle1.image, self.obstacle1.rect)  # отображаем первое препятствие на экране
            self.screen.blit(self.obstacle2.image, self.obstacle2.rect)  # отображаем второе препятствие на экране
            self.screen.blit(self.obstacle3.image, self.obstacle3.rect)  # отображаем третье препятствие на экране
            self.screen.blit(self.target.image, self.target.rect)  # отображаем цель игрока на экране

            # отображаем количество секунд, которые игрок прожил
            seconds = (pygame.time.get_ticks() - start_ticks) // 1000
            font = pygame.font.Font(None, 36)
            text = font.render(f"Очки: {seconds}", True, (255, 255, 255))
            self.screen.blit(text, (10, 10))

            if self.target.collides_with(self.player):
                self.running = False
                print("Вы выиграли!!!!")
                print(f'Поздравляю!!! Вы набрали {seconds} очков')

            pygame.display.flip()  # обновляем экран


