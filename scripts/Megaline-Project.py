
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
print("El proposito del siguiente proyecto, consiste en la optimizacion del presupuesto para generar una publicidad que se enfoque en los planes de servicio que genera mayor cantidad de ingresos para la empresa.")

print()

print("Observamos la informacion  general de los datos proporcionados por nuestra muestra representattiva")

print()


print("Inicialización")

print()


print("Cargar datos")


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

megaline_calls = pd.read_csv(os.path.join(DATA_DIR, "megaline_calls.csv"))
megaline_messages = pd.read_csv(
    os.path.join(DATA_DIR, "megaline_messages.csv"))
megaline_internet = pd.read_csv(
    os.path.join(DATA_DIR, "megaline_internet.csv"))
megaline_plans = pd.read_csv(os.path.join(DATA_DIR, "megaline_plans.csv"))
megaline_users = pd.read_csv(os.path.join(DATA_DIR, "megaline_users.csv"))

print("Preparar los datos")

print()


print(megaline_calls.head())

print()

print(megaline_internet.head())

print()


print(megaline_messages.head())

print()

print(megaline_plans.head())

print()

print(megaline_users.head())

print()

print("La informacion se obserba bien en primera instancia se . Sin embargo es siempre importante realizar un preprocesamiento para verficar que nuestros valores sean confiables")

print("Tarifas")

print()

print(megaline_plans.info())

print()

print(megaline_plans.sample(2))

print("Este DataFrame maneja unicamente 2 columnas representativas en las cuales nos vamos a basar para llegar a conclusiones mas concretas")

print()

print("el trafico de internet es medido en Gigabytes usados pero son contados en megabytes utilizados, para solucionar esto realizaremos un transformacion en el la tabla  qeu mide el trafico de internet.")

print()

megaline_internet['gb_used'] = megaline_internet['mb_used']/1024
print(megaline_internet.head())

print()

print("Verificamos valores usentes y duplicados en nuestra tabla de tarifas")

megaline_plans.isna().sum()

print(" Es bastante obvio que no vamos encontrar valores ausentes en esta tabla ya que contiene los terminos y las tarifas de cada uno de los planes")

print()

print(megaline_plans.duplicated())

print()

print(megaline_plans.describe())

print()

print("No hemos encontrado valores ausentes o duplicados en este DataFrame, podria puede ser normal que los valores que se nos presentan en la descripcion de los datos vallan de forma decsendente")

print()

print("Vamos a conservar los valores de las tarifas y los planes de este conjunto de datos, Mas que nada para que nuestros datos no presenten resultados atipicos mas adelante")

print()

print("Imprime la información general/resumida sobre el DataFrame de usuarios")

print()

print(megaline_users.info())

print()

print(megaline_users.sample(10))

megaline_users.sample(10).isna().sum()

print()

print(megaline_users.sample(10).describe())

print()

print("Observamos valores ausentes en la columna de fecha de abandono, y si los  hay significa que aun siguen con su plan, son clientes que siguen comprando planes de megaline y sobre los que podemos trabajar ya que continuan con el servicio")

print()

print("En este apartado vamos a denotar los valores que tienen una fecha de abandono de su plan sobre los cuales no vamos a poder trabajar ya que cacelaron o abandonaron su plan de servicio previamente")


print(megaline_users.sample(10).isna().count())

print()

print("De esta manera en nuestra muestra podemos observar la cantidad de usurios que no manejan su plan activo, ya que el conteo se realiza unicamnete para los valores no ausentes, y si estos presentan una fecha. significa que hasta entonces  estuvienron manteniendo su plan.")

print()

print()

print("El atributo mes de la lista de usuarios, no corresponde al mes de los servicios y ya que  el objetivo es poder relacionarla con la tabla que contiene los terminos para cada uno de los planes en especifico, no extraeremos el atributo month de la tabla de usuarios.")

print()

print(megaline_users.head())

print()

print("Obtenemos el mes de esta tabla de usuarios y la agregamos como columna a nuestro DataFrame")

print()

print("Se imprime la información general/resumida sobre el DataFrame de las llamadas")

print()

print("megaline_calls.info()")

print()


print(megaline_calls.sample(10))

