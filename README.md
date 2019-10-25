# ColorPalette
Find the dominant colors in any image

# Setup Instructions:
## Step 1)
Make sure you have python installed on your machine

## Step 2)
navigate into the main directory ColorPallete and create a python virtual environment as follows:
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
To use this tool place whatever image you want to analyze in the main ColorPallete folder and type the following:
```
./bin/run EXAMPLE_IMAGE.jpg NUM_COLORS
```
In the above, NUM_COLORS refers to the number of colors you want displayed. Additionally, you may follow NUM_COLORS with either a 0 or a 1 to specify whether you would like the hexadecimal color codes of each number to be displayed in the final picture.

# Output
The tool will output two files into the main folder your image was initially in. The first file will be named YOUR_FILE_palette and will contain just the color palette. The second file will be called YOUR_FILE_with_palette and this will contain the original image with the palette below it.

# Notes:
A batch edit feature will be coming in the future.
