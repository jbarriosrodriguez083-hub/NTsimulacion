#simulando datos de una tabla en PYTHON

import random

def generar_ubicaciones(cantidad): 

    listaNombres=["crear ubicacion","eliminar ubicacion","actualizar ubicacion","consultar ubicacion"]

    listaCiudades=["Bogota","Medellin","Cali","Barranquilla","Cartagena"]

    listaZonas = ["Norte", "Sur", "Centro", "Oriente", "Occidente"]

    ubicaciones=[]

    for i in range(cantidad):
        ubicacion={
            "id_ubicacion": i + 1,
            "ciudad": random.choice(listaCiudades),
            "zona": random.choice(listaZonas),
            "direccion": f"Calle {random.randint(1, 100)} #{random.randint(1, 50)}-{random.randint(1, 50)}",
            "id_reporte": random.randint(1, 50)
        }
        ubicaciones.append(ubicacion)
    return ubicaciones