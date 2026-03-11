# 🚗 MAXI AUTOS

Proyecto web desarrollado con **Django** que simula un marketplace de vehículos donde los usuarios pueden explorar autos y motos, ver detalles, guardar favoritos y contactar al vendedor.

---

# 🧰 Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript

---

# ⚙️ Funcionalidades

### 🚘 Vehículos
- Listado de vehículos
- Página de detalle de cada vehículo
- Información completa: marca, año, tipo, categoría y precio

### 🔎 Buscador
Permite buscar vehículos por:

- título
- marca
- tipo

### 🗂 Categorías
Sistema de filtrado por categorías:

- Autos
- Motos

### 🖼 Galería de imágenes
Cada vehículo incluye:

- imagen principal
- carrusel de imágenes
- miniaturas seleccionables

### ⭐ Sistema de favoritos
Los usuarios pueden:

- guardar vehículos en favoritos
- quitar vehículos de favoritos
- ver sus favoritos
- contador de favoritos en la barra de navegación

### 👤 Usuarios
Sistema de autenticación:

- Login
- Logout

### 📞 Contacto
Cada vehículo incluye:

- botón de contacto por WhatsApp
- acceso a Instagram

### 🧭 Navbar
La barra de navegación incluye:

- Todos los vehículos
- Categoría Autos
- Categoría Motos
- Favoritos
- Login / Logout

### 🦶 Footer
Incluye:

- WhatsApp
- Teléfono
- Instagram
- Ubicación

---

# 📁 Estructura del proyecto
MaxiAutosFinal
│
├── blog
│ ├── models.py
│ ├── views.py
│ ├── admin.py
│
├── templates
│ ├── base.html
│ ├── inicio.html
│ └── vehiculos
│ ├── lista_vehiculos.html
│ └── detalle_vehiculo.html
│
├── media
│
├── db.sqlite3
├── manage.py
└── README.md

Desde el admin se pueden:

- crear vehículos
- cargar imágenes
- crear categorías
- gestionar usuarios
- gestionar favoritos

---

# 📌 Estado del proyecto

Proyecto **completamente funcional**.

Incluye funcionalidades típicas de un marketplace básico de vehículos.

---

# 🚀 Mejoras futuras

- vehículos destacados
- vehículos relacionados
- botón flotante de WhatsApp
- paginación de resultados
- deploy online

---

# 👨‍💻 Autor

Maximiliano Fernández

MaxiAutosFinal
│
├── blog
├── templates
├── media
├── db.sqlite3
├── manage.py
└── README.md