# Media Downloader Bot

Este proyecto es un bot de Telegram que permite descargar videos y audios de YouTube, entre otras plataformas.

## Funcionalidades

- Descargar videos y audios de YouTube.
- Interactuar con un servidor Django.
- Otras funcionalidades de descarga (Instagram, TikTok, etc.).

## Requisitos

1. **Python 3.x**: Asegúrate de tener instalada una versión reciente de Python.

2. **Librerías necesarias**:
    - `django`
    - `pytube`
    - `python-telegram-bot`
    - `aiohttp`
    - Otras dependencias mencionadas en `requirements.txt`.

3. **FFmpeg**: Necesitas instalar FFmpeg y agregarlo al PATH de tu sistema. FFmpeg es una herramienta poderosa para manejar archivos multimedia.

### Instalación de FFmpeg

#### Windows

1. Descarga FFmpeg desde el sitio oficial: [FFmpeg Download](https://ffmpeg.org/download.html).
2. Extrae el archivo descargado y mueve la carpeta a una ubicación permanente, por ejemplo, `C:\ffmpeg`.
3. Agrega FFmpeg al PATH:
    - Abre el Panel de Control y selecciona **Sistema**.
    - Haz clic en **Configuración avanzada del sistema**.
    - En la pestaña **Opciones avanzadas**, haz clic en **Variables de entorno**.
    - En **Variables del sistema**, busca la variable `Path` y haz clic en **Editar**.
    - Agrega la ruta `C:\ffmpeg\bin` y guarda los cambios.

#### macOS

1. Instala FFmpeg usando Homebrew:
    ```sh
    brew install ffmpeg
    ```

#### Linux

1. Instala FFmpeg utilizando el gestor de paquetes de tu distribución. Por ejemplo, en Ubuntu:
    ```sh
    sudo apt update
    sudo apt install ffmpeg
    ```

## Configuración

### Crear Carpetas Necesarias
1. Inicia sesion en Instagram con el navegador Firefox:

2. Ejecuta el script `import_instagram_firefox_session.py` para generar el archivo de sesion de Instagram:

```sh
mediadownloaderboot/scripts/create_necessary_folders.py
```

3. Ejecuta el script `create_necessary_folders.py` para crear las carpetas necesarias en la estructura de tu proyecto:

```sh
mediadownloaderboot/scripts/create_necessary_folders.py
```

### Crear archivo `.env`

1. **Crear variable `BOT_TOKEN`**:
   - **Descripción**: Guarda aquí el token de tu bot.
   - **Ejemplo**:
     ```plaintext
     BOT_TOKEN=tu_bot_token_aqui
     ```
2. **Crear variable `INSTAGRAM_USERNAME`**:
   - **Descripción**: Guarda aquí tu nombre de usuario de Instagram.
   - **Ejemplo**:
     ```plaintext
     INSTAGRAM_USERNAME=tu_usuario_de_instagram
     ```

3. **Crear variable `INSTAGRAM_SESSION_FILEPATH`**:
   - **Descripción**: Guarda aquí la ruta al archivo de sesión de Instagram.
   - **Ejemplo**:
     ```plaintext
     INSTAGRAM_SESSION_FILEPATH=ruta_al_archivo_de_sesion
     ```

#### Ejemplo de archivo `.env` completo:
```plaintext
BOT_TOKEN=tu_bot_token_aqui
INSTAGRAM_USERNAME=tu_usuario_de_instagram
INSTAGRAM_SESSION_FILEPATH=ruta_al_archivo_de_sesion
# Puedes agregar más variables de entorno aqui
```
