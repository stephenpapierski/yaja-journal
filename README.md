# yaja
yaja-journal is Yet Another Journaling App.

Like many others, I searched for a long time for a journaling app that worked for my needs and came up short. Yaja aims to meet my needs for journaling, and if it happens to meet the needs of others, that's great too.

> **Warning**
> As of now, Yaja is in its infancy and is not a functioning application. Below are some goals of what I hope the project will look like in the future.

## Goals
- **Progressive Web App** - accesible via a standard web browser on any device (no apps needed)
- **Simple** - no flashy features that clutter the interface
- **`docker`** - easily hostable on many platforms
- **No vendor lock-in** - stores all journal entires in standard Markdown on local storage
- **Templates** - Like to do a mental check-in or answer similar questions? Templates allow you to have a starting point for different types of journal entries.

## Project Template
[Flask Corona Dark](https://appseed.us/product/corona-dark/flask/) - Provided by **[App Generator](https://appseed.us/app-generator)** serves as the starting point for this project.

![top](https://user-images.githubusercontent.com/51070104/181686893-b039fcba-b7bf-4ab7-b210-a22224ffd516.png)

<br />

## ✨ Quick Start in `Docker`

> 👉 Get the code

```bash
$ git clone https://github.com/stephenpapierski/yaja-journal.git
$ cd yaja-journal
```

> 👉 Start the app in Docker

```bash
$ docker-compose up --build
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## ✨ How to use it

```bash
$ # Get the code
$ git clone https://github.com/stephenpapierski/yaja-journal.git
$ cd yaja-journal
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## ✨ Code-base structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production), and an intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                           # A simple app that serve HTML files
   |    |    |-- routes.py                  # Define app routes
   |    |
   |    |-- authentication/                 # Handles auth routes (login and register)
   |    |    |-- routes.py                  # Define authentication routes
   |    |    |-- models.py                  # Defines models
   |    |    |-- forms.py                   # Define auth forms (login and register)
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |-- requirements-mysql.txt               # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt               # Production modules  - PostgreSql DMBS
   |
   |-- Dockerfile                           # Deployment
   |-- docker-compose.yml                   # Deployment
   |-- gunicorn-cfg.py                      # Deployment
   |-- nginx                                # Deployment
   |    |-- appseed-app.conf                # Deployment
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

## ✨ Recompile CSS

To recompile SCSS files, follow this setup:

<br />

**Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional)

<br />

**Step #2** - Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

<br />

**Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

**Step #4** - Edit & Recompile SCSS files

```bash
$ gulp scss
```

The generated file is saved in `static/assets/css` directory.
