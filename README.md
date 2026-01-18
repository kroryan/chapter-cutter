# Chapter Cutter

Herramienta en Python para dividir archivos TXT en capítulos y volver a fusionarlos.

This project provides both a CLI and a GUI to split books (plain `.txt`) into numbered chapter files, and to merge chapter files back into a single text.

**Características / Features**
- Splits chapters using language-specific chapter markers (supports English, Spanish, French, German, Italian, Portuguese, Russian, Chinese, Japanese, Korean).
- Merges numbered chapter files (`01.txt`, `02.txt`, ...) preserving order.
- CLI for automation and batch processing.
- Clickable GUI (Tkinter) for easy use on Windows.
- Builds standalone `.exe` for Windows via PyInstaller; includes app icon.

**Instalación / Installation**
- Recomendado: crear un virtualenv.
- Instalar dependencias:

```
pip install -r requirements.txt
```

**Uso - CLI**
- Dividir un archivo:

```
python -m chapter_cutter.cli split dokumen.pub_mybook.txt --lang Spanish
```

- Fusionar una carpeta de capítulos:

```
python -m chapter_cutter.cli merge output_folder --out merged.txt
```

**Uso - GUI**
- Ejecuta la aplicación gráfica:

```
python -m chapter_cutter.gui
```

- O usa el ejecutable `dist\chapter_cutter_gui.exe` generado por el script de build.
- La GUI permite seleccionar con un clic un archivo `.txt` para cortar o una carpeta para fusionar; elegir el idioma y carpeta de salida.

**Compatibilidad de idiomas / Supported languages**
- Spanish, English, French, German, Italian, Portuguese, Russian, Chinese, Japanese, Korean.

**Cómo funciona (nota técnica)**
- El programa busca líneas que coincidan con patrones típicos de encabezado de capítulo (ej. `Chapter`, `Capítulo`, `第...章`, `제...장`).
- Los patrones no son infalibles: libros con encabezados inusuales o capítulos identificados sólo por numeración romana o por números aislados pueden requerir ajustes.
- Si no se detectan marcadores, el splitter deja el archivo entero como un solo capítulo (comportamiento por defecto).

**Construir el ejecutable (.exe) en Windows**
- Se incluye `build_exe.bat` que automatiza la conversión del icono, empaqueta el PNG/ICO dentro del ejecutable y construye dos binarios: `chapter_cutter_cli.exe` y `chapter_cutter_gui.exe`.
- Requisitos: `PyInstaller` y `Pillow` (ya listados en `requirements.txt`).
- Para construir manualmente (si prefieres):

```
python -m pip install -r requirements.txt
python tools/convert_icon.py   # crea app-icon.ico/app-icon.png si es necesario
pyinstaller --onefile --name chapter_cutter_gui --windowed --icon app-icon.ico --add-data "app-icon.png;." --add-data "app-icon.ico;." chapter_cutter/gui.py
```

**Icono / App icon**
- El script `tools/convert_icon.py` convierte `app-icon.png` a `app-icon.ico` y, si sólo existe el `.ico`, regenera una versión `app-icon.png` para mostrar dentro de la GUI.
- El `.ico` se inserta en el `.exe` y la GUI también carga la imagen pequeña desde los datos embebidos para mostrarla en la esquina superior izquierda.

**Ejecución y pruebas rápidas**
- Prueba con el archivo de ejemplo incluido: `dokumen.pub_the-elminster-series-4-elminster-in-hell-forgotten-realms-1st-pbk-ed-0786927461-9780786927463.txt`.

```
python -m chapter_cutter.cli split dokumen.pub_the-elminster-series-4-elminster-in-hell-forgotten-realms-1st-pbk-ed-0786927461-9780786927463.txt --lang English
```

Luego verifica la carpeta creada junto al `.txt` de entrada: contendrá `01.txt`, `02.txt`, ...

**Contribuir / Contributing**
- Ajustes de patrones de idioma: editar `chapter_cutter/patterns.py` para añadir o mejorar expresiones regulares.
- Abrir issues o pull requests en el repositorio.

**Advertencias / Caveats**
- El splitter depende de patrones heurísticos; para libros con maquetación inusual quizá sea necesario adaptar los patrones o preprocesar el `.txt`.
- El proceso de push automático en `build_exe.bat` intentará `git push`; si tus credenciales no están configuradas en el entorno, el push puede fallar.

---

Si quieres que haga el `git push` ahora, dímelo y lo realizo después de esta actualización del README (puedo incluir un commit con este README actualizado y compilar de nuevo).
# Chapter Cutter

Small Python tool to split and merge TXT books into chapters for multiple languages.

Usage:

- Install dependencies: `pip install -r requirements.txt`
- Build .exe (Windows): run `build_exe.bat` (requires PyInstaller installed).


Examples:

- CLI Split: `python -m chapter_cutter.cli split book.txt --lang Spanish`
- CLI Merge: `python -m chapter_cutter.cli merge output_folder --out merged.txt`
- GUI: run the built exe (or `python -m chapter_cutter.gui`) to use a clickable interface.

Output: creates a folder with the base name of the input file and numbered files `01.txt`, `02.txt`, ...
