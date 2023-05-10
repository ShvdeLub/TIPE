

from PiicoDev_LIS3DH import PiicoDev_LIS3DH
from PiicoDev_Unified import sleep_ms # sleep

motion = PiicoDev_LIS3DH() # définit l'objet : accéléromètre

while True:
    x, y, z = motion.angle # mesure de l'angle sur les 3 axes
    print("Angle: {:.0f}°".format(y)) # affiche l'angle sur l'axe y (possible pour x et z aussi)

    a, b, c = motion.acceleration
    a = round(x,2) # arrondissement au centième
    b = round(y,2)
    c = round(z,2)
    myString = "X: " + str(a) + ", Y: " + str(b) + ", Z: " + str(a) # affichage de l'accélération sur les 3 axes
    print(myString)
    sleep_ms(50)

    # implémentation des fonctions de commande du drone en fonction des valeurs de x, y, z et a, b, c

