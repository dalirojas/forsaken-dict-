forsaken_dict = {
                "Shedletsky": "Es un admin de roblox que creo el juego SFOTH y normalmente se le relaciona con las espadas",
                "Noob": "Personaje principal y asociado con la gente nueva",
                "C00lkidd": "exploiter de roblox de hace mucho tiempo y es la cuenta secundaria de 007n7 (ambos estan baneados)",
                "1x1x1x1":"mito de roblox que trata de un hacker",
                "John Doe":"mito de roblox que se trata de un hacker que iba a hackear todo roblox el 18 de marzo",
                "Guest1337":"Es un soldado experimentado con varios años de experiencia"
                }

personaje = input("Elije cual personaje usaras (Con mayusculas)")


if personaje in forsaken_dict.keys():
     print (forsaken_dict[personaje])
else:
     print("Ese personaje no existe")
