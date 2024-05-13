from os import system

try : import pygame
except ModuleNotFoundError :
    system("pip install pygame")

try : from random import randint
except ModuleNotFoundError :
    system("pip install random")

try : from time import sleep
except ModuleNotFoundError :
    system("pip install time")


from random import randint
from time import sleep


import pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
my_font2 = pygame.font.SysFont('Comic Sans MS', 10)
my_font3 = pygame.font.SysFont('Comic Sans MS', 15)
screen = pygame.display.set_mode([500, 500])


class Square :

    def __init__(self) -> None:
        self.vivant = True
        self.pos = [250, 350]
        self.color = [250, 250, 250]
        self.size = 20
        self.velocity = 2.1
        self.rect = [self.pos[0], self.pos[1], self.size, self.size]
    
    def update(self, keys, vivant):
        self.vivant = vivant

        if self.vivant :

            if self.pos[1] > 400 : self.pos[1] -= self.velocity
            if self.pos[1] < 250 : self.pos[1] += self.velocity

            if keys[pygame.K_LEFT] and self.pos[0] > 0 : self.pos[0] -= self.velocity
            if keys[pygame.K_RIGHT] and self.pos[0] < 500 - self.size : self.pos[0] += self.velocity
            if keys[pygame.K_UP] and self.pos[1] < 400 : self.pos[1] -= self.velocity
            if keys[pygame.K_DOWN] and self.pos[1] > 250: self.pos[1] += self.velocity
        else : self.color = [150, 0, 20]

        self.rect = [self.pos[0], self.pos[1], self.size, self.size]

    def draw(self, screen) :
        pygame.draw.rect(screen, self.color, [self.pos[0], self.pos[1], self.size, self.size])

class Road :

    def __init__(self, position):
        self.droite_gauche = randint(0, 1)
        self.position = position
        self.color = (100, 150, 150)
        self.velocity_car_line = randint(1, 3)
        self.nb_voitures = randint(3, 6)
        self.cars = [Car(randint(-80, 580), self.position+5, self.velocity_car_line, self.droite_gauche) for i in range(self.nb_voitures)]

    def update(self, keys, Player, en_vie):
        if en_vie :
            # déplace la route si le joueur avance ou recule
            if Player.pos[1] < 250:
                self.position += Player.velocity
            elif Player.pos[1] > 400 :
                self.position -= Player.velocity
        for i in self.cars : i.update(self.position+5, Player.rect)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [0, self.position, 500, 30])
        for i in self.cars : i.draw(screen)

def rect_touche(r1, r2):
    if  r1[0]-r2[2] < r2[0] < r1[0] + r1[2] and r1[1]-r2[3] < r2[1] < r1[1] + r1[3] : return True
    else : return False

class Car :
    def __init__(self, x, y, velocity, dg) -> None:
        self.droite_gauche = dg
        self.color = [randint(50, 200), randint(0, 100), randint(50, 250)]
        self.longeur = randint(40,80)
        self.rect = [x, y, self.longeur, 20]
        self.velocity = velocity
    
    def update(self, y, rec_Player) :
        self.rect[1] = y
        if self.rect[0] < 500+80 :
            self.rect[0] += self.velocity
        else :
            self.rect[0] = randint(-160, -80)
            self.longeur = randint(40,80)
            self.color = [randint(50, 200), randint(0, 100), randint(50, 250)]

    def voiture_ecrase(self, rec_Player) :
        en_vie = True
        if self.droite_gauche == 1 : self.rect[0] = -self.rect[0]+500
        if rect_touche(self.rect, rec_Player) : en_vie = False
        if self.droite_gauche == 1 : self.rect[0] = -self.rect[0]+500
        return en_vie
    
    def draw(self, screen) :
        if self.droite_gauche == 1 : self.rect[0] = -self.rect[0]+500
        pygame.draw.rect(screen, self.color, self.rect)
        if self.droite_gauche == 1 : self.rect[0] = -self.rect[0]+500