print()

print()

print(megaline_calls.sample(10).isna().sum())

print()

print(megaline_calls.sample(10).duplicated().sum())

print()

print("tenemos datos de tipos enteros de tipos objetos de puntos de coma flotante, en esta tabla ya que representa la cantidad, duracion fecha y fecha de adquicision del plan de llamadas para cada uno de los usuarios.")

print()

print(" Despues de revisar la suma delos datos duplicados y ausentes, observamos que tenemos por el momento en orden los datos de la tabla de llamadas.")

print()

print(megaline_calls.sample(10).describe())

print()

print("Tenemos buenos conteos y buenas medias, podemos notar tambien que los valores maximos aluden mas a los usuarios  que en la duracion asi que podriamos encontrarnos mas adelante con valores atipicos en esta columna.")

print("Transformamos y obetnemos el los mese que cada usuario ha mantedido su plan de servicios activo, para poder realcionarlo en con la tabla que contiene las tarifas para cada mes de uso de cada plan.")

print()

megaline_calls['call_date'] = pd.to_datetime(
    megaline_calls['call_date'], format='%Y-%m-%d')

megaline_calls['month'] = megaline_calls['call_date'].dt.month

print(megaline_calls.head())

print(" Una vez que extraemos el mes del plan de llamadas, notamos que la duracion de estas, esta compuesta por minutos y segundos de duracion.")

print()

megaline_calls['duration_v2'] = megaline_calls['duration']
megaline_calls['duration_v2'] = np.ceil(megaline_calls['duration'])
print(megaline_calls.head())

print(" De esta manera tenemos una vision mas acorde al plan de minutos de llamada de cada uno de los usuarios y podremos verificar de manera mas eficaz")

print()

print("Se Imprime la información general/resumida sobre el DataFrame de los mensajes")
print()

print(megaline_messages.info())

print()

print(megaline_messages.sample(10))

print()

print(megaline_messages.sample(10).isna().sum())

print()

print(megaline_messages.isna().sum())

print()

print(megaline_messages.sample(10).duplicated().sum())

print()

megaline_messages.duplicated().sum()

print("Tanto en la muestra como en la tabla de los valores completos de nuestros datos.")

print()

print("Para finalizar realizamos una descripcion general de la muestra y tambien de nustra tabla de datos completa para verificar si notamos alguna incontingecia")

print()

print(megaline_messages.sample(10).describe())

print()

print(megaline_messages.describe())


print("Notamos diferencias obvias en las descripciones de cada una de las tablas, es normal encontrarnos con valores mas elevados en el la tabla copleta que en la mustra, debido a que manejamos mayor cantidad de datos en la tabla general.")

print()

print("Transformamos y obetenemos el el mes de uso de los mensajes de cada usuario. Esto nos sera util al para que sea muhcho mas facil al mometnto de relacionarla con al resto de tablas.")

print()

megaline_messages['message_date'] = pd.to_datetime(
    megaline_messages['message_date'], format='%Y-%m-%d')

megaline_messages['month'] = megaline_messages['message_date'].dt.month

print(megaline_messages.head())

print()

print("Internet")

print()

print(megaline_internet.info())

print()

print(megaline_internet.sample(10))

print("Tenemos columnas de datos de tipos punto de coma flotante y enteros en su mayoria debemos realizar algunas transformaciones para poder trabajar de mejor manera")

print()

print("Verificamos valores ausentes o duplicados")

print()

print(megaline_internet.sample(10).isna().sum())

megaline_internet.isna().sum()

print()

print(megaline_internet.sample(10).duplicated().sum())

print()

print(megaline_internet.duplicated().sum())

print()

print("Al no encontrar valores ausentes o duplicados ni en la muestra ni en nuestra poblacion de datos completa, solo nos resta realizar una descripcion general de nustras datos para nuestro plan de internet.")

print()

print(megaline_internet.describe())

print()

print("Tenemos buenas metricas para cada una de nustras columnas tenemos buenas metricas, mas adelnate encontraremos valores atipicos esi es que los hay en nuestro grupo de  datos para el plan de internet.")

print()

print("Realizamos las transformaciones pertinentes para los tipos de datos que manejamos.")

print()

