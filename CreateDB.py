import random
import pandas as pd
import numpy as np

#database columns  
columns=["Agency_Name","url","Number_of_interventions","Price_Average","Number_of_Photos","Number_of_Doctors","Experience_Years_Average","Reviews"]

#creation de la base
dataset=pd.DataFrame(columns=columns)

#remplissage de la base
for i in range(100):
    line=[]
    #NomAgence
    NomAgence="Agency_"+str(i)
    line.append(NomAgence)
    #URLAgence
    NomAgence="http://Agency_"+str(i)+".com/"
    line.append(NomAgence)
    #NombreInterventions
    nbInterventions=random.randint(20, 50)
    line.append(nbInterventions)
    #MoyennePrix
    prix=0
    for j in range(nbInterventions):
        prix+=random.randrange(500, 5000,50)
    moyennePrix=prix//nbInterventions
    line.append(moyennePrix)
    #NombrePhotosBA
    nbPhotos=random.randint(0, 50)
    line.append(nbPhotos)
    #NombreMedecins
    nbMedecins=random.randint(2, 10)
    line.append(nbMedecins)
    #MoyenneAnneesExperience
    anneeExp=0
    for j in range(nbMedecins):
        anneeExp+=random.randint(5,15)
    moyAnneeExp=anneeExp//nbMedecins
    line.append(moyAnneeExp)
    #Temoignage
    temoignage=random.randint(0, 1)
    line.append(temoignage)
    #add row to the dataset
    dataset.loc[i]=line
    
dataset.to_csv('Database.csv', encoding='UTF-8',index=False)
