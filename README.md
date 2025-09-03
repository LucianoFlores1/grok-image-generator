# 🖼️ **USA LA API DE GROK PARA GENERAR IMAGENES EN 3 SIMPLES PASOS**

## Descripción: Este repositorio contiene un script en Python que usa la API de Grok para generar imagenes a partir de un promt de texto

---

# 📋 Prerrequisitos
- Python 3.8+.
- Dependencias: `pip install -r requirements.txt` (`openai`, `python-dotenv`).
- API key de xAI (obtén una en https://console.x.ai/, requiere facturación).
- Archivo `.env` con `XAI_API_KEY=tu_clave` (ESTA ES LA APIKEY. Aquí te dejo un tutorial de como conseguirla ).

---

## Instalación: Solo copia y pegá los siguientes comandos en tu terminal
# 1. Clona el repositorio:
```
git clone https://github.com/LucianoFlores1/grok-image-generator.git
cd GROK_IA_API/
```

# 2. Crea un entorno virtual e instala dependencias:

**Si estas en Windows (PowerShell):**
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Si estas en Linux/Mac:**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# 3. Configura tu clave de la API Grok:
Crea un archivo `.env` en la raíz del proyecto que contendrá tu API Key, 
### El archivo debe contener un codigo, como por ejemplo: 
XAI_API_KEY=xai-EG3xZlhX5S1jqDdgDBucMD6kaCshHO6BPI8TtXpONatZ5eo3KerfTNZJuzMfWqv2ft

Así deberia de quedar tu carpeta:
#### GROK_IA_API/
#### │
#### ├──📁venv
#### ├──.env
#### ├──.gitignore
#### ├──main.py
#### ├──README.md
#### ├──requirements.txt

# 4. Al final de el archivo main.py se encuentran las siguientes lineas de codigo

```
if __name__ == "__main__":
    prompt = "A mid Poodle, curly-haired dog lying peacefully on a light beige tiled floor"
    generate_image(prompt, num_images=1, format="url")
```

Para generar una imagen es necesario modificar esta variable, el texto indicara la imagen que se generará, 
por ejemplo:

`prompt = "Un hombre amarillo disfrazado de el hombre pie, hiperrealista"`

`prompt = "Una anciana cayendose por las escaleras"`

`prompt = "Un niño siniestro"`

El numero de imagenes generadas por prompt depende de la variable `num_images=` 
Modificarla retornara mas imagenes con un limite de 10. Por ejemplo:

`num_images = 2` `num_images = 8` `num_images = 10` 


# 5. Ahora solo queda Ejecutar la aplicación en tu terminal:
```python main.py```

---
# Felicidades generaste una imagen