megaline_internet['session_date'] = pd.to_datetime(
    megaline_internet['session_date'], format='%Y-%m-%d')

megaline_internet['month'] = megaline_internet['session_date'].dt.month

print(megaline_internet.head())

print()

print("Algo importante a considerar en este paquete es que, segun el plan de internet de el dataframe que tiene las tarifas.")

print()

megaline_internet['gb_used'] = megaline_internet['mb_used']/1024
print(megaline_internet.head())

print()

print("Asi podremos estudiar la columna de gigabytes utilizados en el DataFrame de una manera mas precisa, en el posible caso que tengamos relacionarla con el DataFrame que contiene las tarifas de cada plan.")

print()

print("Es sumamente importante entender cómo funcionan las tarifas, cómo se les cobra a los usuarios en función de su plan de suscripción. Así vamos imprimir la información de la tarifa para ver una vez más sus condiciones.")

print()

print(megaline_plans.info())

print()

print("Ahora que hemos limpiado nustros datos, vamos a agregar los datos por usuario y por periodo para que solo haya un registro por usuario y por periodo. Esto facilitará mucho el análisis posterior")

print()


montly_calls_total = (
    megaline_calls
    .groupby(['user_id', 'month'])['duration_v2']
    .sum()
    .reset_index()
    .rename(columns={'duration_v2': 'call_minutes'})
)
montly_calls_minutes = (
    megaline_calls
    .groupby(['user_id', 'month'])['duration_v2']
    .count()
    .reset_index()
    .rename(columns={'duration_v2': 'total_calls'})
)

print((montly_calls_minutes.head()))
print((montly_calls_total.head()))

print()

print("Al obetner el tiempo en minutos y la cantidad de llamadas realizadas por cada uno de los usuarios. Renombramos dichas columnas para que se puedan diferenciar de mejor manera, y poder trabajar con ellas de manera mas eficaz.")

print()

total_calls = montly_calls_minutes.merge(
    montly_calls_total, on=['user_id', 'month'])
print(total_calls.head())

print()

print("Juntamos las dos tablas para tener una vision mas generalizada  de las llamadas que realizo cada usuario y cuantos minutos de duracion tiene cada una de estas, nos servira para obserbar mas a delante de mejor manera.")

print()

montly_messages = megaline_messages.groupby(['user_id', 'month'])[
    'id'].count().reset_index()
print(montly_messages.head())

print()

print(
    "Realizamos una agrupacion de los mensajes por ususario y el mes para denotar la cantidad de llamadas que hizo cada cliente en cada mes donde [id] representa la cantidad de llamdas realizadas, y [month] el mes en el que realizo cada una de ellas")

# %%
montly_internet = np.ceil(megaline_internet.groupby(
    ['user_id', 'month'])['gb_used'].sum().reset_index())
print(montly_internet.head())

print()

print("Juntamos los datos agregados en un DataFrame para que haya un registro que represente lo que consumió un usuario único en un mes determinado.")

print()

total_information = total_calls.merge(
    montly_messages, on=['user_id', 'month'], how='outer')
total_information = total_information.merge(
    montly_internet, on=['user_id', 'month'], how='outer')
total_information = total_information.merge(
    megaline_users, on=['user_id'], how='outer')
total_information = total_information.fillna(0)
print(total_information.head(2))

print()

print("De esta manera obtenemos una tabla que contiene la informacion mas precisa y a corde con lo que cada uno de los planes de megaline, nos solicita.")

print()

print("Luego  le unimos la informacion de de los planes de manera meticulosa. Para poder trabajar con una tabla mas general, precisa y limpia")

print()

total_information = total_information.merge(
    megaline_plans, left_on='plan', right_on='plan_name')
print(total_information.head(2))

print()

print("Unimos la informacion del plan a nuestro dataframe general para poder trabajar a partir de un solo dataframe")

print()

print("Vamos a realizar los calculos necesarios para facturar cada uno de los mensajes que superaron el numero de mensajes que contiene el plan que contrato cada usuario.")

print()

print(total_information.head(2))

print()

print(
    "Partimos desde nuestra tabla de datos general [total_information], que contiene la informacion completa de cada uno de los susuarios y tambien de los planes con sus respectivas tarifas.")