running2 = True
home_screen = True
while running2 :
    
    best_score = 0
    with open("jeux/Crossyroad/data.txt", 'a') as fic : pass
    with open("jeux/Crossyroad/data.txt", 'r') as fic :
        data = fic.readlines()

    if len(data) == 0 :
        best_score = 0
        with open("jeux/Crossyroad/data.txt", 'w') as fic :
            fic.write("0\n")
    elif len(data) == 1 :
        with open("jeux/Crossyroad/data.txt", 'a') as fic :
            fic.write("\n")

    with open("jeux/Crossyroad/data.txt", 'r') as fic :
        data = fic.readlines()
    best_score = int(data[0][0:-1])

    running = True

    while home_screen :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                running2 = False
                home_screen = False
        text_surface1 = my_font.render("CE JEU EST CODE AVEC LE C*L)", False, (0, 0, 0))
        text_surface2 = my_font.render("BIENVENUE DZNS CROSSY ROAD", False, (0, 0, 0))
        text_surface3 = my_font3.render("Synopsis :\n Vous êtes un poulet qui fuyez le kfc : courez le plus loin possible avant\nque le monsieur moustachu vous rattrape", False, (0, 0, 0))
        text_surface4 = my_font.render("ESPACE POUR COMMENCER !!!!!", False, (0, randint(0,255), 0))
        text_surface5 = my_font3.render("UTULISER les flèches pour vous déplacer", False, (0, 0, randint(0,255)))
        chaine4 = "meilleur score : " + str(best_score)
        text_surface6 = my_font3.render(chaine4, False, (0, randint(0, 255), randint(0,255)))

        
        
        pygame.draw.rect(screen, (100, randint(0, 50), randint(0, 50)), [0, 0, 500, 500])
        screen.blit(text_surface1, (-10,100))
        screen.blit(text_surface2, (10,50))
        screen.blit(text_surface3, (50,200))
        screen.blit(text_surface4, (50,300))
        screen.blit(text_surface5, (50,400))
        screen.blit(text_surface6, (50,450))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: home_screen = False
        pygame.display.flip()


    score = 0
    Player = Square()
    list_roads = [Road(50)]
    liste = ["(et les ananas)", "(et les rappeuses à fromage)", "(et les panoramas)", "(et le poulet)", "(et toi <3)", "(et Raphaël DELMAIARE)", "(et Salah)", "(et les protocoles TCP-IP)", "(et la boue)", "(et les feutres)", "(et la colle UHU)"]
    clock = pygame.time.Clock()
    vivant = True
    
    timer_parti = False
    timer = 60*3
    while running:

        if vivant == False and not(timer_parti):
            running=True
            timer_parti = True
            text_surface1 = my_font.render("J'ADORE LE POULET éCRASé", False, (0, 0, 0))
            chaine2 = "SCOo0ORE : " + str(score)
            text_surface2 = my_font.render(chaine2, False, (0, 0, 0))
            chaine3 = liste[randint(0, len(liste)-1)]
            text_surface3 = my_font2.render(chaine3, False, (0, 0, 0))
            timer -=1
            if score > int(best_score):
                with open("jeux/Crossyroad/data.txt", 'w') as fic:
                    fic.write(str(score))
                    fic.write("\n")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                running2 = False
        # upadte
        keys=pygame.key.get_pressed()
        Player.update(keys, vivant)
        for i in list_roads :
            i.update(keys, Player, vivant)
            if i.position > 750 : list_roads.remove(i)
        if list_roads[len(list_roads)-1].position > -100 :
            score += 1
            max = list_roads[len(list_roads)-1].position
            max -= 30*randint(1, 2)
            list_roads.append(Road(max))
        
        for route in list_roads :
            for car in route.cars :
                vivant = vivant and car.voiture_ecrase(Player.rect)

        # draw
        screen.fill((20, 150, 100))
        for i in list_roads : i.draw(screen)
        Player.draw(screen)
        if timer_parti :
            screen.blit(text_surface1, (100,300))
            screen.blit(text_surface3, (100,350))
            screen.blit(text_surface2, (150,400))

        pygame.display.flip()

        clock.tick(60)
        chaine = str(int(clock.get_fps())) + "FPS, " + "TARTE A L4AUTOROUTE"
        pygame.display.set_caption(chaine)
        if timer_parti : timer -= 1
        if timer < 0 : running = False
    home_screen = True

pygame.quit()
