from PIL import ImageEnhance
import random


def apply_realism(image):
    """
    Applies subtle realism effects to a handwritten character image.
    """

    # Rotate the character slightly
    angle = random.uniform(-2, 2)
    image = image.rotate(
        angle,
        expand=True,
        fillcolor=(0, 0, 0, 0)  # Keep new corners transparent
    )

    # Slightly vary the ink darkness
    brightness = random.uniform(0.95, 1.05)
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    return image


def jitter_offset():
    """
    Returns a small random vertical offset
    to make the writing baseline look more natural.
    """
    return random.randint(-2, 2)