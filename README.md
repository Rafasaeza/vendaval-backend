# API REST de Subasta de Artículos

Este proyecto es una API REST para la subasta de artículos, donde cada usuario puede participar tanto como comprador como vendedor. Los usuarios pueden:
- Subir artículos para subasta.
- Pujar por artículos subidos por otros usuarios.

## Tecnologías Utilizadas
- **Framework:** FastAPI (Python)
- **Base de Datos:** MongoDB
- **Servidor de Desarrollo:** Uvicorn

## Documentación y Pruebas
Puedes acceder a la documentación interactiva de la API (Swagger UI) en el siguiente enlace:
[Swagger UI - Vendaval](https://vendaval-backend.vercel.app/docs)

Frontend desplegado: https://vendaval-frontend.vercel.app/
## Instalación y Ejecución en Local
Sigue estos pasos para desplegar la API en tu entorno local:

### 1. Crear un Entorno Virtual
Ejecuta el siguiente comando para crear un entorno virtual y aislar las dependencias:
```bash
python -m venv vendaval
```

### 2. Activar el Entorno Virtual
- En Windows:
  ```bash
  vendaval\Scripts\activate
  ```
- En macOS y Linux:
  ```bash
  source vendaval/bin/activate
  ```

### 3. Instalar Dependencias
Ejecuta el siguiente comando para instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```

### 4. Iniciar la API REST
Ejecuta el siguiente comando para iniciar el servidor (puedes cambiar el puerto según tu preferencia):
```bash
uvicorn main:app --reload --port 13000
```

La API estará disponible en: [http://localhost:13000](http://localhost:13000)

---

### Contribución
Si deseas contribuir al proyecto, puedes clonar el repositorio y enviar tus mejoras mediante Pull Requests.

**Autor:** [Rafael Sáez Arana]  

**Repositorio:** [https://github.com/Rafasaeza/vendaval-backend]

**Repositorio frontend:** [https://github.com/Rafasaeza/vendaval-frontend]

