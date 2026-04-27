import pandas as pd

from utils.simulacion_ubicaciones import  generar_ubicaciones

ubicaciones=generar_ubicaciones(5)

simulaciones_ordenadas=pd.DataFrame(ubicaciones)
print(simulaciones_ordenadas)