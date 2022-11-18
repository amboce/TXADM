#!/usr/bin/env python
# coding: utf-8

# ## Mi primer proyecto
# Volvemos a encontrarnos con el conjunto de datos de pingüinos `PalmerPenguins`. Esta vez trabajaremos con ellos desde `Python`, para ello instalaremos el paquete que nos permitirá cargarlo:
# 

# In[1]:


get_ipython().system('pip install palmerpenguins')


# En segundo lugar, importaremos las librerías necesarias:

# In[3]:


import pandas as pd
from palmerpenguins import load_penguins


# Ahora ya estamos en posición de empezar a trabajar con los datos.
# 
# 1. Vamos a cargar el conjunto de datos. Muestra por pantalla el número de observaciones y sus características. Mira el tipo de datos de cada una de sus columnas.

# In[22]:


penguins = load_penguins()
print (penguins.shape)

print (penguins.columns)

print (penguins.info)

print (type(penguins))
print (type(penguins.species))
print (type(penguins.island))


# 2. Ya sabemos que este conjunto de datos tiene observaciones `NA`. Vamos a eliminarlas y a verificar que efectivamente no queda ninguno:

# In[16]:


penguins_1 = print(penguins.dropna())
print(penguins_1)

#También podemos substituir los valores NA por 0
penguins_11 = penguins.fillna(0)
print(penguins_11)


# 3. ¿Cuántos individuos hay de cada sexo? Puedes obtener la longitud media del pico según el sexo:

# In[53]:


sexo = penguins_1
mujer = penguins.loc[penguins['sex']=='female']
print ("El número de mujeres que hay es:")
print (mujer.shape[0])
hombre = penguins.loc[penguins['sex']=='male']
print ("El número de hombres que hay es")
print (hombre.shape[0])
#Longitud media según el sexo
print ("La longitud media del pico de una mujer es:")
print(mujer.bill_length_mm.mean())
print ("La longitud media del pico de un hombre es:")
print(hombre.bill_length_mm.mean())


# 4. Vamos a añadir una columna, vamos a realizar una estimación (muy grosera) del área del pico de los pingüinos (bill) tal como si esta fuese un rectángulo. Esta nueva columnas se llama `bill_area` y debe encontrarse en la última posición. Verifica que es correcto.

# In[137]:


print(penguins_1.shape[1])
penguins_2 = penguins_1.insert(loc=9,column="bill_area",value=(1,333)


# 5. Hagamos algo un poco más elaborado, vamos a realizar una agrupación en función del **sexo y de la especie de cada observación** donde obtendremos la longitud media del pico y solamente la referente al de las hembras.

# In[130]:


penguins_2 = penguins_1.groupby(['sex',"species"])
print(penguins_2.groups)
#Ahora obtenemos la longitud media del pico referente a la mujer
penguins_22 = penguins_1.groupby(['sex',"species"])['bill_length_mm'].mean()
print (penguins_22)


# 6. Como ya sabemos, la variable peso, se encuentra en gramos, la pasaremos a kg. Para ello crearemos una nueva columna llamada `body_mass_kg` y eliminaremos `body_mass_g`.

# In[63]:


print ("DataFrame after addition of new column:")
penguins_1['body_mass_kg']=penguins_1['body_mass_g']/1000
print(penguins_1)

#Eliminamos la columna body_mass_g
penguins_3= penguins_1.drop(columns=["body_mass_g"])
penguins_3



# In[ ]:




