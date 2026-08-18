#!/usr/bin/env python3
"""
Prebake colored aspect images from grayscale PNGs.
Reads aspect_registry.json and creates colored versions of each aspect.
"""

import json
from PIL import Image
import os

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def colorize_image(input_path, output_path, hex_color):
    """
    Colorize a grayscale image with the given color.
    Uses multiply blend mode: grayscale * color
    """
    # Load the grayscale image
    img = Image.open(input_path).convert('RGBA')
    
    # Get the color
    r, g, b = hex_to_rgb(hex_color)
    
    # Create a color overlay
    colored = Image.new('RGBA', img.size)
    pixels = colored.load()
    src_pixels = img.load()
    
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            src_r, src_g, src_b, src_a = src_pixels[x, y]
            
            # Multiply blend mode
            new_r = int((src_r / 255.0) * r)
            new_g = int((src_g / 255.0) * g)
            new_b = int((src_b / 255.0) * b)
            
            pixels[x, y] = (new_r, new_g, new_b, src_a)
    
    # Save the colored image
    colored.save(output_path, 'PNG')
    return True

def main():
    print("Prebaking Colored Aspect Images")
    print("=" * 50)
    
    # Load aspect registry
    print("Loading aspect_registry.json...")
    with open('aspect_registry.json', 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    print(f"Found {len(registry['aspects'])} aspects")
    
    # Create output directory
    output_dir = 'aspect_images_colored'
    os.makedirs(output_dir, exist_ok=True)
    print(f"Created output directory: {output_dir}/")
    
    # Process each aspect
    success_count = 0
    error_count = 0
    
    for aspect in registry['aspects']:
        tag = aspect['tag']
        color = aspect['hexColor']
        input_path = f"aspect_images/{tag}.png"
        output_path = f"{output_dir}/{tag}.png"
        
        if not os.path.exists(input_path):
            print(f"[ERROR] {tag}: File not found")
            error_count += 1
            continue
        
        try:
            colorize_image(input_path, output_path, color)
            print(f"[OK] {tag}: {color}")
            success_count += 1
        except Exception as e:
            print(f"[ERROR] {tag}: {e}")
            error_count += 1
    
    print("\n" + "=" * 50)
    print(f"Successfully colored: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Output directory: {output_dir}/")
    print("\nNext step: Update index.html to use 'aspect_images_colored' instead of 'aspect_images'")

if __name__ == '__main__':
    main()
