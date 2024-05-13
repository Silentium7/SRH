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


font = pygame.font.SysFont('monospace', 50)
font2 = pygame.font.SysFont('monospace', 25)
title = text_surface = font.render('Doodle Jump', False, (0, 0, 50))

screen = pygame.display.set_mode([500, 500])


class Plaque :

    def __init__(self) -> None:
        self.color = [50, 50, 50]
        self.rect = [random.randint(0, 450), random.randint(-1000, -10), 50, 10]
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


score_precedent = "/"

encours = True

while encours :

    with open("jeux/Doodlejump/data.txt", 'a') as fic : pass
    with open("jeux/Doodlejump/data.txt", 'r') as fic :
        data = fic.readlines()
    if len(data)==0 :
        with open("jeux/Doodlejump/data.txt", 'w') as fic :
            fic.write("0\n")
    with open("jeux/Doodlejump/data.txt", 'r') as fic :
        data = fic.readlines()
    best_score = data[0][0:-1]


    clock = pygame.time.Clock()

    x_cube = 400
    y_cube = 250
    vitesse = 10
    liste_plaques = [Plaque() for i in range(50)]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            encours = False
            running = False
    
    running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        running = True
    
    # dessine le fond
    for i in range(10):
        pygame.draw.rect(screen, (200, int(i*150/10), 0), [0, i*50, 500, 50])
    
    # titre
    screen.blit(text_surface, (85,50))
    espace = font2.render('Espace pour lancer !', False, (0, 0, 50))
    screen.blit(espace, (100,160))
    
    chaine = "Score précendent : "+score_precedent
    t1 = font2.render(chaine, False, (0, 0, 50))
    screen.blit(t1, (100,360))

    chaine = "Meilleur score : "+best_score
    t1 = font2.render(chaine, False, (0, 0, 50))
    screen.blit(t1, (120,410))

    chaine = "Doodle Jump / FPS : "+str(int(clock.get_fps()))+" / Best score = "+best_score+" / Score = "+score_precedent
    pygame.display.set_caption(chaine)
    clock.tick(60)
    pygame.display.flip()
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                encours = False
                running = False

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x_cube -= 5
        if keys[pygame.K_RIGHT]:
            x_cube += 5

        for plaque in liste_plaques :
            if vitesse < 0 :
                if plaque.rect[0]-20 < x_cube < plaque.rect[0]+plaque.rect[2] and plaque.rect[1]-20 < y_cube < plaque.rect[1]+plaque.rect[3]-20 :
                    vitesse = 10
            if plaque.rect[1] > 500 :
                liste_plaques.remove(plaque)
                if random.randint(0, 10) != 1 : liste_plaques.append(Plaque())


        if y_cube < 200 :
            for plaque in liste_plaques :
                plaque.rect[1] -= (y_cube-200)
            y_cube = 200
        

        y_cube -= vitesse
        vitesse -= 0.1

        if y_cube >= 500 : running = False

        # dessine le fond
        for i in range(10):
            pygame.draw.rect(screen, (200, int(i*150/10), 0), [0, i*50, 500, 50])
        
        for plaque in liste_plaques :
            plaque.draw(screen)

        if score_precedent != "/" and int(score_precedent) > int(best_score) :
            best_score = score_precedent
            with open("jeux/Doodlejump/data.txt", 'w') as fic:
                chaine = str(score_precedent)+"\n"
                fic.write(chaine)

        score_precedent = str(int(50 - len(liste_plaques)))

        # dessine le cube
        pygame.draw.rect(screen, (100, 100, 255), [x_cube, y_cube, 20, 20])
        clock.tick(60)
        pygame.display.flip()
        chaine = "Doodle Jump / FPS : "+str(int(clock.get_fps()))+" / Best score = "+best_score+" / Score = "+score_precedent
        pygame.display.set_caption(chaine)

pygame.quit()
