
# **SANS PDF Indexing Project**

### **Overview**

This project automates the initial indexing of SANS PDF textbooks by extracting key terms and definitions from each page. The extracted data is then stored in a CSV file, allowing for easier reference and study. The project utilizes the `PyPDF2`, `pdfplumber`, and `OpenAI` APIs to process the text and prompt OpenAI to identify important cybersecurity, cloud, and threat detection terms.

### **Features**

- **PDF Processing**: Extracts text from each page of a PDF.
- **OpenAI Integration**: Uses OpenAI's GPT model to analyze each page and identify key terms and definitions.
- **Dynamic Term Parsing**: Handles multiple formats (colon `:`, dash `-`, comma `,`) to extract terms and their respective definitions.
- **CSV Output**: Saves the results in a CSV file, with terms, page numbers, and concise definitions.

### **How It Works**

1. **PDF Processing**: The script processes SANS textbooks in PDF format and extracts text from each page.
2. **Prompting OpenAI**: It prompts OpenAI to identify and define the most crucial terms or concepts on the page, focusing on topics like cybersecurity, cloud, and threat detection.
3. **Term and Definition Extraction**: The script uses a flexible parsing approach to extract terms and definitions, which are stored in a dictionary.
4. **CSV Export**: After processing the entire PDF, the script converts the extracted terms into a CSV file, making it easy to reference the index.

### **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/repo_name.git
   cd repo_name
   ```

2. **Install dependencies**:
   You’ll need the following Python libraries:
   - `pdfplumber`
   - `openai`
   - `python-dotenv`
   - `pandas`

   Install them using pip:
   ```bash
   pip install pdfplumber openai python-dotenv pandas
   ```

3. **Create a `.env` file**:
   Add your OpenAI API key and the password for your PDF files (if needed):
   ```
   OPENAI_API_KEY=your_openai_api_key
   PDF_PASSWORD=your_pdf_password
   ```

### **Usage**

1. Place the SANS PDF textbooks you want to index in a folder named `Books` in the root directory of the project. Ensure the files match the pattern `FOR500_[BW]*.pdf` (you can modify the pattern in the script if necessary).

2. Run the script:
   ```bash
   python3 your_script_name.py
   ```

   The script will process each PDF in the folder, prompt OpenAI for the key terms, and generate a CSV file containing the index.

3. **CSV Output**: After processing, you will find a CSV file in the same directory as the PDF. The CSV will have the following columns:
   - **Term**: The key term extracted from the page.
   - **Pages**: A list of pages where the term appears.
   - **Definition**: A concise definition provided by OpenAI.

### **Example Output**
The CSV file will look like this:

| Term           | Pages     | Definition                                                          |
|----------------|-----------|---------------------------------------------------------------------|
| Cloud Security | 1, 3, 5   | A set of practices to protect cloud environments from cyber threats. |
| MITRE ATT&CK   | 2         | A framework for classifying adversary tactics and techniques.        |
| Threat Detection | 4       | The process of identifying cyber threats in real time.               |

### **OpenAI Prompting Strategy**

The script prompts OpenAI with a custom task to identify the most relevant term or concept on each page of the textbook. It focuses on:
- **Cloud**: Topics related to cloud computing and security.
- **Cybersecurity**: Terms that pertain to defensive and offensive strategies.
- **Threat Detection**: Tools and techniques used to detect and respond to threats.

If the page does not contain relevant material, OpenAI responds with "none," ensuring that irrelevant pages (like title pages) are excluded.

### **Customization**

- **PDF Pattern**: You can modify the pattern for PDF files in the script to match other textbooks by changing the `glob.glob('./Books/FOR500_[BW]*.pdf')` line.
- **OpenAI Prompt**: The prompt provided to OpenAI can be adjusted based on what kind of indexing you need. You can refine the focus by changing the `prompt` variable within the `process_pdf()` function.

### **Error Handling**

- **Rate Limiting**: If OpenAI's API rate limit is exceeded, the script will pause and retry after 60 seconds.
- **Unclear Terms**: If OpenAI provides unclear or partial matches, the script logs these for review.

### **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

