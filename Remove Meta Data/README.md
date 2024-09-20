
## **Remove PDF Metadata Script**

### **Overview**
This Python script uses the `PyPDF2` library to remove metadata from a PDF file. Metadata includes information such as the author, creation date, modification date, and other document properties. By removing this data, you can create a clean PDF without any traceable information about its origins or edits.

### **Script Breakdown**

1. **Import Libraries:**
   ```python
   from PyPDF2 import PdfReader, PdfWriter
   ```
   - This imports `PdfReader` and `PdfWriter` from the `PyPDF2` library, which are used to read and manipulate PDF files.

2. **Function Definition:**
   ```python
   def remove_metadata(input_pdf_path, output_pdf_path):
   ```
   - This function takes two arguments: 
     - `input_pdf_path`: The path to the original PDF file.
     - `output_pdf_path`: The path where the new PDF without metadata will be saved.

3. **Create PDF Reader and Writer Objects:**
   ```python
   reader = PdfReader(input_pdf_path)
   writer = PdfWriter()
   ```
   - `PdfReader`: Reads the contents of the input PDF.
   - `PdfWriter`: Prepares a new PDF file to write without metadata.

4. **Add Pages to the New PDF:**
   ```python
   for page in reader.pages:
       writer.add_page(page)
   ```
   - The loop iterates through all pages of the input PDF and adds them to the `writer` object, keeping the page content intact.

5. **Remove Metadata:**
   ```python
   writer.add_metadata({})
   ```
   - By setting an empty dictionary `{}`, all existing metadata is stripped from the PDF.

6. **Save the New PDF:**
   ```python
   with open(output_pdf_path, "wb") as f:
       writer.write(f)
   ```
   - The cleaned PDF (without metadata) is saved to the specified `output_pdf_path`.

### **Example Usage**

Replace the `<File location>` and `<File location add desired file name>` in the following example with the appropriate paths for the input and output PDF files:

```python
input_pdf = "path/to/input.pdf"
output_pdf = "path/to/output_clean.pdf"
remove_metadata(input_pdf, output_pdf)
```

This will save a new version of the input PDF file with all metadata removed.

### **Requirements:**

Make sure you have `PyPDF2` installed. You can install it using pip:

```bash
pip install PyPDF2
```

### **How to Use:**
1. Clone the repository containing this script:
   ```bash
   git clone https://github.com/username/repo_name
   ```

2. Navigate to the repository folder:
   ```bash
   cd repo_name
   ```

3. Run the script:
   ```bash
   python3 remove_metadata.py
   ```

4. Replace the file paths in the example usage with the actual paths for your input and output PDF files.

### **Notes:**
- This script does not alter the content of the PDF pages, only the metadata.
- Make sure to specify a different output path, or the original PDF will be overwritten.
- Metadata may contain sensitive information, and removing it is useful for privacy and security.

---

