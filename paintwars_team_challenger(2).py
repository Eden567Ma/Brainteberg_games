
import random

def get_team_name():
    return "0 inspi" # à compléter (comme vous voulez)

def step(robotId, sensors):
        
    comportement = 0

    #Variable indiquant s'il y a un membre de son équipe vers l'avant
    ami_devant = sensors["sensor_front"]["isSameTeam"] or sensors["sensor_front_left"]["isSameTeam"] or sensors["sensor_front_right"]["isSameTeam"] or sensors["sensor_left"]["isSameTeam"] or sensors["sensor_right"]["isSameTeam"]
    
    #Variable indiquant s'il y a un ennemi vers l'avant
    ennemi_devant = (sensors["sensor_front"]["isRobot"] and not sensors["sensor_front"]["isSameTeam"]) or (sensors["sensor_front_left"]["isRobot"] and not sensors["sensor_front_left"]["isSameTeam"]) or (sensors["sensor_front_right"]["isRobot"] and not sensors["sensor_front_right"]["isSameTeam"]) or (sensors["sensor_left"]["isRobot"] and not sensors["sensor_left"]["isSameTeam"]) or (sensors["sensor_right"]["isRobot"] and not sensors["sensor_right"]["isSameTeam"])
    
    #Variable indiquant s'il y a un mur en face (risque d'être bloqué)
    mur_droit_devant = (not sensors["sensor_front"]["isRobot"] and sensors["sensor_front"]["distance"]<1)
    #mur_droit_devant = (not sensors["sensor_front"]["isRobot"] and sensors["sensor_front"]["distance"]<1) and (not sensors["sensor_front_left"]["isRobot"] and sensors["sensor_front_left"]["distance"]<1)==(not sensors["sensor_front_right"]["isRobot"] and sensors["sensor_front_right"]["distance"]<1)
    
    #Variable indiquant s'il y a des obstacles devant et sur les côtés (risque d'être bloqué)
    partout_devant = sensors["sensor_front"]["distance"]<1 and sensors["sensor_left"]["distance"]<1 and sensors["sensor_right"]["distance"]<1
	
	#Variable indiquant s'il y a un mur vers l'avant
    mur_devant = mur_droit_devant or (not sensors["sensor_front_left"]["isRobot"] and sensors["sensor_front_left"]["distance"]<1) or (not sensors["sensor_front_right"]["isRobot"] and sensors["sensor_front_right"]["distance"]<1) or (not sensors["sensor_left"]["isRobot"] and sensors["sensor_left"]["distance"]<1) or (not sensors["sensor_right"]["isRobot"] and sensors["sensor_right"]["distance"]<1)
	
    if comportement==0:
        if partout_devant: #Pour ne pas se retrouver bloqué dans un cul de sac
            #Rotation aléatoire extrême et freinage total
            translation = 0
            rotation = random.randint(0,1)*2 - 1
            
        elif ami_devant: #Pour ne pas se bloquer contre un allié ou repasser derrière lui
            #Hate bot (Braitenberg)
            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = 0.1 -1 * sensors["sensor_front_left"]["distance"] + 1 * sensors["sensor_front_right"]["distance"] -1 * sensors["sensor_left"]["distance"] + 1 * sensors["sensor_right"]["distance"]
            
        elif ennemi_devant: #Pour gêner les adversaires en les bloquant ou en repeignant derrière eux
            #Love bot (Braitenberg)
            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = 1 * sensors["sensor_front_left"]["distance"] - 1 * sensors["sensor_front_right"]["distance"] + 0.5 * sensors["sensor_left"]["distance"] - 0.5 * sensors["sensor_right"]["distance"]
            
        elif mur_droit_devant: #Pour se débloquer facilement si un mur se trouve droit devant
            #Rotation aléatoire extrême et freinage total
            translation = 0
            rotation = random.randint(0,1)*2 - 1
            
        elif mur_devant: #Pour éviter les murs si besoin
            #Hate wall (Braitenberg)
            translation = 1 * sensors["sensor_front"]["distance"]
            rotation = -1 * sensors["sensor_front_left"]["distance"] + 1 * sensors["sensor_front_right"]["distance"] -1 * sensors["sensor_left"]["distance"] + 1 * sensors["sensor_right"]["distance"]
            
        else: #Comportement "par défaut" qaund il n'y a pas d'obstacles
            #Rotation aléatoire légère tout en avançant (exploration)
            maxi_rota = 0.2
            translation = 1
            rotation = 2*maxi_rota*(random.random() - 0.5)
            
    

    return translation, rotation
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
