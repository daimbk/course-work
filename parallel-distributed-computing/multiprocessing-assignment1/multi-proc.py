import os
import requests
from PIL import Image, ImageOps
import time
import multiprocessing


def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as url_file:
        url_file.write(response.content)


def resize_and_grayscale(input_path, output_path, new_size=(1280, 800)):
    image = Image.open(input_path)
    image_resized = image.resize(new_size)
    image_processed = ImageOps.grayscale(image_resized)
    image_processed.save(output_path)


def process_image(idx, url):
    filename = f'wallpapers/wallpaper_{idx}.jpg'
    output_path = f'processed/wallpaper_{idx}_processed.jpg'
    download_image(url, filename)
    resize_and_grayscale(filename, output_path)


def main(num_processes):
    # sequential code start time
    seq_start = time.time()

    # create directories if they don't exist
    os.makedirs('wallpapers', exist_ok=True)
    os.makedirs('processed', exist_ok=True)

    # get image URLs from file
    with open('ImageUrls.txt', 'r') as url_file:
        urls = url_file.readlines()
        total_images = len(urls)

    seq_time = time.time() - seq_start

    # parallel code start time
    par_start = time.time()

    # create a pool of workers
    with multiprocessing.Pool(processes = num_processes) as pool:
        # use map to distribute the task to all available workers
        pool.starmap(process_image, [(idx, url.strip()) for idx, url in enumerate(urls)])

    # parallel end time
    par_time = time.time() - par_start

    # return sequential execution time, parallel execution time, total number of images
    return seq_time, par_time, total_images


if __name__ == "__main__":
    start_time = time.time()

    num_processes = 14
    seq_time, par_time, total_images = main(num_processes)

    # end timer and get time taken
    end_time = time.time()
    total_time = end_time - start_time
    avg_proc_time_per_image = total_time / total_images

    parallelizable_ratio = seq_time / (seq_time + par_time)
    speedup = 1 / ((1 - parallelizable_ratio) + (parallelizable_ratio / num_processes))

    print(f'Total Images: {total_images}')
    print(f'Number of Multiprocessing processes: {num_processes}')
    print(f'Execution Time: {total_time:.2f} seconds')
    print(f'Average processing time per image: {avg_proc_time_per_image:.2f} seconds')
    print(f'Speedup: {speedup:.2f}x')
