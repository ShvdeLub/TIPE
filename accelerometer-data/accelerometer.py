
from djitellopy import Tello
from PiicoDev_LIS3DH import PiicoDev_LIS3DH
from PiicoDev_Unified import sleep_ms # sleep

motion = PiicoDev_LIS3DH() # définit l'objet : accéléromètre

tello = Tello() # définit l'objet : drone

valeur_etat = [False, False, False, False, False, False, False, False] 
# liste des états de chaque variable de déplacement
# dans l'ordre : x +, x -, z +, z -, y +, y -, rot z trigo, rot z horaire  

def move_x(az, z):
    """
    Entrée : 
    - z : valeur de l'accélération sur l'axe z
    az : valeur absolue de z
    Pré-condition : az vérifie la condition du seuil
    """
    if z == az:
        tello.move_forward(0) # 10 centimètres d'avancée
        valeur_etat[0] = False       
    else:
        tello.move_forward(10)
        valeur_etat[0] = True

def move_y(ay, y):
    """
    Entrée : 
    - y : valeur de l'accélération sur l'axe y, flottant
    - ay : valeur absolue de y, flottant
    Pré-condition : ay vérifie la condition du seuil
    """
    if valeur_etat[4] == False and y == ay:
        tello.move_left(5)
        valeur_etat[4] = True

    if valeur_etat[5] == False and y != ay:
        tello.move_right(5)
        valeur_etat[5] = True

    if valeur_etat[4] == True and y != ay:
        tello.move_left(0)
        valeur_etat[4] = False
        
    if valeur_etat[5] == True and y == ay:
        tello.move_right(0)
        valeur_etat[5] = False

while True:
    x, y, z = motion.angle # mesure de l'angle sur les 3 axes
    x , y, z= round(x, 2), round(y, 2), round(z, 2)
    ax, ay, az = abs(x), abs(y), abs(z) # valeur absolue de chaque donnée

    l, m, n = motion.acceleration
    l, m, n = round(l,2), round(m,2), round(n,2)
    # implémentation des fonctions de commande du drone en fonction
    #  des valeurs de x, y, z et l, m, n
    if az >= 1: # 1 représente ici le seuil de déclenchement en m/s^-2
        move_x(az, z)
    
    if ay >= 1:
        move_y(ay, y)


    sleep_ms(50)