print()

extra_messages = total_information['id'] - \
    total_information['messages_included']
extra_messages = extra_messages.fillna(0)

extra_messages = [0 if x < 0 else x for x in extra_messages]
extra_messages = pd.Series(extra_messages)
total_information['extra_messages'] = extra_messages * \
    total_information['usd_per_message']
print(total_information.query('extra_messages > 0').head())

print()

print()

print("Realizamos el calculo respectivo para despues mostrar nuestra columna que factura los mensajes de cada usuario que excedio el cupo en su respectivo plan.")

print()

print("Generada nuestra columna de facturacion en los mensages extra de cada uno de los planes para cada usuario, notamos que los usuarios de plan Ultimate tienen menos mesages excedidos en su plan a comparacion los  mensajes exedidos del plan surf que son mayores.")

print()

print()

print(
    "Ahora vamos a generar nustras graficas para los servicios de mensajes de cada uno de los planes, y de la misma forma empeamos con un diagrama de barras. Empezamos agrupando nusto Dataframe por el mes el plan y obenemos la mediana de ['id'], que es la columna que muestra la cantidad de mensajes enviados pora cada usuario emn su respectivo plan.")

print()

print(total_information.columns)

print()

print("Exponemos las columnas de nuestra tabla general para realizar el agrupamiento correspondiente y realizar nuestra grafica.")

print()

df_1 = total_information.groupby(['month', 'plan'])['id'].mean().reset_index()
print(df_1.head())

print()

grafik_p1 = df_1.pivot(index='month', columns='plan', values='id')

print(grafik_p1.plot(kind='bar'))

print()

print("En este grafico observamos una mayor cantidad de mensajes enviados por los uaurios del plan Ultimated, pero tambien hay que tomar en cueta que este plan tienen  menor cantidad de usuarios que el plan Surf,asi que quizas  un grafico de porporcion, asi que un histograma puede resultar en una vision diferente.")

print()

df1_2 = total_information.pivot(
    index=['user_id', 'month'], columns='plan', values='id')
print(df1_2.head())

print()

print(df1_2.hist())

print()

print("Esta proporcion es muy clara, y nos indica casi la misma informacion del grafico de barras sin embargo a pesar que el plan Surf tiene mayor cantidad de usuarios que el plan Ultimated")

print()

df1_2 = total_information.pivot(index='user_id', columns='month', values='id')

print(df1_2.boxplot())

print()

print("El grafico de caja es mas especifico para mostarnos los pocos usuarios que han excedido por mucha diferencia el cupo de sus mensajes en el plan que manejan.")

print()

extra_gb = total_information['gb_used'] - \
    total_information['mb_per_month_included']/1024
extra_gb = extra_gb.fillna(0)

extra_gb = [0 if x < 0 else x for x in extra_gb]
extra_gb = pd.Series(extra_gb)
total_information['extra_gb'] = extra_gb * total_information['usd_per_gb']
print(total_information.query('extra_gb > 0').head())

print("Ahora hemos creado una columna que facture el trafico de internet utilizado por cada uno de los usuarios que ha excedido los giabytes que contenia su plan.")

print()

print("Tambien puede ser conveniente realizar graficas sobre el trafico de internet durante los meses de uso de cada uno de los clientes, para tener una vision mas espesifica sobre este servicio en el plan de cada usuario.")

print(total_information.columns)

print("Exponemos las columnas de nuestra tabla general para realizar el agrupamiento correspondiente y realizar nuestra grafica.")

print()

df_2 = total_information.groupby(['month', 'plan'])[
    'gb_used'].mean().reset_index()
print(df_2.head())

print()

grafik_p2 = df_2.pivot(index='month', columns='plan', values='gb_used')
print(grafik_p2.plot(kind='bar'))

print("En este aspecto, observamos que el plan Ultimated tiene mas trafico de internet utilizado que el plan surf, sin emargo tambien debemos tomar en cuenta que este plan tiene menor cantidad de usuarios que el plan Surf,")

print()

df2_1 = total_information.pivot(
    index=['user_id', 'month'], columns='plan', values='gb_used')
print((df2_1.head()))

print(df2_1.hist())

