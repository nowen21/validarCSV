# 📄 Aplicación Django para Validación de CSV  

**Versión 1.0.0** | 🐍 **Django 5.1.6** | 🖥️ **Windows / macOS / Linux**  

🚀 Aplicación web desarrollada en **Django** para la validación de archivos CSV según una estructura definida. Utiliza la plantilla **ARCHA** descargada de [BootstrapMade](https://bootstrapmade.com/arsha-free-bootstrap-html-template-corporate/).  

---

## 📌 Características  
👉 **Carga y validación de archivos CSV**  
👉 **Verificación de estructura de columnas y tipos de datos**  
👉 **Mensajes de error detallados con fila y columna afectada**  
👉 **Interfaz moderna basada en Bootstrap**  
👉 **Despliegue fácil en cualquier sistema operativo**  

---

## 🔧 Requisitos Técnicos  

### 🗉️ **Requisitos del sistema**  
- 👉 **Python 3.13.2+**  
- 👉 **Django 5.1.6**  
- 👉 **Base de datos SQLite (por defecto) o PostgreSQL/MySQL**  
- 👉 **Bibliotecas necesarias:** Especificadas en `requirements.txt`  

---

## 🏗️ Reglas de Validación del Archivo CSV  
El archivo debe cumplir con la siguiente estructura:

1️⃣ **Debe contener exactamente 5 columnas**. Si tiene más o menos, se mostrará un error.  
2️⃣ **Columna 1:** Solo permite números enteros entre 3 y 10 caracteres.  
3️⃣ **Columna 2:** Solo permite correos electrónicos válidos.  
4️⃣ **Columna 3:** Solo acepta los valores "CC" o "TI".  
5️⃣ **Columna 4:** Solo permite valores numéricos entre 500,000 y 1,500,000.  
6️⃣ **Columna 5:** Permite cualquier valor.  

Tras cargar el archivo, se mostrará un mensaje indicando el éxito o los errores detectados, indicando la fila y columna correspondiente.  

---

## 📦 Instalación  

### **1️⃣ Clonar el repositorio**
```bash
 git clone https://github.com/nowen21/validarCSV.git
 cd validarCSV
```

### **2️⃣ Crear un entorno virtual e instalar dependencias**  
```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows
pip install -r requirements.txt
```

### **3️⃣ Configurar la base de datos**  
Ejecutar las migraciones:  
```bash
python manage.py migrate
```

### **4️⃣ Ejecutar el servidor de desarrollo**  
```bash
python manage.py runserver
```
Accede a la aplicación en: [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 🎯 Uso  
1️⃣ Ingresa a la aplicación web.  
2️⃣ Carga un archivo CSV con la estructura correcta.  
3️⃣ La aplicación validará el archivo y mostrará los resultados en pantalla.  
4️⃣ En caso de errores, se indicará la fila y columna afectada.  
5️⃣ Si el archivo es válido, se mostrará un mensaje de confirmación.  

---

## 🏗️ Estructura del Proyecto  
```
VALIDARCSV/
│── statics/
│   │── assets/
│   │   │── css/
│   │   │   │── main.css
│   │   │── img/
│   │   │── js/
│   │   │── scss/
│   │   │── vendor/
│   │── css/
│── templates/
│   │── partials/
│   │── base.html
│   │── index.html
│   │── pruetecn.html
│── validarCSV/
│   │── __pycache__/
│   │── __init__.py
│   │── asgi.py
│   │── forms.py
│   │── settings.py
│   │── urls.py
│   │── views.py
│   │── wsgi.py
│── db.sqlite3
│── manage.py
│── README.md
│── requirements.txt
```

---

## 🏢 Tecnologías Usadas  
- **Django 5.1.6**  
- **Bootstrap 5 (Plantilla ARCHA)**  
- **SQLite / PostgreSQL / MySQL**  
- **Python 3.13.2+**  
- **Pandas para validación de archivos CSV**  

---

## 📑 Licencia  
Este proyecto está bajo la licencia [MIT](LICENSE).  

---

## 👤 Autor  
Desarrollado por [Ing. José Dúmar Jiménez Ruíz](https://github.com/nowen21).  

