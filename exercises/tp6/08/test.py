from participante import Participante
from evento import Evento
from organizador import Organizador
class Test:
    @staticmethod
    def run():

        O1 = Organizador("Live Shows S.A.", "contacto@liveshows.com", "Conciertos Masivos")
        O2 = Organizador("Tech Conferences Inc.", "info@techconf.com", "Tecnología y Desarrollo")

        # Participantes
        P1 = Participante("Elena Rodríguez", "elena.r@email.com", "291-444555")
        P2 = Participante("Marcos Torres", "marcos.t@email.com", "291-666777")
        P3 = Participante("Sofía Castro", "sofia.c@email.com", "291-888999")
        P4 = Participante("Javier Morales", "javier.m@email.com", "291-000111")

        E1 = Evento("Gira Nacional de Rock", "2025-11-20", "Un evento con las mejores bandas de rock del país.")
        E2 = Evento("PyCon Anual 2025", "2025-09-05", "La conferencia de Python más grande de la región.")

        O1.asignarEvento(E1)
        O2.asignarEvento(E2)

        E1.establecerParticipantes(P1)
        E2.establecerParticipantes(P2)
        E2.establecerParticipantes(P3)
        E1.establecerParticipantes(P4)
        E1.establecerParticipantes(P1)
        E2.establecerParticipantes(P1)



if __name__ == "__main__":
    Test.run()