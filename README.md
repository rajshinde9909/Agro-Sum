# AgroSum: Agricultural Report Summarizer

A Streamlit web application that uses AI to summarize agricultural reports and documents.

## Features

- **Text Input**: Paste text directly for summarization
- **PDF Upload**: Upload PDF files to extract and summarize text
- **AI-Powered Summarization**: Uses Facebook's BART model for high-quality summaries
- **Key Terms Extraction**: Identifies the most frequent terms in the document
- **User-Friendly Interface**: Clean and intuitive Streamlit interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Rajshinde9909/Agro-Sum.git
cd LLM_DOC_Summ
```

2. Create a virtual environment:
```bash
python -m venv my_env
```

3. Activate the virtual environment:
```bash
# On Windows
my_env\Scripts\activate

# On macOS/Linux
source my_env/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run agrisum.py
```

2. Open your web browser and go to the URL shown in the terminal (usually `http://localhost:8501`)

3. Choose your input method:
   - **Paste Text**: Copy and paste your agricultural report text
   - **Upload PDF**: Upload a PDF file containing your report

4. Click "Generate Summary" to get an AI-powered summary

## Technologies Used

- **Streamlit**: Web application framework
- **Transformers**: Hugging Face library for AI models
- **BART**: Facebook's BART model for text summarization
- **NLTK**: Natural language processing toolkit
- **PyPDF2**: PDF text extraction

## Requirements

See `requirements.txt` for all dependencies.

## License

This project is open source and available under the MIT License.

