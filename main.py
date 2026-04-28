import pandas as pd

from utils.simulacion_ubicaciones import  generar_ubicaciones

from notebook.limpieza_ubicaciones import limpiar_simulaciones

ubicaciones=generar_ubicaciones(10)

simulaciones_ordenadas=pd.DataFrame(ubicaciones)

simulaciones_ordenadas=limpiar_simulaciones(simulaciones_ordenadas)
print(simulaciones_ordenadas)