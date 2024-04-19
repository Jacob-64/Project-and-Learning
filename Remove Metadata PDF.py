from PyPDF2 import PdfReader, PdfWriter

def remove_metadata(input_pdf_path, output_pdf_path):
    # Create a PDF reader object
    reader = PdfReader(input_pdf_path)
    
    # Create a PDF writer object
    writer = PdfWriter()
    
    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)
    
    # Set document info to an empty dictionary to remove metadata
    writer.add_metadata({})

    # Write the output PDF file
    with open(output_pdf_path, "wb") as f:
        writer.write(f)

# Example usage
input_pdf = "<File location> "
output_pdf = "<File location add desired file name> "
remove_metadata(input_pdf, output_pdf)
