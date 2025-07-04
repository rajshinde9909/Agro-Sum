import streamlit as st
from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize
import PyPDF2
import io

# Download NLTK data
nltk.download('punkt')

# Initialize Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to preprocess text (split into chunks if too long)
def preprocess_text(text, max_length=1000):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_length:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# Function to summarize text
def summarize_text(text):
    chunks = preprocess_text(text)
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return " ".join(summaries)

# Streamlit app
st.title("AgriSum: Agricultural Report Summarizer")
st.write("Upload a report or paste text to generate a concise summary.")

# Option to upload PDF or paste text
input_option = st.radio("Choose input method:", ("Paste Text", "Upload PDF"))

if input_option == "Paste Text":
    input_text = st.text_area("Paste your report text here:", height=200)
else:
    uploaded_file = st.file_uploader("Upload a PDF report", type=["pdf"])
    input_text = ""
    if uploaded_file:
        input_text = extract_text_from_pdf(uploaded_file)

# Summarize button
if st.button("Generate Summary"):
    if input_text:
        with st.spinner("Generating summary..."):
            summary = summarize_text(input_text)
            st.subheader("Summary")
            st.write(summary)
    else:
        st.error("Please provide text or upload a file.")

# Optional: Key term extraction (basic example using NLTK)
if input_text:
    st.subheader("Key Terms (Sample)")
    words = nltk.word_tokenize(input_text.lower())
    freq = nltk.FreqDist(words)
    common_words = [word for word, count in freq.most_common(10) if word.isalpha()]
    st.write(", ".join(common_words))