# Guía de Git desde Cero — Python/Django

Guía introductoria a Git y GitHub pensada para el curso, aplicada a proyectos en Python/Django.

## 1. ¿Qué es Git y por qué usarlo?

Git es un **sistema de control de versiones**: guarda el historial de cambios de tu código, permite volver atrás, trabajar en paralelo con otras personas sin pisarse el trabajo, y es la base de flujos de trabajo colaborativos como los de GitHub.

**Git ≠ GitHub**:
- **Git**: el programa que corre en tu computadora y maneja el versionado.
- **GitHub**: un servicio web (hay otros como GitLab o Bitbucket) que aloja repositorios Git en la nube y agrega funcionalidades de colaboración (Pull Requests, Issues, etc.).

## 2. Conceptos clave

| Concepto | Qué significa |
|---|---|
| **Repositorio (repo)** | Carpeta de tu proyecto rastreada por Git. |
| **Commit** | Una "foto" del estado del proyecto en un momento dado, con un mensaje descriptivo. |
| **Working directory** | Los archivos tal cual están en tu carpeta ahora. |
| **Staging area (índice)** | Zona intermedia donde preparás los cambios que van a formar el próximo commit. |
| **Branch (rama)** | Una línea de desarrollo independiente. La rama principal hoy se llama **`main`** (antes se usaba `master`). |
| **Remote (remoto)** | Una copia del repo alojada en otro lugar (ej. GitHub). El remoto por defecto se llama **`origin`**. |
| **Clone** | Copiar un repo remoto a tu máquina. |
| **Pull** | Traer cambios del remoto a tu máquina. |
| **Push** | Enviar tus commits locales al remoto. |
| **Merge** | Combinar los cambios de una rama en otra. |
| **Pull Request (PR)** | En GitHub, una propuesta para fusionar cambios de una rama a otra, con revisión de código. |

## 3. Instalación y configuración inicial

Verificar si ya está instalado:

```bash
git --version
```

