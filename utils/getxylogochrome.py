import pyautogui
from typing import Tuple, Optional

def getxylogochrome(imagen: str) -> Optional[Tuple[int, int]]:
    """
    Busca una imagen en la pantalla y devuelve sus coordenadas centrales.
    
    Args:
        imagen (str): Ruta del archivo de imagen a buscar
        
    Returns:
        Optional[Tuple[int, int]]: Tupla con coordenadas (x, y) del centro de la imagen,
                                   o None si no se encuentra o hay un error
    """
    try:
        # Intentar localizar la imagen en la pantalla (sin confidence)
        ubicacion = pyautogui.locateOnScreen(imagen)
        
        if ubicacion is None:
            print(f"No se encontró la imagen '{imagen}' en la pantalla")
            return None
        
        # Obtener las coordenadas del centro de la imagen
        x, y = pyautogui.center(ubicacion)
        print(f"Imagen encontrada en coordenadas: ({x}, {y})")
        return (x, y)
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{imagen}'")
        return None
        
    except pyautogui.ImageNotFoundException:
        print(f"Error: La imagen '{imagen}' no fue encontrada en la pantalla")
        return None
        
    except Exception as e:
        print(f"Error inesperado al buscar la imagen: {type(e).__name__}: {e}")
        return None


# Ejemplo de uso (comentado para no ejecutar automáticamente)
if __name__ == "__main__":
    # coordenadas = getxylogochrome("logo_chrome.png")
    # if coordenadas:
    #     print(f"Coordenadas obtenidas: {coordenadas}")
    # else:
    #     print("No se pudieron obtener las coordenadas")
    pass