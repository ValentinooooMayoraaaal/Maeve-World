import pygame as pg
import sys
pg.init()

length = 700
height = 600
white = (255, 255, 255)
running = True
class Button(pg.sprite.Sprite):
    def __init__(self, x, y, height, length, color, text, font_police, font_size, font_color):
        super(Button, self).__init__()
        self.x = x
        self.y = y
        self.height = height
        self.length = length
        self.color = color
        self.text = text
        self.font_police = font_police
        self.font_size = font_size
        self.font_color = font_color
        self.font = pg.font.Font(font_police, font_size)
    def draw_button(self):
        button = pg.draw.rect(window, self.color,(self.x, self.y, self.height, self.length))

    def is_clicked(self):
        button = pg.Rect(self.x, self.y, self.height, self.length)
        if button.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("Clicked")

    def draw_font(self):
        button = pg.Rect(self.x, self.y, self.height, self.length)
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.height // 2, self.y + self.length // 2)
        window.blit(text_surface, text_rect)

#font = pg.font.Font("chemin_vers_votre_police.ttf", taille_de_la_police)
buttontest = Button(300, 250, 100, 100, (25,25,25), "Click Here !", "assets/font.ttf", 18, "white")
window = pg.display.set_mode((length, height))
window.fill(white)
pg.display.set_caption('Test_Button')

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    buttontest.draw_button()
    buttontest.is_clicked()
    buttontest.draw_font()
    pg.display.flip()