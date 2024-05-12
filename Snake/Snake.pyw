from os import system

try : import pygame
except ModuleNotFoundError :
    system("pip install pygame")

try : import random
except ModuleNotFoundError :
    system("pip install random")

try : import time
except ModuleNotFoundError :
    system("pip install time")


import random
import time
import pygame
pygame.init()

ouvert = True

while ouvert :

    # meilleur_score = data[0]

    with open("jeux/Snake/data.txt", 'a') as fic : pass
    with open("jeux/Snake/data.txt", 'r') as fic :
        data = fic.readlines()

    if len(data) == 0 :
        BS = 0
        with open("jeux/Snake/data.txt", 'w') as fic :
            fic.write("0\n")
    else :
        BS = int(data[0][0:-1])

    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption("SRH - Snake")

    snake_pos = [[3,12], [4,12], [5,12]]
    snake_pos = [ [i+3, 12] for i in range(4)]
    direction = "D"

    pomme = [20, 12]

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                ouvert = False

        if ouvert : 

            screen.fill([25,200,0])
            
            keys=pygame.key.get_pressed()
            if keys[pygame.K_UP] and direction != "S": direction = "Z"
            if keys[pygame.K_DOWN] and direction != "Z": direction = "S"
            if keys[pygame.K_RIGHT] and direction != "Q": direction = "D"
            if keys[pygame.K_LEFT] and direction != "D": direction = "Q"

            if direction == "D" : 
                snake_pos.append(
                    [snake_pos[len(snake_pos)-1][0]+1,
                    snake_pos[len(snake_pos)-1][1]]
                )
                snake_pos.pop(0)
            elif direction == "S" : 
                snake_pos.append(
                    [snake_pos[len(snake_pos)-1][0],
                    snake_pos[len(snake_pos)-1][1]+1]
                )
                snake_pos.pop(0)
            elif direction == "Q" : 
                snake_pos.append(
                    [snake_pos[len(snake_pos)-1][0]-1,
                    snake_pos[len(snake_pos)-1][1]]
                )
                snake_pos.pop(0)
            elif direction == "Z" : 
                snake_pos.append(
                    [snake_pos[len(snake_pos)-1][0],
                    snake_pos[len(snake_pos)-1][1]-1]
                )
                snake_pos.pop(0)

            for i in snake_pos : 
                pygame.draw.rect(screen, (0,0,255), [i[0]*20, i[1]*20, 20, 20])
            pygame.draw.rect(screen, (255,0,0), [pomme[0]*20, pomme[1]*20, 20, 20])
        
            if not(0<=snake_pos[len(snake_pos)-1][0]<25) : running = False
            if not(0<=snake_pos[len(snake_pos)-1][1]<25) : running = False

            for a in range(len(snake_pos)) :
                for b in range(a+1, len(snake_pos)) : 
                    if snake_pos[a] == snake_pos[b] : running = False


            if len(snake_pos) > BS :
                BS = len(snake_pos)
                with open("jeux/Snake/data.txt", 'w') as fic :
                    chaine = str(BS)+"\n"
                    fic.write(chaine)
            
            for a in snake_pos:
                if a == pomme :
                    print("touché")
                    snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1]])
                    pomme = [random.randint(0, 24),random.randint(0, 24)]

            chaine = "SRH - Snake - Score : "+str(len(snake_pos))+" - Best score : " + str(BS)
            pygame.display.set_caption(chaine)
            pygame.display.flip()
            time.sleep(0.10)
    
pygame.quit()