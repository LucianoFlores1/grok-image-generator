import os
from openai import OpenAI
import base64 
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env (Solo para windows()
load_dotenv()

# Obtén la API key de la variable de entorno
api_key = os.getenv("XAI_API_KEY")
if not api_key:
    raise ValueError("Define la variable de entorno XAI_API_KEY con tu key de xAI.")

# Inicializa el cliente con la URL base de grok
client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)

def generate_image(prompt, num_images=1, format="url"):
    """
    Genera imágenes usando la API de Grok.
    - prompt: Texto descriptivo.
    - num_images: 1 a 10 (máximo permitido).
    - format: "url" (devuelve links) o "b64_json" (devuelve base64 para guardar local).
    
    Retorna: Lista de URLs o paths de archivos guardados.
    Costo: ~$0.07 por imagen generada.
    """
    try:
        response = client.images.generate(
            model="grok-2-image-1212",  # Modelo para generación de imágenes
            prompt=prompt,
            n=num_images,
            response_format=format
        )
        
        results = []
        for idx, img_data in enumerate(response.data):
            if format == "url":
                url = img_data.url
                print(f"Imagen {idx+1}: {url}")
                results.append(url)
            elif format == "b64_json":
                b64 = img_data.b64_json
                filename = f"examples/generated_image_{idx+1}.jpg"
                with open(filename, "wb") as f:
                    f.write(base64.b64decode(b64))
                print(f"Imagen {idx+1} guardada como {filename}")
                results.append(filename)
        
        return results
    except Exception as e:
        print(f"Error al generar imágenes: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    prompt = "A mid Poodle, curly-haired dog lying peacefully on a light beige tiled floor. The dog has light-colored fur, possibly cream or pale beige, with soft curls and a gentle expression. She is in a relaxed position, lying on her side with her legs stretched out naturally. The setting is indoors, with warm lighting that highlights her calm demeanor. The dog looks serene, affectionate, and slightly sleepy, evoking a sense of comfort and companionship. The image should capture her from a slightly elevated angle, showing her full body and the texture of her fur. Style: photorealistic, warm tones, soft shadows."
    generate_image(prompt, num_images=1, format="url") 