# ChatMyPDF - Unlock the Power of Your PDFs

Welcome to **ChatMyPDF**! This is your personal chatbot that interacts with your PDF papers. Whether you're in research, business, education, or any field, ChatMyPDF makes it easy to extract valuable insights from your documents. Built using **Retrieval-Augmented Generation (RAG)** technology, ChatMyPDF pulls relevant documents from an indexed database and generates responses that are both detailed and contextually accurate.

## Try It Out!
Want to see **ChatMyPDF** in action? It’s live on HuggingFace Spaces! Check it out and start chatting with your PDFs instantly:

[![ChatMyPDF Demo](https://github.com/Sakalya100/AutoTabML/blob/main/Sample%20Data/5229488.png)]()

## Key Features

- **Efficient Document Indexing:** Upload your PDFs once, and ChatMyPDF will index them for quick retrieval, so you don’t have to re-upload. Create different chatbots for different categories of research papers.
- **Contextual Responses:** ChatMyPDF utilizes the powerful **Llama-7B** model with **Pinecone** as the vector database to provide contextual, accurate answers based on your PDF documents.
- **Modular & Expandable:** The modular design allows easy expansion and integration with various data sources for future updates and use cases.

## Tech Stack
ChatMyPDF uses a variety of technologies to deliver its powerful features:

- **Pinecone**: Vector database for fast document retrieval
- **Streamlit**: Frontend interface to interact with the chatbot
- **HuggingFace**: Hosting platform for the app
- **Python**: Backend logic for processing and model interactions
- **Llama-7B (Groq API)**: The model that powers the chatbot’s responses
- **Sentence-Transformers (Embedding)**: For embedding and retrieving document content

## Installation Guide

1. **Clone the repository**:
    ```bash
    git clone https://github.com/butterr12/chatmypdf.git
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use ChatMyPDF

Getting started is simple:

1. **Index Your PDFs**: Use the `index.py` script to index your PDF documents, or use the client interface for a more seamless indexing process.
   
2. **Start the Chatbot**: To launch the chatbot, run:
    ```bash
    streamlit run app.py
    ```

3. **Interact**: Open the client interface, and start chatting with your PDF assistant!

## Files Overview

Here’s a quick overview of the project files:

- **README.md**: This file with all the info.
- **app.py**: The main entry point to start the chatbot.
- **chatbot.py**: Core logic for handling chatbot interactions.
- **index.py**: Script for indexing PDF documents.
- **indexes.csv**: Contains indexed PDFs and Pinecone details.
- **requirements.txt**: List of dependencies for the project.

## License

This project is licensed under the **MIT License**. Feel free to use, modify, and share!

## Need Help?

If you have any questions or need help, don’t hesitate to open an issue in the repository. I'm usually responsive!
