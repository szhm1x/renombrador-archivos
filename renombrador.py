from pathlib import Path
from datetime import datetime
log_path = Path(__file__).parent / "logs" / "registro.txt"

class Renombrador:
    def __init__(self, ruta, prefijo):
        self.ruta = Path(ruta)
        self.prefijo = prefijo
        
    def renombrar(self):
        if not self.ruta.exists():
            print("La ruta no existe.")
            return
        log_path.parent.mkdir(exist_ok=True)
        
        
        vf2 = input("Estas Seguro? (s/n): ")
        if vf2 != "s":
            print("Saliendo del Programa....")
            return
        
        for i, archivo in enumerate(self.ruta.iterdir(), start=1):
            if archivo.is_file():
                nuevo_nombre = f"{self.prefijo}_{str(i).zfill(3)}{archivo.suffix}"
                
                archivo.rename(self.ruta/nuevo_nombre)
                
                with open(log_path, "a") as log:
                    log.write(F"{datetime.now()}: El archivo {archivo} se ha Renombrado a {nuevo_nombre} \n")

if __name__ == "__main__":
    ruta = input("Ingrese la Ruta del Directorio a Renombrar: ")
    prefijo = input("Ingrese el Prefijo para los Archivos: ")
    Renombrador(ruta, prefijo).renombrar()