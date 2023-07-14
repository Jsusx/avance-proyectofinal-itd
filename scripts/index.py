#!/usr/bin/env python
# coding: utf-8

#########
# Importamos las librerias y listamos las primeras 5 columnas
#########

# In[35]:


import pandas as pd
import matplotlib.pyplot as pit

data = pd.read_csv("/app/avance-proyectofinal-itd/data/Postulantes-2022_1.csv", sep=",", encoding='unicode_escape')

######
# Mostramos la data que vamos a utilizar
######
# In[4]:


columns = ['DEPARTAMENTO', 'PROVINCIA', 'DISTRITO', 'EDAD', 'SEXO', 'PRIMERA_OPCION', 'SEGUNDA_OPCION']
data[columns].head(5)


# In[5]:


data = data.rename(columns={ 'PRIMERA_OPCION':'PRIMERA CARRERA', 'SEGUNDA_OPCION': 'SEGUNDA CARRERA' })


# In[6]:


columns = ['DEPARTAMENTO', 'PROVINCIA', 'DISTRITO', 'EDAD', 'SEXO', 'PRIMERA CARRERA', 'SEGUNDA CARRERA']
datanueva = data[columns]
datanueva


# <h1>VERIFICANDO SI HAY DATOS NULOS</h1>

# <p>Mostrando la cantidad de datos nulos por columna</p>

# In[14]:


datanueva.isnull().sum()


# <p>Mostrando filas con datos nulos</p>

# In[18]:


datanueva[datanueva.isnull().any(axis=1)].head(20)


# <h2>Eliminando datos que estan nulos</h2>

# In[20]:


datanueva_limpia = datanueva.dropna()


# In[26]:


datanueva_limpia[datanueva_limpia.isnull().any(axis=1)].head(20)

#Como se visualiza ya no hay ningun dato nulo


# In[27]:


datanueva_limpia.info()


# <h1>Guardando datos en un archivo limpio</h1>

# In[28]:


datanueva_limpia.to_csv('/app/avance-proyectofinal-itd/data_limpia/datalimpia.csv', index=False)


# <h1>ANALISIS EXPLORATORIO DE DATOS</h1>

# <p>Utilizando group by podemos agrupar datos lo cual nos permite poder mostrar una cantidad total de la columna o dato que queramos sacar.</p>

# <p>Conoceremos la cantidad segun su sexo de postulantes que han aplicado para la carrera de sistemas</p>

# In[259]:


datanuevalimpia = pd.read_csv("/app/avance-proyectofinal-itd/data_limpia/datalimpia.csv", sep=",")


pit.figure(figsize=(16, 6))

columna1 = 'PRIMERA CARRERA'
columna2 = "SEXO"
carrera_key = "Desarrollo de Sistemas de Información"

datos = datanuevalimpia[datanuevalimpia[columna1].str.contains(carrera_key)].groupby([columna1, columna2]).size().groupby([columna2]).max()

pit.title("Grafico de la cantidad de hombres y mujeres postularon a sistemas")

pit.bar("Mujeres", datos[0])
pit.bar("Hombres", datos[1])

pit.show()


# In[258]:





# In[ ]:





# In[ ]:




