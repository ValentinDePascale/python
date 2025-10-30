from atraccion import Atraccion
from visitante import Visitante
from entrada import Entrada
from guia_de_aventura import Guia

class Test:
    @staticmethod
    def run():
        # --- Guías de Aventura (G1, G2) ---
        G1 = Guia("Carlos", "tarde")
        G2 = Guia("Laura", "noche")

        # --- Atracciones (A1, A2, A3) ---
        A1 = Atraccion("Montaña Rusa Abismal", "Montaña Rusa", "alto", 1.40)
        A2 = Atraccion("La Mansión del Terror", "Casa embrujada", "medio", 1.20)
        A3 = Atraccion("Carrusel Mágico", "Carrusel", "bajo", 0.90)

        # --- Visitantes (V1, V2, V3) ---
        V1 = Visitante("Ana Torres", 25, 1.55, "ana.t@email.com")   # Alta
        V2 = Visitante("Leo Gómez", 10, 1.35, "leo.g@email.com")    # Estatura media
        V3 = Visitante("Sofía Cruz", 8, 1.15, "sofia.c@email.com")  # Estatura baja

        # --- Entradas (T1, T2, T3) ---
        # Cada entrada se asocia a un visitante
        T1 = Entrada(1, "2025-10-18", "Pase VIP")
        T2 = Entrada(2, "2025-10-18", "Entrada General")
        T3 = Entrada(3, "2025-10-18", "Entrada General")





        T1.asignarEntrada(V1)
        T1.asignarEntrada(V2)
        T2.asignarEntrada(V2)
        T3.asignarEntrada(V3)

        A1.establecerTurno("Tarde")
        A2.establecerTurno("Mañana")
        A1.establecerTurno("Mañana")


        G1.autorizarIngreso(V1, A1)
        G2.autorizarIngreso(V2, A3)      

        print("VISITANTES"+"-"*50)
        print(V1)  
        print(V2)           
        print(V3)           


        print("ATRACIONES"+"-"*50)
        print(A1)  
        print(A2)           
        print(A3)      

        
        print("ENTRADAS"+"-"*50)
        print(T1)  
        print(T2)           
        print(T3)   

        print("GUIAS"+"-"*50)
        print(G1)  
        print(G2)          
    

if __name__ == "__main__":
    Test.run()