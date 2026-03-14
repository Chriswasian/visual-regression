import os
import requests
from PIL import Image, ImageChops

BASELINE_FILE = "baseline.png"
CURRENT_FILE = "current.png"

def take_screenshot(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Saved: {filename}")
    else:
        print(f"Failed to download image")

def compare_images(file1, file2):
    img1 = Image.open(file1)
    img2 = Image.open(file2)
    diff = ImageChops.difference(img1, img2)
    if diff.getbbox() is None:
        print("✅ No differences found.")
    else:
        print("❌ Differences detected!")
    diff.save("diff-result.png")
    print("Saved diff to: diff-result.png")

def main():
    url = input("Enter image URL to test: ")
    take_screenshot(url, BASELINE_FILE)
    take_screenshot(url, CURRENT_FILE)
    compare_images(BASELINE_FILE, CURRENT_FILE)

main()
