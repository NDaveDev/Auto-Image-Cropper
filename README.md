# Auto Image Cropper

This repository contains a Python script for automatically cropping images to their outermost non-transparent pixels.

## Prerequisites

The script requires Python 3 and the Pillow library. You can install Pillow using pip:

```bash
pip install pillow
```

## Usage

The `cropper.py` script crops an image to its outermost non-transparent pixels. The script specifically takes images from a folder named `input_folder` and outputs the cropped images to a folder named `output_folder`. 

To run the script, simply use:

```bash
python cropper.py
```

This will take all the .png images from the `input_folder`, crop them, and save the results to the `output_folder` with “_cropped.png” added to their original filenames.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

