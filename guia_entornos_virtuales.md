# Guía de Entornos Virtuales en Python

Guía introductoria sobre entornos virtuales (virtual environments): qué son, por qué se usan y cómo crearlos y manejarlos, aplicado a proyectos en Python/Django.

## 1. ¿Qué es un entorno virtual?

Un **entorno virtual** es una carpeta aislada que contiene una copia de Python y sus propias librerías, **separada del Python "global"** que tenés instalado en tu sistema operativo.

Dicho de otra forma: es una "burbuja" para cada proyecto, donde instalás únicamente las dependencias que ese proyecto necesita, sin que se mezclen con las de otros proyectos ni con las del sistema.

## 2. ¿Por qué se necesita? (el problema que resuelve)

Imaginá esta situación sin entornos virtuales:

- El **Proyecto A** necesita `Django 3.2`.
- El **Proyecto B** necesita `Django 5.0`.
- Si instalás las librerías de forma global (`pip install django`), solo puede haber **una versión instalada a la vez** en tu sistema. Al pasar de un proyecto a otro, romperías el otro.

Además, sin entornos virtuales:

- Se acumulan en el sistema decenas de librerías de proyectos distintos, sin saber cuál usa cada uno.
- Es difícil replicar el proyecto en otra máquina (¿qué versiones exactas necesita?).
- Se puede romper una herramienta del sistema operativo que dependa de una versión específica de una librería de Python.

**El entorno virtual resuelve esto**: cada proyecto tiene sus propias versiones de Python y de las librerías, totalmente aisladas del resto.

## 3. ¿Cómo funciona por dentro? (idea general)

Cuando creás un entorno virtual, Python genera una carpeta (comúnmente llamada `venv` o `env`) con:

- Una copia (o enlace) del ejecutable de Python.
- Una carpeta propia para instalar librerías (`site-packages`), separada de las globales.
- Scripts para "activar" y "desactivar" ese entorno.

Cuando el entorno está **activado**, los comandos `python` y `pip` de tu terminal apuntan a esa copia aislada, no a la instalación global del sistema.

## 4. Crear un entorno virtual

Python ya incluye el módulo `venv` para esto, no hace falta instalar nada adicional (Python 3.3+).

Parado en la carpeta de tu proyecto:

```bash
python -m venv venv
```

- `python -m venv` → ejecuta el módulo `venv`.
- El segundo `venv` → es el **nombre de la carpeta** que se va a crear (podría llamarse distinto, ej. `env`, `.venv`, etc. `venv` es el más común por convención).

Esto crea una carpeta `venv/` en tu proyecto con todo lo necesario.

> En Windows, si `python` no funciona, probá `py -m venv venv`.

## 5. Activar el entorno virtual

Crear el entorno **no alcanza**: hay que **activarlo** cada vez que vayas a trabajar en el proyecto.

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
venv\Scripts\activate.bat
```

### Mac / Linux

```bash
source venv/bin/activate
```

**¿Cómo sé si está activado?** El nombre del entorno aparece entre paréntesis al principio de la línea de la terminal:

```
(venv) C:\Users\nicolas\Desktop\mi_proyecto>
```

> **Nota para Windows/PowerShell:** si aparece un error de "ejecución de scripts deshabilitada" (`running scripts is disabled on this system`), hay que habilitar la ejecución de scripts una vez con:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

## 6. Usar el entorno (instalar librerías)

Con el entorno **activado**, cualquier `pip install` que hagas queda guardado únicamente dentro de esa carpeta `venv/`, sin afectar al resto del sistema:

```bash
pip install django
pip install requests
```

Verificar qué está instalado en el entorno actual:

```bash
pip list
```

## 7. Congelar y restaurar dependencias (`requirements.txt`)

El archivo `requirements.txt` es la forma estándar de dejar registradas las librerías (y sus versiones exactas) que usa el proyecto, para que cualquier otra persona (o vos mismo en otra máquina) pueda instalar exactamente lo mismo.

**Generar el archivo** con lo que está instalado en el entorno activo:

```bash
pip freeze > requirements.txt
```

Esto crea un archivo parecido a:

```
Django==5.0.3
requests==2.31.0
sqlparse==0.4.4
```

**Instalar desde ese archivo** (por ejemplo, al clonar el proyecto en otra máquina):

```bash
pip install -r requirements.txt
```

> Es una buena práctica correr `pip freeze > requirements.txt` cada vez que instalás o actualizás una librería importante del proyecto, y subir ese archivo al repositorio.

## 8. Desactivar el entorno virtual

Cuando termines de trabajar, para volver a la terminal "normal" (fuera del entorno):

```bash
deactivate
```

Este comando funciona igual en Windows, Mac y Linux.

## 9. Flujo completo de ejemplo (proyecto Django)

```bash
# 1. Crear la carpeta del proyecto
mkdir mi_proyecto
cd mi_proyecto

