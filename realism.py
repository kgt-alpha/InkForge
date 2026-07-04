from PIL import ImageEnhance
import random


def apply_realism(image):
    """
    Applies small random effects to a character image
    so the handwriting looks more natural.
    """

    # Rotate the character slightly
    angle = random.uniform(-2, 2)
    image = image.rotate(angle, expand=True)

    # Slightly change the ink darkness
    brightness = random.uniform(0.9, 1.1)
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    return image


def jitter_offset():
    """
    Returns a small random vertical offset.
    This makes characters sit slightly above
    or below the writing line.
    """
    return random.randint(-2, 2)