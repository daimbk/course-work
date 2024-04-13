import os
import requests
from PIL import Image, ImageOps
import time


def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as url_file:
        url_file.write(response.content)


def resize_and_grayscale(input_path, output_path, new_size=(1280, 800)):
    image = Image.open(input_path)
    image_resized = image.resize(new_size)
    image_processed = ImageOps.grayscale(image_resized)
    image_processed.save(output_path)


def process_images():
    # create directories if they don't exist
    os.makedirs('wallpapers', exist_ok=True)
    os.makedirs('processed', exist_ok=True)

    # get image URLs from file
    with open('ImageUrls.txt', 'r') as url_file:
        urls = url_file.readlines()

    # download images
    for index, url in enumerate(urls):
        url = url.strip()
        filename = f'wallpapers/wallpaper_{index}.jpg'
        download_image(url, filename)

    # resize images and apply grayscale
    for index, url in enumerate(urls):
        filename = f'wallpapers/wallpaper_{index}.jpg'
        output_path = f'processed/wallpaper_{index}_processed.jpg'
        resize_and_grayscale(filename, output_path)

    # return the number of images processed
    return len(urls)


if __name__ == "__main__":
    start_time = time.time()

    total_images = process_images()

    # end timer and get time taken
    end_time = time.time()
    total_time = end_time - start_time
    avg_proc_time_per_image = total_time / total_images
    print(f'Total Images: {total_images}')
    print(f'Execution Time: {total_time:.2f} seconds')
    print(f'Average processing time per image: {avg_proc_time_per_image:.2f} seconds')