Si no está instalado, bajarlo de [git-scm.com](https://git-scm.com/).

Configurar tu identidad (una sola vez por máquina, se guarda global):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

Ver la configuración actual:

```bash
git config --list
```

**Tip:** desde 2020 GitHub cambió el nombre por defecto de la rama principal de `master` a `main`. Podés configurar tu Git local para que use `main` en todo repo nuevo:

```bash
git config --global init.defaultBranch main
```

## 4. Crear un repositorio desde cero y subirlo a GitHub (paso a paso)

Este es el flujo típico para arrancar un proyecto Django nuevo y publicarlo en GitHub.

### Paso 1 — Crear la carpeta del proyecto e iniciar Git

```bash
mkdir mi_proyecto_django
cd mi_proyecto_django
git init
```

`git init` crea un repositorio Git local (una carpeta oculta `.git/`). Si configuraste `init.defaultBranch main`, la rama ya se llama `main`. Si no, podés renombrarla manualmente:

```bash
git branch -M main
```

### Paso 2 — Crear un `.gitignore`

Muy importante en proyectos Python/Django: evita subir archivos que no deberían estar en el repo (entornos virtuales, archivos compilados, configuraciones locales, la base de datos SQLite, etc.).

Ejemplo de `.gitignore` típico para Django:

```gitignore
# Entornos virtuales
venv/
env/
.venv/

# Python
__pycache__/
*.pyc

# Django
*.sqlite3
/media
/staticfiles

# Variables de entorno / secretos
.env

# Editor / SO
.vscode/
.idea/
.DS_Store
```

### Paso 3 — Primer commit

```bash
git add .
git commit -m "Primer commit: estructura inicial del proyecto"
```

### Paso 4 — Crear el repositorio en GitHub

1. Entrar a [github.com](https://github.com) e iniciar sesión.
2. Click en **New repository**.
3. Ponerle nombre (ej. `mi_proyecto_django`).
4. **No** marcar "Initialize with README" si ya tenés commits locales (para evitar conflictos de historiales).
5. Crear el repositorio. GitHub va a mostrar la URL, algo como:
   `https://github.com/tu-usuario/mi_proyecto_django.git`

### Paso 5 — Conectar el repo local con el remoto

```bash
git remote add origin https://github.com/tu-usuario/mi_proyecto_django.git
```

Verificar que quedó bien conectado:

```bash
git remote -v
```

### Paso 6 — Subir los cambios (push)

```bash
git push -u origin main
```

El flag `-u` (o `--set-upstream`) asocia tu rama local `main` con la rama `main` del remoto `origin`. A partir de ahí, alcanza con `git push` a secas.

### Alternativa: clonar un repo que ya existe

Si el repositorio ya fue creado en GitHub (por ejemplo, por un profesor o compañero) y solo necesitás una copia local:

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```

## 5. Flujo de trabajo diario (el ciclo básico)

```bash
git status              # ver qué archivos cambiaron
git add archivo.py      # agregar un archivo puntual al staging
git add .                # agregar TODOS los cambios al staging
git commit -m "mensaje"  # crear el commit con lo que está en staging
git push                 # subir los commits al remoto
```

Antes de empezar a trabajar (sobre todo en equipo), conviene traer lo último del remoto:

```bash
git pull
```

## 6. Comandos más usados (referencia rápida)

### Estado e historial

```bash
git status                 # estado actual: qué está modificado/staged/sin trackear
git log                    # historial de commits
git log --oneline --graph  # historial resumido con gráfico de ramas
git diff                   # diferencias entre working directory y staging
git diff --staged          # diferencias entre staging y el último commit
```

### Guardar cambios

```bash
git add <archivo>          # agregar un archivo al staging
git add .                  # agregar todos los cambios
git commit -m "mensaje"    # commitear lo que está en staging
git commit -am "mensaje"   # add + commit en un paso (solo archivos ya trackeados)
```

### Ramas (branches)

```bash
git branch                     # listar ramas locales
git branch nueva-rama          # crear una rama nueva
git checkout nueva-rama        # cambiar a esa rama
git checkout -b nueva-rama     # crear y cambiar en un solo paso
git switch nueva-rama          # forma moderna de cambiar de rama
git switch -c nueva-rama       # forma moderna de crear y cambiar
git merge nueva-rama           # fusionar "nueva-rama" en la rama actual
git branch -d nueva-rama       # borrar una rama local (ya fusionada)
```

### Trabajo con el remoto

```bash
git remote -v                  # ver remotos configurados
git remote add origin <url>    # agregar un remoto
git push                       # subir commits
git push -u origin main        # subir y fijar la rama upstream
git pull                       # traer y fusionar cambios del remoto
git fetch                      # traer cambios del remoto SIN fusionar
git clone <url>                # clonar un repo remoto
```

### Deshacer cosas (con cuidado)

```bash
git restore <archivo>          # descartar cambios locales de un archivo (working dir)
git restore --staged <archivo> # sacar un archivo del staging (sin perder el cambio)
git reset --soft HEAD~1        # deshacer el último commit, dejando los cambios en staging
git revert <hash-del-commit>   # crear un commit nuevo que revierte uno anterior (seguro en repos compartidos)
```

> ⚠️ `git reset --hard` y `git push --force` reescriben historial o descartan cambios de forma permanente. Evitarlos salvo que sepas exactamente qué estás haciendo, y nunca usarlos sobre ramas compartidas sin avisar al equipo.

### Otros útiles

```bash
git stash              # guardar cambios sin commitear, para retomarlos después
git stash pop           # recuperar lo guardado con stash
git show <hash>         # ver el contenido de un commit puntual
```

## 7. `master` vs `main`: por qué importa

- Históricamente, la rama principal de un repo Git se llamaba `master` por convención.
- En 2020, GitHub (y luego GitLab y la comunidad en general) adoptaron **`main`** como nombre por defecto para nuevas rama principal.
- Funcionalmente **`main` y `master` son idénticos**, es solo un nombre de rama.
- Lo importante es que el nombre de tu rama local coincida con el de tu rama remota al hacer push/pull. Si ves un error tipo `src refspec main does not match any`, generalmente es porque tu rama local se llama distinto que la que espera el remoto.

Para renombrar una rama existente de `master` a `main`:

```bash
git branch -M main
```

## 8. Ejemplo aplicado a un proyecto Django

Flujo completo para un proyecto Django armado desde cero:

```bash
# 1. Crear entorno virtual y activarlo
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 2. Instalar Django y crear el proyecto
pip install django
django-admin startproject config .

# 3. Congelar dependencias
pip freeze > requirements.txt

# 4. Inicializar Git
git init
git branch -M main

# 5. Crear .gitignore (ver sección 4, Paso 2)

# 6. Primer commit
git add .
git commit -m "Proyecto Django inicial"

# 7. Conectar con GitHub y subir
git remote add origin https://github.com/tu-usuario/mi-proyecto.git
git push -u origin main
```

A partir de ahí, cada vez que se agrega una funcionalidad (una app, un modelo, una vista):

```bash
git add .
git commit -m "Agrega app 'productos' con modelo Producto"
git push
```

## 9. Buenas prácticas

- **Commits chicos y frecuentes**, con mensajes claros que digan *qué* y *por qué* (ej: `"Corrige validación de email en formulario de registro"`, no `"cambios"` o `"fix"`).
- Nunca subir el entorno virtual (`venv/`), la base de datos local, ni archivos con contraseñas/API keys (usar `.env` + `.gitignore`).
- Usar ramas para features nuevas en vez de trabajar todo directo sobre `main` (ej: `git checkout -b feature/login`).
- Hacer `git pull` antes de empezar a trabajar si el proyecto es compartido.
- Revisar `git status` antes de cada `add`/`commit` para saber exactamente qué se va a subir.

## 10. Errores comunes y cómo resolverlos

**"fatal: not a git repository"**
→ No corriste `git init` en la carpeta, o no estás parado en la carpeta correcta.

**"src refspec main does not match any"**
→ Tu rama local no se llama `main` (puede ser `master` o no tener commits todavía). Verificá con `git branch` y hacé al menos un commit antes del push.

**"failed to push some refs" / rechazo al hacer push**
→ El remoto tiene cambios que no tenés localmente. Solución: `git pull` (y resolver conflictos si aparecen) y luego `git push` de nuevo.

**Conflictos de merge**
→ Git no puede combinar automáticamente los cambios. Hay que abrir los archivos marcados, elegir qué contenido queda (Git marca las secciones con `<<<<<<<`, `=======`, `>>>>>>>`), guardar, y luego:

```bash
git add <archivo-resuelto>
git commit
```

## 11. Recursos

- Documentación oficial: [git-scm.com/doc](https://git-scm.com/doc)
- GitHub Docs: [docs.github.com](https://docs.github.com)
- Hoja de referencia visual: [ohshitgit.com](https://ohshitgit.com) (para cuando algo sale mal)