print("La proporcion de el trafico de internet, muestra un amyor uso para los usuarios que han contratado el plan Surf, aunque tambien tenemos valoes ausentes en el plan Utimated, puede que un drafico de caja nos pueda dar una vision mas especifica de el trafico de internet en los usuarios de cada plan.")

print()

df2_2 = total_information.groupby(['month', 'plan'])[
    'gb_used'].mean().reset_index()
print(df2_2.head())

print()

df2_3 = total_information.pivot(
    index='user_id', columns='month', values='gb_used')

print(df2_3.boxplot())

print()

print("Ya con nuestro diagrama de caja observamos que los bigotes se acercan mucho en el ultimo mes a los valores maximos.")

print("De esta manera tendremos toda la informacion de manera mas detallada graficada de cada uno de estos 2 servicos. Solo nos falta calular el servicio de minutos y exponerlos con sus respectivas graficas.")

print("Luego realizamos el mismo proceso para calcular las llamadas que exeden la cantidad de minutos incluidos en cada uno de los planes.")

print()

extra_clls = total_information['call_minutes'] - \
    total_information['minutes_included']
extra_clls
extra_clls = [0 if x < 0 else x for x in extra_clls]
extra_clls = pd.Series(extra_clls)
total_information['extra_clls'] = extra_clls * \
    total_information['usd_per_minute']
print(total_information.query('extra_clls > 0').head(2))

print("Antes de mostrar como va quedando nuestra tabla con las columnas agregadas.Estamos haciendo una especificasion en los usuarios que si ecxedieron su total de minutos de llamada para comprobar que se este facturando el valor por minuto extra del plan que corresponde.")

print(total_information.columns)

print()

print("Exponemos las columnas de nuestra tabla general para realizar el agrupamiento correspondiente y realizar nuestra grafica.")

print()

df_3 = total_information.groupby(['month', 'plan'])[
    'call_minutes'].mean().reset_index()
print(df_3.head())

print()

print("Exponemos en primera instancia el dataframe bajo el cual basaremos el grafico de barras.El obejetivo es que este mismo, contenga la duracion de llamadas por cada plan y por cada mes.")

print()

grafik_p3 = df_3.pivot(index='month', columns='plan',
                       values='call_minutes')
print(grafik_p3.plot(kind='bar'))

print()

print("Las barras nos muestran cierta inclinacion y supremacia por el numero de llamadas en el plan surf, superando al plan ultimate en 7 de los 12 meses del año 2018. Sin embargo no hay que descartar que el plan ultimate aun con menor cantidad de usuarios, supero en 5 meses al plan surf,  y en los ultimos de destaco por mucho.")

print()

print("Comparemos y visualisemos el número de minutos mensuales que necesitan los usuarios de cada plan,atravez de  un histograma.")

print()

df3_2 = total_information.pivot(
    index=['user_id', 'month'], columns='plan', values='call_minutes')
print((df3_2.head()))

print()

print("De la misma manera, creamos una tabla que muestre todos los datos que queremos visualizar en nuestro histograma.")

print()

print(df3_2.hist())

print()

print("Aunque los graficos parecen ser similares, la cantidad de datos en nuestros ejes demuestra una mayopr cantiadad en el umero de usuarios y minutos que ocupan las llamadas en el plan surf, a comparacion con el plan ultimate.")

print()

print("Una vez realizado los graficos podremos visualizar los datos de cada plan de mejor manera, ahora calcularemos la media y la varianza de la duración mensual de llamadas.")

print()

print(total_calls.mean())
print(np.var(total_calls))

print()

print("Tenemos buenas medias y una desviasion estandar bastante interesante y a tomar mucho en cuenta en nuestra tabla de datos, que refleja las llamadas totales.")

print()

print(total_calls.head())

print()

print("Para tener un panorama mas general y comprensible de esta tabla, trazaremos  un diagrama de caja para visualizar la distribución de la duración mensual de llamadas.")

print()

df3_3 = total_calls.groupby(['month', 'total_calls'])[
    'call_minutes'].mean().reset_index()
print(df3_3.head())

print()

