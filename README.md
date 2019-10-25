# ColorPalette
Find the dominant colors in any image

# Setup Instructions:
## Step 1)
Make sure you have python installed on your machine

## Step 2)
navigate into the main directory ColorPalette and create a python virtual environment as follows:
```
python3 -m venv env
```

## Step 3)
Activate the virtual environment as follows:
```
source env/bin/activate
```

## Step 4)
Install the required packages:
```
pip install -e .
```

# Using the tool:
To use this tool place whatever image you want to analyze in the main ColorPalette folder and type the following:
```
./bin/run EXAMPLE_IMAGE.jpg NUM_COLORS
```
In the above, NUM_COLORS refers to the number of colors you want displayed. Additionally, you may follow NUM_COLORS with either a 0 or a 1 to specify whether you would like the hexadecimal color codes of each number to be displayed in the final picture.

# Output
The tool will output two files into the main folder your image was initially in. The first file will be named YOUR_FILE_palette and will contain just the color palette. The second file will be called YOUR_FILE_with_palette and this will contain the original image with the palette below it.

# Examples:
## Image without color names
![alt text](https://github.com/rodartha/ColorPalette/blob/master/Example/fox_with_palette.jpg)

## Image with color names
![alt text](https://github.com/rodartha/ColorPalette/blob/master/Example/Sfox_with_pallete_text.jpg)

# FAQ:
## Will there be a batch edit feature?
Yes, I hope to make one soon.
## How long does it take to run?
This varies wildly based on the size of the image but anywhere from 1 second to a minute
## What file types does it support?
Currently this only works for .jpg and .png images but I hope to expand this in the future

# Notes:
In the future I hope to add real time analysis so that it can display colors as you watch a movie.
