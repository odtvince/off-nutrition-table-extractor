import argparse
from PIL import Image

def crop_img(image_path, coords, saved_location, extend_ratio=0):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    @param extend_ratio: The value by which the bounding boxes to be extended to accomodate the text that has been cut
    """
    image_obj = Image.open(image_path)
    nx, ny = image_obj.size
    modified_coords = (coords[0]-extend_ratio*nx, coords[1]-extend_ratio*ny, coords[2]+extend_ratio*nx, coords[3]+extend_ratio*ny)
    cropped_image = image_obj.crop(modified_coords)
    # cropped_image.save(saved_location)
    cropped_image.show()
    return cropped_image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    ap.add_argument("-c", "--coords", nargs="+", type = int, required=True, help="path to the input image")
    args = ap.parse_args()

    coords = tuple(args.coords)
    saved_location = './'

    crop(args.image, coords, saved_location)

if __name__ == '__main__':
    main()