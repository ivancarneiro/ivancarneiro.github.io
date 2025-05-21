import json
import os
from jinja2 import Environment, FileSystemLoader

def generate_cv():
    # Definir las rutas
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)  # Subir un nivel para llegar a la raíz del repositorio
    json_path = os.path.join(script_dir, 'cv_data.json')
    template_path = project_root
    output_path = os.path.join(project_root, 'index.html')

    # Leer los datos del JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            cv_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {json_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: El archivo {json_path} no tiene un formato JSON válido")
        return

    # Configurar el entorno de Jinja2
    env = Environment(loader=FileSystemLoader(template_path))
    try:
        template = env.get_template('index.html')
    except Exception as e:
        print(f"Error al cargar el template index.html: {e}")
        return

    # Renderizar el template con los datos
    try:
        rendered_html = template.render(**cv_data)
    except Exception as e:
        print(f"Error al renderizar el template: {e}")
        return

    # Guardar el archivo renderizado
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)
        print(f"Archivo {output_path} generado exitosamente")
    except Exception as e:
        print(f"Error al escribir el archivo {output_path}: {e}")

if __name__ == "__main__":
    generate_cv()