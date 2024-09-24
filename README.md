# OCR and Document Search Web Application Prototype

This is a simple web-based prototype that demonstrates Optical Character Recognition (OCR) on uploaded images containing text in both Hindi and English. It also includes a basic keyword search functionality based on the extracted text.

## Table of Contents
- [Objective](#objective)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Objective
The goal of this project is to:
- Extract text from an uploaded image using OCR.
- Perform keyword searches on the extracted text.
- Provide a live URL where users can access and use the application.

## Features
- Upload an image in JPEG, PNG, or other common picture formats.
- Extract text from the image using OCR (supports Hindi and English).
- Perform keyword-based searches within the extracted text.
- Display search results and highlight matching sections.

## Technologies Used
- **Python 3.x**
- **Streamlit** - For creating the web application interface.
- **Pytesseract** - For performing OCR on the uploaded image.
- **PIL (Python Imaging Library)** - For image processing.
- **Huggingface Transformers** and **PyTorch** (optional) - For advanced OCR models.
  
## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ocr-document-search-app.git
cd ocr-document-search-app
```

### 2. Install Dependencies
Ensure you have Python 3.x installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```
Alternatively, you can install the libraries manually:
```bash
pip install streamlit pytesseract Pillow transformers torch
```

### 3. Install Tesseract OCR
- **Linux**: 
  ```bash
  sudo apt-get install tesseract-ocr
  ```
- **MacOS** (with Homebrew):
  ```bash
  brew install tesseract
  ```
- **Windows**: 
  Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).

### 4. Run the Application
After setting up the environment, run the application:
```bash
streamlit run app.py
```

This will start the application, and it will be accessible locally at `http://localhost:8501`.

## Usage

1. Open the web application.
2. Upload an image that contains text in Hindi, English, or both.
3. The application will display the extracted text.
4. Enter a keyword in the search box to find and highlight matching text within the extracted content.

## Deployment

The app has been deployed and is accessible via the following URL:

[Live Demo](https://yourappname.streamlitapp.com)

You can deploy this app using platforms like **Streamlit Sharing** or **Hugging Face Spaces**. 

### Deployment Steps on Streamlit Sharing:
1. Push the project to a public GitHub repository.
2. Go to [Streamlit Sharing](https://streamlit.io/sharing).
3. Connect your GitHub account, select your repository, and deploy.

## Examples

- **Extracted Text Example**: An uploaded image with Hindi and English text will show the extracted content on the page.
- **Search Example**: If you search for a word (e.g., "example"), the application will highlight all occurrences of that word in the extracted text.

## Contributing

Feel free to submit issues or pull requests to help improve the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:
- Ensure the `requirements.txt` file includes all necessary dependencies:
  ```
  streamlit
  pytesseract
  Pillow
  transformers
  torch
  ```

