📱 **Proyecto: Análisis de Tarifas Megaline**

**Autor:** Alexander Herrera

**Lenguaje:** Python

**Librerías utilizadas:** ```pandas``` , ```numpy``` , ```matplotlib``` , ```scipy.stats```

**Tipo de proyecto:** Exploración y análisis de datos (EDA)

**Nivel:** Analista de Datos Jr. — Intermedio

⚙️**Configuración del entorno:**

Para garantizar la correcta ejecución del proyecto, se recomienda crear un entorno virtual y usar las dependencias listadas en requirements.txt.

``` sh
1️⃣ Crear el entorno virtual
python -m venv .venv

2️⃣ Activarlo (Windows)
. ./.venv/Scripts/activate

3️⃣.2️⃣  Activarlo (Mac / Linux)
source venv/bin/activate

 4️⃣ clonar el repositortio
git clone https://github.com/code-ALX79/Musica-en-la-Gran-Ciudad.git

5️⃣ Instalar las dependencias
pip install -r requirements.txt

```

🧩 **Descripción general**

Este proyecto analiza los datos de uso de los clientes de **Megaline**, un operador telefónico que ofrece dos planes de prepago:

**°Surf**

**°Ultimate**

Cada cliente registra:
✔ Minutos consumidos
✔ Mensajes enviados
✔ Gigas usados
✔ Mes de uso
✔ Plan contratado

El objetivo del análisis es determinar **cuál de los dos planes es más rentable**, identificando patrones de consumo, excedentes facturados y comportamiento mensual.

El proyecto sigue un flujo profesional de **limpieza, transformación, exploración y análisis,** utilizando Python y pandas.

🎯 **Objetivos**

**1.** Calcular el consumo mensual de llamadas, mensajes e internet por cliente.

**2.** Comparar el comportamiento entre los planes Surf y Ultimate.

**3.** Detectar excedentes y calcular cargos adicionales.

**4.** Construir un DataFrame consolidado con el consumo mensual por usuario.

**5.** Analizar cuál plan genera más ingresos para la empresa.

**6.**  Presentar conclusiones que permitan tomar decisiones de negocio.


```
│
├── data/
│   ├── megaline_calls.csv             # Registro de llamadas
│   ├── megaline_messages.csv          # Registro de SMS
│   ├── megaline_internet.csv          # Sesiones de internet
│   ├── megaline_plans.csv             # Tarifas Surf y Ultimate
│   └── megaline_users.csv             # Información de clientes
│
├── notebooks/
│   └── megline_analysis.ipynb         # Notebook principal del análisis
│
├── scripts/
│   └── megaline_analysis.py           # Script ejecutable del proyecto
│
├── requirements.txt                   # Dependencias necesarias
└── README.md                          # Documentación del proyecto
```

🧹 **Etapas del análisis**
1️⃣ Carga y exploración inicial

*- Lectura de los CSV de llamadas, mensajes, internet, tarifas y usuarios.*

*-Revisión del contenido con ```.head()```, ```.info()``` y ```.describe()```.*

*-Identificación de nulos y duplicados.*


2️⃣ **Limpieza y preparación de datos**

*- Conversión de fechas a formato ```datetime```.*

*- Conversión de MB → GB en tráfico de internet.*

*- Redondeo hacia arriba de duración de llamadas (los planes cobran por minuto entero).*

*- Creación de columnas de mes (```month_calls``` , ```month_messages``` , ```month_internet```).*

*- Agrupación del uso mensual por usuario.*

*- Unificación de todos los datasets en un solo DataFrame maestro.*


3️⃣ **Transformación y cálculo de excedentes**

Se comparan los consumos contra los límites del plan:

*- Minutos incluidos*

*- Mensajes incluidos*

*- Gigas incluidos*

Luego se generan:

*- extra_calls*

*- extra_messages*

*- extra_gb*

Posteriormente se calcula:

💵 **Costo adicional mensual**

Incluye excedentes × tarifas del plan.

💳 **Facturación total mensual**

```facturación = tarifa_base + cargos_extra```


4️⃣ **Resultados y análisis comparativo**

Se realizaron comparaciones mensuales entre Surf y Ultimate:

📨 **Mensajes**

*- Ultimate tiene mayor promedio mensual.*

*- Surf presenta más variabilidad y más excedentes.*

🌐 **Internet**

*- Ultimate consume más en promedio.*

*-Surf muestra más dispersión y casos de sobreuso.*

📞 **Llamadas**

*-Surf supera a Ultimate en varios meses del año.*

*-Ultimate crece más en los meses finales.*

💰 **Facturación**

*- Ultimate genera más ingreso por usuario.*

*- Surf genera ingresos altos por volumen, pero depende más de cargos extra.*


🧪 **Cómo ejecutar el proyecto**

📘 **Opción 1: Ejecutar el Notebook**

*1. Ve al directorio de notebooks:*

```cd notebooks```

*2. Abre el archivo:*

```megaline_analysis.ipynb````

*3. Ejecuta cada celda en orden para reproducir todo el análisis.*

🐍 **Opción 2: Ejecutar el script .py**

*1- Ve al directorio:*

```cd scripts```

*2- Ejecuta:*

 ```python megaline_analysis.py```


💡 **Habilidades demostradas**

*- Limpieza avanzada de datos con pandas.*

*- Agrupación y consolidación de datasets.*

*- Manejo de valores nulos y conversiones de fecha.*

*- Cálculo de métricas por mes y por usuario.*

*- Uso de funciones personalizadas para cálculos de excedentes.*

*- Análisis exploratorio gráfico (EDA).*

*- Integración de múltiples fuentes de datos.*

*- Documentación técnica profesional.*


🧭 **Conclusiones**

✔ **Principales hallazgos:**

*- **Ultimate es más rentable por usuario**, gracias a su tarifa mensual más alta.*

*- Surf es fuerte por volumen, pero más dependiente de cargos adicionales.*

*- Los usuarios de Surf tienden a superar límites de mensajes y GB con mayor frecuencia.*

*- Ultimate ofrece un comportamiento más estable y predecible en sus consumos.*


🤝 **Próximos pasos: ¡Contribuye a este proyecto!**

Este proyecto queda abierto para cualquier **analista, científico de datos, estudiante o entusiasta del análisis** que desee ampliarlo, mejorarlo o abordarlo desde nuevas perspectivas.

Si tienes ideas o quieres experimentar, ¡eres bienvenido! Algunas posibles rutas para contribuir:

🔍 Proponer nuevas visualizaciones o métricas avanzadas

🧮 Implementar pruebas estadísticas adicionales

🤖 Diseñar modelos predictivos para ingresos o cambio de plan

📈 Comparar diferentes enfoques de segmentación de usuarios

🛠️ Optimizar la estructura del código o agregar nuevas funciones

📚 Documentar mejoras o agregar ejemplos de uso

Si deseas colaborar:

**1. Clona el repositorio**

*Crea tu rama:*

```git checkout -b feature-tu-aporte```

*3. Haz tus mejoras y envía un **Pull Request**.*


Toda contribución será revisada y agradecida.
¡Hagamos crecer este proyecto juntos! 🚀

