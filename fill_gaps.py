import os
import re
from PIL import Image

def get_image_numbers(directory):
    files = os.listdir(directory)
    image_numbers = []
    for file in files:
        match = re.match(r"Metacritic rant(\d+)\.png", file)
        if match:
            image_numbers.append(int(match.group(1)))
    return sorted(image_numbers)

def find_gaps(numbers):
    return [num for num in range(numbers[0], numbers[-1] + 1) if num not in numbers]

def create_blank_image(size, file_path):
    img = Image.new('RGBA', size, (0, 0, 0, 0))  # Create a blank (transparent) image
    img.save(file_path)

def fill_gaps(directory, image_numbers, gaps):
    if not image_numbers:
        print("No images found with the specified naming convention.")
        return

    # Determine the size of the blank images using the first image
    first_image_path = os.path.join(directory, f"Metacritic rant{image_numbers[0]}.png")
    with Image.open(first_image_path) as img:
        size = img.size

    for gap in gaps:
        file_path = os.path.join(directory, f"Metacritic rant{gap}.png")
        create_blank_image(size, file_path)
        print(f"Created blank image for missing file: {file_path}")

def main():
    directory = os.getcwd()  # Get the current working directory
    image_numbers = get_image_numbers(directory)
    if image_numbers:
        gaps = find_gaps(image_numbers)
        fill_gaps(directory, image_numbers, gaps)
    else:
        print("No images found with the specified naming convention.")

if __name__ == "__main__":
    main()
