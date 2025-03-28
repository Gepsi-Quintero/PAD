import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

class actividad3:
    def __init__(self, ruta_dataset=""):
        self.ruta_raiz = os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/pad/actividad_3/".format(self.ruta_raiz)
        datos = {
            "n_punto": [0,1,2,3,4,5,6,7,8,9,10,11],
            "detalle":["Crea un DataFrame frutas que luzca así","","","","","","","","","","",""],
            "resultado":[0,0,0,0,0,0,0,0,0,0,0,0],      
        }
        self.df = pd.DataFrame(datos)
        self.df["resultado"] = self.df["resultado"].astype(object) # Convertimos a tipo de object
        print(self.ruta_raiz)

        try:
            ruta_dds= "{}/archive (2)/winemag-data-130k-v2.csv".format(self.ruta_raiz)
            self.review = pd.read_csv(ruta_dds)
            print("Dataset 'Wine Reviews' cargado con exito")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ruta_dds}'")
            self.review = pd.DataFrame() # Inicializa un DataFrame vacio para evitar errores posteriores 
        except Exception as e: 
            print(f"Error al cargar el dataset: {e}")
            self.review = pd.DataFrame()        

    # Función para asegurar que la información en 'resultado' esté en formato adecuado para guardar en CSV
    def convertir_a_texto(self, obj):
        # Convierte objetos como DataFrames, Series o listas en texto
        if isinstance(obj, pd.DataFrame) or isinstance(obj, pd.Series):
            return obj.to_string(index=False)  # Convierte DataFrames y Series a texto sin los índices
        else:
            return str(obj)  # Convierte cualquier otro tipo a texto

    def punto_1(self):

        df_1 = pd.DataFrame({ # Guardamos como atributo para reutilizar
            "granadillas": [20],
            "tomates": [50]
        })
        df_1.to_csv/pad/actividad3.csv"
        self.df.loc[0, "resultado"]= entregable2/src/pad/actividad_3/punto_1.csv"
        print("punto_1") 

    def punto_2(self):

        ventas_frutas = pd.DataFrame({ 
            "Granadilla": [20, 49],
            "Tomates": [50, 100]
        }, index=["ventas_2021", "ventas_2022"])
        self.df.loc[1, "detalle"] = "Ventas de frutas"
        self.df.loc[1, "resultado"]
        ventas_frutas.to_csv(entregable2/src/pad/actividad_3/punto_2.csv")
        print("punto_2") 

    def punto_3(self):
        utensilios = pd.Series({
        'cocina': ["cuchara 3 unidades","cuchara 3 unidades"]
        })
        # self.df.loc[2,"detalle"] = "serie de utensilios"
        # self.df.loc[2,"resultado"] = self.convertir_a_texto(utensilios)
        utensilios.head().to_csv(entregable2/src/pad/actividad_3/punto_3.csv")
        print("punto_3")
        print("utensilios") 

    def punto_4(self):
        if not self.review.empty:
          # Mostrar las primeras 5 filas
            primeras_filas = self.review.head()
          # Mostrar las últimas 5 filas
            ultimas_filas = self.review.tail()
          # Concatenar las primeras y últimas filas en un solo string para mostrarlo en el DataFrame
            resultado = f"Primeras filas:\n{primeras_filas}\n\nÚltimas filas:\n{ultimas_filas}"

          # Guardar el resultado en el DataFrame
           
            self.df.loc[3, "resultado"] = self.convertir_a_texto(resultado)
            self.df.loc[3, "detalle"] = "Primeras y últimas filas del DataFrame"
          
        else:
            self.df.loc[3, "resultado"] = "Dataset no cargado"
            self.df.loc[3, "detalle"] = "Dataset no cargado"
        print("punto_4")



    def punto_5(self):
        self.df.loc[4, "resultado"] = len(self.df) + 4

    def punto_6(self):
        self.df.loc[5, "resultado"] = "punto_5.csv"

    def punto_7(self):
        self.df.loc[6, "resultado"] = len(self.df) + 6

    def punto_8(self):
        self.df.loc[7, "resultado"] = len(self.df) + 7

    def punto_9(self):
        self.df.loc[8, "resultado"] = len(self.df) + 8

    def punto_10(self):
        self.df.loc[9, "resultado"] = len(self.df) + 9

    def punto_11(self):
        self.df.loc[10, "resultado"] = len(self.df) + 10

    def punto_12(self):
        self.df.loc[11, "resultado"] = len(self.df) + 11

    def ejecutar(self):
        self.punto_1()
        self.punto_2()
        self.punto_3()
        self.punto_4()
        self.punto_5()
        self.punto_6()
        self.punto_7()
        self.punto_8()
        self.punto_9()
        self.punto_10()
        self.punto_11()
        self.punto_12()
        self.df.to_csv("actividad3.csv", index=False)
        print(self.df)

# Ejecutar el código
actividad = actividad3()
actividad.ejecutar()
        
    def punto_1(self):
        self.df.loc[0,"resultado"] = len(self.df)+0
        print("punto_1")     
    def punto_2(self):
        self.df.loc[1,"resultado"] = len(self.df)+1
        print("punto_2") 
    def punto_3(self):
        self.df.loc[2,"resultado"] = len(self.df)+2
        print("punto_3") 
    def punto_4(self):
        self.df.loc[3,"resultado"] = len(self.df)+3
        print("punto_4") 
    def punto_5(self):
        self.df.loc[4,"resultado"] = len(self.df)+4
        print("punto_5") 
    def punto_6(self):
        self.df.loc[5,"resultado"] = "punto_5.csv"
        print("punto_6") 
    def punto_7(self):
        self.df.loc[6,"resultado"] = len(self.df)+6
        print("punto_7") 
    def punto_8(self):
        self.df.loc[7,"resultado"] = len(self.df)+7
        print("punto_8") 
    def punto_9(self):
        self.df.loc[8,"resultado"] = len(self.df)+8
        print("punto_9") 
    def punto_10(self):
        
        self.df.loc[9,"resultado"] = len(self.df)+9
        print("punto_10") 
    def punto_11(self):
        self.df.loc[10,"resultado"] = len(self.df)+10
        print("punto_11") 
    def punto_12(self,num=100):
        self.df.loc[11,"resultado"] = len(self.df)+11
        print("punto_12") 
    
    def ejecutar(self):
        self.punto_1()     
        self.punto_2() 
        self.punto_3() 
        self.punto_4() 
        self.punto_5() 
        self.punto_6() 
        self.punto_7() 
        self.punto_8() 
        self.punto_9() 
        self.punto_10()
        self.punto_11()
        self.punto_12()
        self.df.to_csv("actividad3.csv")
        
act = actividad3()
act.ejecutar()
