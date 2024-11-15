import random
import time

class Sensor:
    """Clase para simular un sensor que mide datos de calidad del aire o agua."""
    def __init__(self, tipo, umbrales):
        self.tipo = tipo
        self.umbrales = umbrales
    
    def obtener_datos(self):
        """Genera datos simulados basados en el tipo de sensor."""
        if self.tipo == "aire":
            return {
                "PM2.5": round(random.uniform(10, 80), 2),
                "CO2": round(random.uniform(300, 1500), 2)
            }
        elif self.tipo == "agua":
            return {
                "pH": round(random.uniform(6, 9), 2),
                "turbidez": round(random.uniform(1, 10), 2)
            }

    def verificar_umbrales(self, datos):
        """Verifica si algún valor supera los umbrales y devuelve alertas."""
        alertas = []
        for key, value in datos.items():
            if isinstance(self.umbrales[key], tuple):  # Umbral de rango (como pH)
                if not (self.umbrales[key][0] <= value <= self.umbrales[key][1]):
                    alertas.append(f"{key} fuera del rango: {value}")
            else:  # Umbral máximo
                if value > self.umbrales[key]:
                    alertas.append(f"{key} excede el límite: {value}")
        return alertas

class AsistentePrimerosAuxilios:
    """Clase para proporcionar instrucciones de primeros auxilios."""
    instrucciones = {
        "RCP": (
            "1. Coloca las manos una sobre otra en el centro del pecho.\n"
            "2. Comprime el pecho firmemente, 100-120 compresiones por minuto.\n"
            "3. Alterna con 2 ventilaciones cada 30 compresiones."
        ),
        "Hemorragia": (
            "1. Aplica presión directa sobre la herida con un paño limpio.\n"
            "2. Si la hemorragia no cesa, mantén la presión y busca ayuda médica.\n"
            "3. No retires el paño si está empapado de sangre; agrega más paños encima."
        ),
        "Quemadura": (
            "1. Enfría la quemadura con agua fría durante 10 minutos.\n"
            "2. Cubre con un paño limpio para evitar infecciones.\n"
            "3. No apliques hielo ni revientes ampollas."
        ),
        "Asfixia": (
            "1. Realiza la maniobra de Heimlich, colocando tus manos alrededor del abdomen.\n"
            "2. Presiona hacia adentro y hacia arriba hasta que expulse el objeto.\n"
            "3. Si es un niño, inclínalo hacia adelante y da golpes en la espalda."
        ),
    }

    def obtener_instrucciones(self, accion):
        """Devuelve instrucciones para una acción específica de primeros auxilios."""
        return self.instrucciones.get(accion, "Acción no reconocida. Intenta con: RCP, Hemorragia, Quemadura, Asfixia.")

class SistemaMonitoreo:
    """Clase principal para el monitoreo de calidad y asistencia de primeros auxilios."""
    def __init__(self):
        self.sensor_aire = Sensor("aire", {"PM2.5": 35, "CO2": 1000})
        self.sensor_agua = Sensor("agua", {"pH": (6.5, 8.5), "turbidez": 5})
        self.asistente_auxilios = AsistentePrimerosAuxilios()
    
    def monitorear(self):
        """Realiza el monitoreo de la calidad del aire y agua."""
        while True:
            # Obtener datos de calidad del aire y agua
            datos_aire = self.sensor_aire.obtener_datos()
            datos_agua = self.sensor_agua.obtener_datos()

            # Verificar alertas en aire y agua
            alertas_aire = self.sensor_aire.verificar_umbrales(datos_aire)
            alertas_agua = self.sensor_agua.verificar_umbrales(datos_agua)

            # Mostrar datos y alertas
            print("Datos de calidad del aire:", datos_aire)
            if alertas_aire:
                print("⚠️ ALERTAS de aire:", ", ".join(alertas_aire))

            print("Datos de calidad del agua:", datos_agua)
            if alertas_agua:
                print("⚠️ ALERTAS de agua:", ", ".join(alertas_agua))

            print("-" * 40)
            time.sleep(5)  # Actualización cada 5 segundos

    def primeros_auxilios(self):
        """Menú interactivo para primeros auxilios."""
        print("Bienvenido al Asistente de Primeros Auxilios")
        print("Elige una acción de emergencia: RCP, Hemorragia, Quemadura, Asfixia")
        
        while True:
            accion = input("Ingrese la acción (o 'salir' para terminar): ")
            if accion.lower() == 'salir':
                break
            instrucciones = self.asistente_auxilios.obtener_instrucciones(accion)
            print("\nInstrucciones para", accion)
            print(instrucciones)
            print("-" * 40)

# Inicialización del sistema
sistema = SistemaMonitoreo()

# Menú principal
while True:
    print("Sistema de Monitoreo y Asistencia de Emergencia")
    print("1. Monitorear Calidad del Aire y Agua")
    print("2. Asistente de Primeros Auxilios")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        sistema.monitorear()
    elif opcion == '2':
        sistema.primeros_auxilios()
    elif opcion == '3':
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")