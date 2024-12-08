# Media Downloader Bot

Este proyecto es un bot de Telegram que permite descargar videos y audios de YouTube, entre otras plataformas.

## Funcionalidades
- Descargar videos y audios de YouTube.
- Soporte para descargas desde Instagram y TikTok.

---

## Requisitos

1. **Python 3.x**: Asegúrate de tener instalada una versión reciente de Python.
2. **Librerías necesarias**: Todas las dependencias están especificadas en `requirements.txt`.
3. **Firefox**: Instala el navegador web Firefox.
4. **FFmpeg**: Una herramienta para manejar archivos multimedia. Es necesario instalarla y agregarla al PATH.
5. **Playwright**: Si las descargas de TikTok presentan errores, ejecuta el siguiente comando:
   ```bash
   py -m playwright install
   ```

---

## Instalación de FFmpeg

### Windows

#### Usando Chocolatey
1. Abre el Símbolo del sistema o PowerShell como administrador.
2. Instala FFmpeg ejecutando:
   ```bash
   choco install ffmpeg
   ```
   Chocolatey se encargará de la instalación y configurará el PATH automáticamente.

#### Instalación Manual
1. Descarga FFmpeg desde el sitio oficial: [FFmpeg Download](https://ffmpeg.org/download.html).
2. Extrae el archivo descargado y mueve la carpeta a una ubicación como `C:\ffmpeg`.
3. Agrega FFmpeg al PATH:
   - Abre **Panel de Control** y selecciona **Sistema**.
   - Haz clic en **Configuración avanzada del sistema**.
   - En la pestaña **Avanzado**, selecciona **Variables de entorno**.
   - Busca la variable `Path` en **Variables del sistema** y haz clic en **Editar**.
   - Agrega `C:\ffmpeg\bin` y guarda los cambios.

### macOS
Instala FFmpeg con Homebrew:
```bash
brew install ffmpeg
```

### Linux
Usa el gestor de paquetes de tu distribución. Por ejemplo, en Fedora:
```bash
sudo dnf install ffmpeg
```

---

## Configuración

### Crear carpetas necesarias
Ejecuta:
```bash
python3 scripts/create_necessary_folders.py
```

### Configurar Instagram
1. Inicia sesión en Instagram usando Firefox.
2. Ejecuta:
   ```bash
   python3 scripts/import_instagram_firefox_session.py
   ```
   Esto generará un archivo de sesión. Guarda su ruta.

### Configurar TikTok
1. Accede a [tiktok.com](https://tiktok.com) e identifica el **MS_TOKEN**.
2. Usa una extensión como `Cookie-Editor` para extraerlo.

---

## Crear archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
BOT_TOKEN=tu_bot_token_aqui
INSTAGRAM_USERNAME=tu_usuario_de_instagram
INSTAGRAM_SESSION_FILEPATH=ruta_al_archivo_de_sesion
TIK_TOK_MS_TOKEN=tu_ms_token
```

### Ejemplo de archivo `.env` completo:

```env
BOT_TOKEN=1234567890:ABCDEFGH-TuTokenDeBotAqui
INSTAGRAM_USERNAME=mi_usuario
INSTAGRAM_SESSION_FILEPATH=/home/tu_usuario/rutas/instagram_session.json
TIK_TOK_MS_TOKEN=abc123456789xyz
```

---

## Ejecución
En la ruta del proyecto, ejecuta:
```bash
python3 app.py
```

---

