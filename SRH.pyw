from os import mkdir, listdir, system

try : import pygame
except ModuleNotFoundError :
    system("pip install pygame")

try : import urllib.request
except ModuleNotFoundError :
    system("pip install urllib3")

try : import time
except ModuleNotFoundError :
    system("pip install time")

try : import subprocess
except ModuleNotFoundError :
    system("pip install subprocess.run")

import subprocess
import time
import urllib.request
import pygame
pygame.init()

# actualise la liste des jeux disponibles en ligne
data_file = urllib.request.urlopen("https://raw.githubusercontent.com/Silentium7/SRH/main/data/data.txt")
data = data_file.readlines()
for i in range(len(data)): data[i] = data[i].decode("utf8")[0:-2]
data_file.close()
if not "jeux" in listdir() : mkdir("jeux")
for i in range(len(data)):
    url_image = "https://raw.githubusercontent.com/Silentium7/SRH/main/"+data[i]+"/icon.jpg"
    fichiers = listdir()
    try : 
        if not "jeux/"+data[i] in fichiers : mkdir("jeux/"+data[i])
    except FileExistsError  :pass
    fichiers = listdir("jeux/"+data[i])
    if not "icon.jpg" in fichiers :
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Silentium7/SRH/main/"+data[i]+"/icon.jpg", "jeux/"+data[i]+"/icon.jpg")
    chaine = data[i]+".pyw"
    if not chaine in fichiers :
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Silentium7/SRH/main/"+data[i]+"/"+chaine, "jeux/"+data[i]+"/"+chaine)
    




screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("RAPHUB")

Liste_jeux = data

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    for i in range(len(Liste_jeux)) :
        chaine = "jeux/"+Liste_jeux[i]+"/icon.jpg"
        picture = pygame.image.load(chaine)
        picture = pygame.transform.scale(picture, (100, 100))
        
        rect = [(i%6)*100,(i//6)*100,100,100]
        screen.blit(picture, rect)
        pos = pygame.mouse.get_pos()
        if rect[0] <= pos[0] <= rect[0]+rect[2] and rect[1] <= pos[1] <= rect[1]+rect[3] and pygame.mouse.get_pressed()[0]:
            subprocess.call(["python", "jeux/Snake/Snake.pyw"])
            time.sleep(1)


    pygame.display.flip()

pygame.quit()