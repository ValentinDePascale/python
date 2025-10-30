from participante import Participante
from disciplina import Disciplina

class Test:
    @staticmethod
    def run():
        Disciplina1 = Disciplina("Carrera 100 metros", "Los particiantes deben correr 100 metros rectos, el primero que llega gana")
        Disciplina2 = Disciplina("Salto en alto", "Los participantes deben saltar lo mas lejos que puedan")

        P1 = Participante("Juan Perez", 18, "Argentina")
        P2 = Participante("Emilia Martinez", 23, "Chile")
        P3 = Participante("Emilio Rodriguez", 19, "Paraguay")
        P4 = Participante("Maria Gomez", 20, "Uruguay")

        print("-"*50)
        print(P1)
        print(P2)
        print(P3)
        print(P3)
        
        print("-"*50)
        print(Disciplina1)
        print(Disciplina2)



        P1.establecerDisciplina(Disciplina1)
        P2.establecerDisciplina(Disciplina2)
        P3.establecerDisciplina(Disciplina1)
        P4.establecerDisciplina(Disciplina1)
        P1.establecerDisciplina(Disciplina2)

        print("-"*50)
        print(P1)
        print(P2)
        print(P3)
        print(P4)

        print("-"*50)
        print(Disciplina1)
        print(Disciplina2)

if __name__ == "__main__":
    Test.run()