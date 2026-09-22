from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, "post/inicio.html")


def post_list(request):
    posts_tecnologia = [
        {
            "id": 1,
            "titulo": "El impacto de la Inteligencia Artificial en la medicina actual",
            "autor": "Alejandro Gómez",
            "fecha": "2026-09-15",
            "categoria": "Inteligencia Artificial",
            "resumen": "Cómo los nuevos modelos de lenguaje y diagnóstico ayudan a los médicos a detectar enfermedades de forma temprana.",
        },
        {
            "id": 2,
            "titulo": "Guía completa de Computación Cuántica para principiantes",
            "autor": "Elena Rostova",
            "fecha": "2026-09-18",
            "categoria": "Computación Cuántica",
            "resumen": "Un desglose sencillo de los conceptos de cúbits, superposición y cómo cambiarán el procesamiento de datos.",
        },
        {
            "id": 3,
            "titulo": "Las mejores prácticas de Ciberseguridad para el trabajo remoto",
            "autor": "Carlos Mendoza",
            "fecha": "2026-09-20",
            "categoria": "Ciberseguridad",
            "resumen": "Protege tus datos y los de tu empresa con estos cinco consejos esenciales de configuración de redes y contraseñas.",
        },
        {
            "id": 4,
            "titulo": "¿Qué es la Web3 y por qué debería importarte?",
            "autor": "Laura Benítez",
            "fecha": "2026-09-21",
            "categoria": "Blockchain",
            "resumen": "Una mirada al futuro de Internet descentralizado, las aplicaciones basadas en blockchain y la soberanía de los datos.",
        },
        {
            "id": 5,
            "titulo": "Tendencias en desarrollo móvil para finales de año",
            "autor": "Martín Silva",
            "fecha": "2026-09-22",
            "categoria": "Desarrollo de Software",
            "resumen": "Analizamos el crecimiento de las apps multiplataforma y la integración nativa de micro-modelos de IA en dispositivos.",
        },
    ]

    return render(request, "post/post_list.html", context={"posts_tecnologia": posts_tecnologia[0]})