print("Mostramos nuestra tabla agrupada con los datos que queremos denotar en nuestro grafico de caja. Para despues realizar una tabla dinamica con los valores que queremos darle al mismo.")

print()

df3_3 = total_calls.pivot(
    index='user_id', columns='month', values='call_minutes')
print(df3_3.boxplot())

print()

print("En este diagarama podremos visualizar un cresimineto progresivo en la duracion de cada una de las llamadas por mes hechas por los usuarios, sobre todo en el ultimo mes donde tenemos bigotes muy por encima de nuestra media de datos.")

print()

print("Del mismo modo que hemos venido estudiado el comportamiento de los usuarios,ahora describiremos estadísticamente los ingresos de los planes")

print()

megaline_fct = total_information['extra_messages'] + total_information['extra_gb'] + \
    total_information['extra_clls'] + total_information['usd_monthly_pay']
total_information['megaline_fct'] = [
    0 if x < 0 else x for x in megaline_fct]
total_information.query('megaline_fct > 0').head(2)

print()

print(total_information.sort_values(by='user_id'))

print()

print("La ultima columna nos indica cuantos ingresos tienen cada usuario en el plan que ha contratado y nos sera muy util para probar nuestras hipotesis estadisticas.")

print()

print("Tambien es importente tenr una visualizacion mas clara y precisa de el ingreso de los planes antes de probar nuestras Hipotesis estaditicas y empezamos verificando , a travez de un diagrama de barras la facturacion a lo largo del año transcurrido.")

print()

print(total_information.columns)

print("Exponemos las columnas de nuestra tabla general para realizar el agrupamiento correspondiente y realizar nuestra grafica.")

print()

df_4 = total_information.groupby(['month', 'plan'])[
    'megaline_fct'].mean().reset_index()
print(df_4.head())

print("Agrupamos nuestro Dataframe antes de exponerlo y para ello vamos a utilizar nuestra columna de facturacion y su mediana.")

print()

grafik_p4 = df_4.pivot(index='month', columns='plan',
                       values='megaline_fct')
print(grafik_p4.plot(kind='bar'))

print()

print("Puede ser normal que el plan Ultimated tenga mayor cantidad de ingreso facturado  en cada uno de los meses de manera independiente, ya que es un plan que tiene mayor costo a comparacion con el plan Surf. Sin embargo tambien vamos ha generar un histograma para verificar la proporcion de ingreso.")

print()

df4_2 = total_information.pivot(
    index=['user_id', 'month'], columns='plan', values='megaline_fct')
print((df4_2.head()))

print()

print("La tabla tiene algunos valores ausentes, sin embargo no los vamos a eliminar, ni tampoco a reeplazar ya que son importantes todas las filas en nuestro histograma.")

print()

print(df4_2.hist())

print()

print("Nuestro gafico de proporcion muestra mayor cantidad de ingreso para  el plan Surf.")

print()

df4_3 = total_information.pivot(
    index='user_id', columns='month', values='megaline_fct')
print(df4_3.boxplot())

print()

print("Nuestro grfico de caja es claro, y muestra una notable inclinacion por el plan Ultimated en cuanto al ingreso del mismo, tenemos pocos valores atipicos, pero tambien representan un ingreso mayor para el plan Ultimated.")

print()

print("Atravez de todos estos calculos y graficos podremos generar algunas conclusiones importantes:")

print()

print("1. El plan Surf tiene mayor catidad de usuarios que el plan Ultimated.")

print()

print("2. El plan ultimate tiene menor cantidad de ingresoso extra ya que abarca mas minutos, mensajes, y gigabytes de internet que el plan Surf.")

print()

print("3. el plan Sur tiene mayor variacion en sus ingresos extra y totales, por que podria generar mayor cantidad de ingresoos totales que el plan Ultimate.")

print()

print()

print("4. Aunuqe sus valores extras tienen poca variacion. Los servicios de los planes del plan Ultimate son mas caros que los servicios que ofrece el plan Surf, esto podria llevar a pensar que no deririan los ingresos de cada plan y que sea el mismo para ambos planes.")

print()

print(total_information['megaline_fct'].fillna(0))


print()

print(total_information['megaline_fct'])

print()