# 2. Crear el entorno virtual
python -m venv venv

# 3. Activarlo
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 4. Instalar dependencias
pip install django

# 5. Guardar las dependencias del proyecto
pip freeze > requirements.txt

# 6. Trabajar normalmente...
django-admin startproject config .
python manage.py runserver

# 7. Al terminar, desactivar el entorno
deactivate
```

### Si alguien más clona el proyecto

```bash
git clone https://github.com/usuario/mi_proyecto.git
cd mi_proyecto

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
```

Así, cualquiera puede levantar el proyecto con exactamente las mismas versiones de librerías, sin importar qué tenga instalado globalmente en su computadora.

## 10. ¿La carpeta `venv/` se sube a Git?

**No.** La carpeta del entorno virtual **nunca** se sube al repositorio: pesa mucho, es específica de cada máquina/sistema operativo, y se puede regenerar fácilmente con `requirements.txt`.

Por eso siempre tiene que estar en el `.gitignore`:

```gitignore
venv/
env/
.venv/
```

Lo que sí se sube es `requirements.txt`, que es el "plano" para reconstruir el entorno en cualquier otra máquina.

## 11. Errores comunes

**"python no se reconoce como un comando"**
→ Python no está instalado o no está en el PATH del sistema. En Windows probar con `py` en lugar de `python`.

**El entorno no se activa / no aparece `(venv)` en la terminal**
→ Verificá que estás parado en la carpeta correcta del proyecto y que usaste el comando de activación correspondiente a tu sistema operativo (ver sección 5).

**"pip install" instala algo pero no lo encuentra al correr el proyecto**
→ Es muy probable que el entorno virtual no esté activado en esa terminal. Cada terminal nueva que abrís necesita activarlo de nuevo.

**Error de permisos/scripts deshabilitados en PowerShell**
→ Ver la nota de la sección 5 (`Set-ExecutionPolicy`).

**Instalé una librería nueva pero un compañero no la tiene**
→ Faltó actualizar `requirements.txt` (`pip freeze > requirements.txt`) y subirlo al repo con `git add`, `git commit`, `git push`.

## 12. Resumen de comandos

| Acción | Comando |
|---|---|
| Crear entorno virtual | `python -m venv venv` |
| Activar (Windows PowerShell) | `venv\Scripts\Activate.ps1` |
| Activar (Windows CMD) | `venv\Scripts\activate.bat` |
| Activar (Mac/Linux) | `source venv/bin/activate` |
| Desactivar | `deactivate` |
| Instalar una librería | `pip install nombre_libreria` |
| Ver librerías instaladas | `pip list` |
| Guardar dependencias | `pip freeze > requirements.txt` |
| Instalar desde archivo | `pip install -r requirements.txt` |

## 13. Recursos

- Documentación oficial de `venv`: [docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
- Guía de empaquetado de Python (dependencias y entornos): [packaging.python.org](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
