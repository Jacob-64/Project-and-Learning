
# **Photo Date/Time Imprint Script**

### **Overview**

This project was created to solve a specific work-related challenge where photos were taken for audit purposes, but employees lacked a way to automatically imprint a date and time stamp on the images. This script solves that problem by extracting metadata from the image file to impose the date and time stamp. It also provides an option for manually inputting the date and time if the metadata is incomplete or missing.

### **Features**

- **Date/Time Stamp Imprint**: Automatically or manually adds a date and time stamp to photos for audit purposes.
- **Custom Font and Color**: The date and time stamp is imprinted using the Arial font (or default font as a fallback) with a customizable color.
- **Bold Text Effect**: The script simulates a bold effect for the date and time stamp by drawing the text multiple times with slight offsets.
- **Manual Input**: If the metadata is missing or incorrect, the user can manually input the date and time.

### **How It Works**

1. **Image Input**: The script opens an image file from a specified path.
2. **User Input (Optional)**: The user is prompted to input the date and time manually, which can be used to override the image's metadata.
3. **Date/Time Imprint**: The script places the date and time in the bottom-right corner of the image. A bold effect is simulated by drawing the text multiple times with slight offsets.
4. **Save Output**: The image with the date and time stamp is saved in the same directory (or a different directory if specified).

### **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/repo_name.git
   cd repo_name
   ```

2. **Install dependencies**:
   You’ll need the following Python libraries:
   - `Pillow` (Python Imaging Library)

   Install them using pip:
   ```bash
   pip install Pillow
   ```

### **Usage**

1. **Edit the Script**: 
   - Modify the `image_path` variable in the script to point to the image you want to process.
   - Example:
     ```python
     image_path = r'path/to/your/image.jpg'
     ```

2. **Run the Script**:
   The script will prompt you for the date and time to imprint on the image:
   ```bash
   python3 your_script_name.py
   ```

   You will be prompted to enter the date and time in the following format:
   ```
   Please enter the date for the date stamp (e.g., '08 June 2021'): 
   Please enter the time for the date stamp (e.g., '14:32'): 
   ```

   Once the script is executed, the date and time will be added to the image.

3. **Output**:
   - The modified image with the date and time stamp will be saved in the same directory as the original image (or another directory if specified).
   - The output image will retain the original name.

### **Example Output**

Assume the following inputs:
- **Date**: `08 June 2021`
- **Time**: `14:32`

The script will imprint this information on the image in the bottom-right corner, using a bold orange font:

![Example Image](path/to/your/image.jpg)

### **Customization**

- **Font Size and Style**: You can adjust the font size and type by modifying the following line:
   ```python
   font = ImageFont.truetype("arial.ttf", 50)  # Change the font size as needed
   ```
- **Text Color**: The default color is set to orange, but you can modify it by changing the `color` variable:
   ```python
   color = (255, 140, 0)  # RGB values for orange
   ```

- **Text Position**: You can adjust the position of the date and time text by modifying the `margin_right` and `margin_bottom` variables.

### **Error Handling**

- If the Arial font is not found, the script falls back to the default font.
- The script prints any errors encountered during image processing, such as issues with loading the image.

### **Known Limitations**

- This version does not automatically extract the date and time from the image's metadata. However, manual input is provided as an alternative.
- For certain image formats, additional processing might be needed to handle metadata extraction.

### **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Let me know if any further adjustments are needed!