print("Antes de generar nuestras hipotesis estadisticas siempre es importante reemplazar los valores ausentres con 0, para no afectar el resultado de las hipotesis")

print()

print()

print("Ahora estamos listos para probar nuestra hipotesis  de que son diferentes los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf.")

print()

print("Elaboramos nuestras hipotesis nula y alternativa y preparamos los datos para el test estadistico a los que los vamos a someter.")

print()

print("Ho : Los ingresos promedios de los usuarios de los planes ultimate y surf son iguales")
print(" H1 : Los ingresos promedios de los usuarios son difrentes en cada uno de los planes")

print()

df_ultimate = total_information[total_information['plan'] == 'ultimate']
df_surf = total_information[total_information['plan'] == 'surf']
df_ultimate = df_ultimate.dropna()
df_surf = df_surf.dropna()

df_ultimate_calls = df_ultimate.megaline_fct
df_surf_calls = df_surf.megaline_fct

alpha = 0.01

results = st.ttest_ind(df_ultimate_calls, df_surf_calls)

print('valor p:', results.pvalue)

if (results.pvalue < alpha):
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

print()

print()

print("Observamos, a travez de esta prueba que el valor de alfa  es superado por nuestro valor P asi que  rechazamos la hipotesis nula, la cual nos indica que Los ingresos promedios de los usuarios son difrentes en cada uno de los planes.")

print()

print("Tambien hay probar la hipótesis de que el ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.")

print()

print()

print("Asi que vamos a formular las hipotesis nula y alternativa, y filtraremos 2 series preparadas especificamnete para generar nuestro test estadistico.")

print()

print(") Ho : Los usuarios del area de NY-NJ en cuanto a su ingreso promedio, se comportan igual que en otras regiones")
print("H1 : Los usuarios del area de NY-NJ en cuanto a su ingreso promedio, se comportan diferente que en otras regiones")

print()

total_infoE = total_information[total_information['city'].str.contains(
    'NY-NJ')]['megaline_fct']
total_infoA = total_information[~total_information['city'].str.contains(
    'NY-NJ')]['megaline_fct']
total_infoE = total_infoE.dropna()
total_infoA = total_infoA.dropna()

print()

alpha = 0.01

results = st.ttest_ind(total_infoE, total_infoA)
print('valor p:', results.pvalue)
if (results.pvalue < alpha):
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

print()

plt.show(block=True)

print("Segun los resultados de este test, la hipotesis nula que nos propone que, Los usuarios del area de NY-NJ en cuanto a su ingreso promedio, se comportan igual que en otras regiones es valida.")

print()

print("# ## Conclusión general")

print()

print("Para finalizar,vamos a  enumerar las conclusiones importantes. Asegurandonos de  abarcar todas las decisiones releventantes que fueron toamdas en cuenta y que determinaron la forma que se eligio, para procesar y analizar los datos.")

print()

print(" 1. Como primera colclusion podemos hacer enfasis en que, si bien los usuarios del plan Surf, son mayores que los del plan Ultimate. Este ultimo tiene planes mas caros que se equiparan a los ingresos del plan Surf.")

print()

print("2. En cuanto al uso de servicios que superan el plan de cada usuario (servicios extras), el plan Surf tiene mayor variedad de usuarios que han excedido el limite de su plan por mucho y otros que no han superado demasiado su cupo.La variedad es mucho mayor a la del plan Ultimated que si bien tiene pocos exedentes en sus servicios, pues tierne mayor cantidad de servicios qeu el plan Surf.")

print()

print("3. Aunque en primera instancia se pudo haber considerado una mayor significancia de ingresos en el plan Ultimated, gracias a las graficas observamos que ambos planes tienen un ingreso aprecido en volumen, pero tambien hubo meses del año en el que destaco en su mayoria el plan Surf en cuanto al uso de los minutos de lamadas para ser especifo.")

print()

print("4. Las Pruebas hipotesis nos suguieren que no rechacemos la posiblidad de que el ingreso de servicios es igual tanto para el plan Surf, y para el plan Ultimated.")

print()

print("5. Como conlcusion final y despues de realizar un ultimo test estdistico, corroboramos que los ingresos de las ciudades de New York y New Jersey son iguales que los ingresos de otras reguiones del pais.")
