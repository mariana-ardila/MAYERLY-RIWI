print("Te encuentras en vacaciones en Roma, pero llega un reclutador de heroes,\nporque necesitaban combatir contra unos villanos que estaban poniendo en peligro la dignidad de las persona")
heroe = str(input("Hola Heroe, ¿te encuentras solo?: "))

nivel = 35
combate = ""

if heroe.lower() == "si":
    refuerzo = str(input("¿Necesitas refuerzos?: "))
    if refuerzo.lower() == "si":
        print("Perfecto, ¿a quien quieres llamar?")
        superHeroe = str(input("Elige un super heroe (Hulk, BatMan, Mujer Maravilla, otro): "))

        # Hulk
        if superHeroe.lower() == "hulk":
            nivel = nivel + 45
            print("Genial, muy buena elección")
            print("Tu nivel ha aumentado, ahora es: ", nivel)
            print("\nVas con tu compañero a McDonalds, y se encuentran a ABOMINACION, el villano más intimidante de todos los tiempos \nquien se encontraba a punto de robar una caja registradora.")
            combate1 = str(input("\n¿Deseas salvar el McDonald's?: "))
            if combate1.lower() == "si":
                print("Hulk Aplasta")
                nivel = nivel + 45
                print("Tu nivel ha aumentado: ", nivel)
            else:
                nivel = nivel - 80
                print("Tu rol como héroe ha sido derrocado, y tu nivel ha disminuido", nivel)

        # Batman
        if superHeroe.lower() == "batman":
            nivel = nivel + 30
            print("Muy bien, ahora tienes el poder del guion de tu lado")
            print("Tu nivel ha aumentado, ahora es: ", nivel)
            print("\nEstas junto a tu compañero en ciudad gótica y se encuentran al Joker haciendo de sus fechorías, haciéndole bullying a las personas.")
            combate2 = str(input("\n¿Deseas salvar a Ciudad Gótica del Joker junto a Batman y el mayordomo Alfred que siempre se encuentra detrás de Batman?: "))
            if combate2.lower() == "si":
                nivel = nivel + 30
                print("Entraron en una pelea interminable en la cual Batman decidió seguir solo. \nBatman le daba y le daba golpes mientras que el Joker solo se reía 'JAJAJAJA Batman solo eres un inútil'")
                print("Con más rabia Batman lo golpeaba, por momentos la gente pensaba que lo quería matar. \nTuvo que intervenir Alfred y Robin, que apareció de la nada para detener a Batman.")
                print("Y al detenerlo llamaron a la policía y se llevaron al Joker preso mientras se reía y Batman solo lo veía con repulsión.")
                print("\nAún así tu nivel ha aumentado", nivel)
            else:
                nivel = nivel + 10
                print("Tu como héroe no querías, pero fue más el odio de Batman hacia Joker y él se fue solo contra él", "Tu nivel ahora es:", nivel)

        # Mujer Maravilla
        if superHeroe.lower() == "mujer maravilla":
            nivel = nivel + 50
            print("Excelente, mujeres al poder")
            print("Tu nivel ha aumentado, ahora es: ", nivel)
            print("\nTe encuentras con la Mujer Maravilla en el parque explora, y te das cuenta de que un dinosaurio no era una exhibición sino que es un villano que tiene la capacidad de transformarse,\nentonces tienes que combatirlo antes de que ponga en peligro a todas las personas y destruya el parque.")
            combate3 = str(input("\n¿Deseas combatir al hombre dinosaurio y salvar el parque explora?: "))
            if combate3.lower() == "si":
                print("Mientras la mujer maravilla lo tenía amarrado con el lazo de la verdad, el héroe aprovechaba y le pegaba con su espada.")
                print("Genial, ya tenemos la cena de hoy.")
                nivel = nivel + 50
                print("Tu nivel ha aumentado: ", nivel)
            else:
                nivel = nivel - 100
                print("No mereces llamarte un héroe. Se van a morir las personas. Tu nivel ha disminuido: ", nivel)

        if superHeroe.lower() == "otro":
            otro = input("¿A qué superhéroe quieres llamar?: ")
            print("Genial ahora tu compañero es: ", otro)
            nivel = nivel + 35
            print("Ahora tu nivel es", nivel)
            print(f"Estás junto a {otro} y se encuentran con Lex Luthor, el cual desea acabar con la ciudad de Misisipi.")
            combate4 = str(input("¿Deseas combatirlo?"))
            if combate4.lower() == "si":
                print("Tienen una pelea estratosférica, todos los presentes quedan anodadados por semejante matanza que hicieron tú y ", otro)
                nivel = nivel + 45
                print("Vuestro nivel ha aumentado", nivel)
            else:
                nivel = nivel - 34
                print("Te faltaron cojones, por pelotudos vuestro nivel bajó, ahora es", nivel)

    else:
        print("Wow, eres un héroe muy valiente y fuerte")
        nivel = nivel + 200
        print("Eres capaz de combatir a los villanos tu solo, pero puedes quedar muy herido y hasta morir")
        print("Tu nivel ha super aumentado:", nivel)

else:
    print("Dios está contigo, tienes el poder absoluto y nadie puede contra ti")
    nivel = str("∞")
    print("Tu nivel es: ", nivel)
