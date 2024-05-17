#1

from os import system, listdir

try : import random
except ModuleNotFoundError :
    system("pip install random")
import random

try : import pygame
except ModuleNotFoundError :
    system("pip install pygame")
import pygame
pygame.init()
pygame.font.init()

class Player :

    def __init__(self) -> None:
        self.velocity = 2
        self.color_j_1 = (250, 250, 10)
        self.color_j_2 = (200, 200, 10)
        self.x = 50
        self.y = 100
        self.rect = [self.x, self.y, 25, 25]
        self.vitesse = 0
    
    def draw(self, screen, jour) :
        self.rect = [self.x, self.y, 25, 25]
        if jour :
            pygame.draw.rect(screen, self.color_j_1, self.rect)
        else : 
            pygame.draw.rect(screen, self.color_j_2, self.rect)
        #pygame.draw.rect(screen, self.color_b, [self.x+15, self.y+5, 10, 15])
        #pygame.draw.rect(screen, self.color_r, [self.x+15, self.y+15, 10, 5])


class Nuage :

    def __init__(self, x) -> None:
        self.x = (x//25)*25
        self.y = random.randint(1, 3)*50
        self.w = random.randint(2, 3)*50
        self.h = random.randint(1, 3)*25
        self.color_1 = (225, 225, 255, 255)
        self.color_2 = (100, 100, 155, 255)
        self.velocity = 1
    
    def draw(self, screen, jour) :
        self.rect = [self.x, self.y, self.w, self.h]
        if jour :
            self.draw_rect_alpha(screen, self.color_1, self.rect)
        else : 
            self.draw_rect_alpha(screen, self.color_2, self.rect)

    def draw_rect_alpha(self, surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

class Tour :

    def __init__(self, x) -> None:
        self.x = x
        self.y = random.randint(0, 200)
        self.espace = random.randint(150, 300)
        
        self.color_1 = (40, 160, 60)
        self.color_2 = (60, 200, 80)
        self.color_3 = (20, 120, 40)

    def draw(self, screen, jour) :
        self.rect_1 = [self.x, 0, 50, self.y]
        self.rect_2 = [self.x, 0, 30, self.y]
        if jour :
            pygame.draw.rect(screen, self.color_1, self.rect_1)
            pygame.draw.rect(screen, self.color_2, self.rect_2)
        else : 
            pygame.draw.rect(screen, self.color_3, self.rect_1)
            pygame.draw.rect(screen, self.color_1, self.rect_2)
        
        self.rect_3 = [self.x, self.y+self.espace, 50, 500 - self.y-self.espace]
        self.rect_4 = [self.x, self.y+self.espace, 30, 500 - self.y-self.espace]
        if jour :
            pygame.draw.rect(screen, self.color_1, self.rect_3)
            pygame.draw.rect(screen, self.color_2, self.rect_4)
        else : 
            pygame.draw.rect(screen, self.color_3, self.rect_3)
            pygame.draw.rect(screen, self.color_1, self.rect_4)



police = pygame.font.SysFont('monospace', 50)
police2 = pygame.font.SysFont('monospace', 20)

title = police.render('Flappy Bird', False, (0, 0, 50))
title2 = police2.render('Espace pour lancer', False, (0, 0, 50))



clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 500])
path_data = "c:/Users/Public/SRH/jeux/Flappybird/data.txt"
last_socre = "/"
    

running = False
encours = True
while encours :

    with open(path_data, 'a') as fic : pass
    with open(path_data, 'r') as fic :
        data = fic.readlines()
    if len(data)==0 :
        with open(path_data, 'w') as fic :
            fic.write("0\n")
    with open(path_data, 'r') as fic :
        data = fic.readlines()
    best_score = data[0][0:-1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            encours = False

    

    # dessine le fond
    for i in range(50) :
        pygame.draw.rect(screen, (0, 100+(i*2), 200+(i*1)), [0, i*(500/50), 800, (500/50)])
    pygame.draw.rect(screen, (40, 160, 60), [600, 0, 100, 500])
    pygame.draw.rect(screen, (60, 200, 80), [600, 0, 60, 500])
    pygame.draw.rect(screen, (250, 250, 10), [300, 300, 50, 50])
    screen.blit(title, (85,50))
    screen.blit(title2, (85,100))

    chaine = "Dernier score : " + last_socre + " Best score : " + best_score
    title_dern_score = police2.render(chaine, False, (0, 0, 50))
    screen.blit(title_dern_score, (85, 150))


    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        running = True

    player = Player()
    liste_tours = [Tour(500+i*200) for i in range(5)]
    liste_nuages = [Nuage(i*100+random.randint(-400, 400)) for i in range(5)]

    speed_percent = 0
    score = 0
    time = 0
    jour = True

    while running :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                encours = False
        
        for nuage in liste_nuages :
            nuage.x -= nuage.velocity

        for tour in liste_tours :
            tour.x -= player.velocity
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] :
            player.vitesse = -5

        # update le joueur
        player.vitesse += 0.25
        player.y += player.vitesse
        if player.velocity < 8 :
            player.velocity += 0.0005
        if player.y > 500-25 or player.y < 0 : running = False
        if (liste_tours[0].x-25<= player.x<=liste_tours[0].x+50) and (0 <= player.y <= liste_tours[0].y):
            running = False
        if (liste_tours[0].x-25<= player.x<=liste_tours[0].x+50) and (liste_tours[0].y+liste_tours[0].espace - 25 <= player.y <= 500):
            running = False

        
        # dessine le fond
        if jour :
            for i in range(50) :
                pygame.draw.rect(screen, (0, 100+(i*2), 200+(i*1)), [0, i*(500/50), 800, (500/50)])
        else :
            for i in range(50) :
                pygame.draw.rect(screen, ((i*1.5), 0+(i*1), 55+(i*2)), [0, i*(500/50), 800, (500/50)])
        
        # dessine les nuages
        for nuage in liste_nuages :
            nuage.draw(screen, jour)
        # dessine les tours
        for tour in liste_tours :
            tour.draw(screen, jour)
        # dessine le joueur
        player.draw(screen, jour)

        # affiche le score
        speed_percent = int(100*(player.velocity-2)/6)
        chaine = str(score) # + " / Speed : " + str(speed_percent) + " %"
        if jour : 
            title_score = police2.render(chaine, False, (0, 0, 0))
            screen.blit(title_score, (20,20))
        else : 
            title_score = police2.render(chaine, False, (250, 250, 250))
            screen.blit(title_score, (20,20))

        if liste_tours[0].x < 0 - 50 :
            liste_tours.pop(0)
            liste_tours.append(Tour(liste_tours[len(liste_tours)-1].x+200))
            score += 1
        last_socre = str(score)
        
        if int(last_socre) > int(best_score) : best_score = last_socre
        with open(path_data, 'w') as fic : 
            fic.write(best_score)
            fic.write("\n")

        for nuage in range(len(liste_nuages)-1) :
            if liste_nuages[nuage].x < 0-150 :
                liste_nuages.remove(liste_nuages[nuage])
                liste_nuages.append(Nuage(random.randint(800, 1200)))

        chaine = "Flappy Bird - FPS : " + str(int(clock.get_fps()))
        pygame.display.set_caption(chaine)
        pygame.display.flip()
        clock.tick(60)
        time += 1/60
        if int((time//30)%2) == 0 : jour = True
        else : jour = False


    chaine = "Flappy Bird - FPS : " + str(int(clock.get_fps()))
    pygame.display.set_caption(chaine)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
