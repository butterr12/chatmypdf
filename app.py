import os
import tempfile
import pandas as pd
import streamlit as st
from pinecone import Pinecone
from groq import Groq
from index import process_pdfs
from chatbot import generate_response

# Constants
CSV_FILE = "indexes.csv"
pc = Pinecone(api_key=st.secrets.pinecone_key, environment="us-east-1")

def save_index_info(index_name, chatbot_name, chatbot_description):
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        if index_name not in df['index_name'].values:
            new_row = {"index_name": index_name, "chatbot_name": chatbot_name, "chatbot_description": chatbot_description}
            new_df = pd.DataFrame(new_row, index=[0])
            df = pd.concat([df, new_df], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
    else:
        df = pd.DataFrame([{"index_name": index_name, "chatbot_name": chatbot_name, "chatbot_description": chatbot_description}])
        df.to_csv(CSV_FILE, index=False)

# Sidebar content
with st.sidebar:
    st.markdown("""
        <style>
            .title-gradient {
                background: linear-gradient(to right, #6a11cb, #2575fc); 
                -webkit-background-clip: text;
                color: transparent;
                font-size: 30px !important;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="title-gradient">PDF-Powered Chatbot</p>', unsafe_allow_html=True)
    
    st.markdown("""
    

    This chatbot can read and understand the contents of your PDF documents. 
    Upload your files, define an index, and start chatting with the information they contain.
    """)

    st.markdown("""
    ### 🎯 Try it Out!

    I've gone ahead and uploaded a sample PDF all about COVID-19 — feel free to check it out!  

    [Check out the PDF here!](https://www.jmir.org/2020/9/e21279/PDF)

    Once you’ve had a look, ask the chatbot some questions related to the document and see it in action.

    Just remember to select the index **med-bot-2** (that’s where I’ve stored the PDF).

    **Need some inspiration?**  
    - Try asking: "What's the result of the study?"

    """)

page = st.sidebar.selectbox("Select a page", ["Chatbot", "PDF Processor"])

# === Chatbot Page ===
if page == "Chatbot":
    st.header("Chatbot")

    st.markdown("""
    ### Here's how to get started:

    1. If you want to start chatting with the uploaded sample PDF, simply select the med-bot-2 index and begin asking questions related to the [document](https://www.jmir.org/2020/9/e21279/PDF).
    2. If you'd like to upload your own PDF document, head to the **PDF Processor** page using the sidebar. There, you'll need to provide an index name, chatbot name, and description before uploading your file.
    3. Happy chatting!
    """)

    with st.sidebar:
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
            st.header("Existing Index Metadata")
            st.dataframe(df)
        else:
            st.warning("No index info available yet.")

    if "history" not in st.session_state:
        st.session_state.history = []

    available_indexes = pc.list_indexes().names()
    if available_indexes:
        index_name = st.selectbox("Select an index", available_indexes)
        user_input = st.text_input("Ask something:")
        if user_input:
            response = generate_response(user_input, index_name)
            st.session_state.history.append({"user": user_input, "bot": response})
            chat = st.session_state.history[-1]
            st.write(f"You: {chat['user']}")
            st.write(f"Bot: {chat['bot']}")
    else:
        st.warning("No indexes available yet. Please process some PDFs first.")

# === PDF Processor Page ===
elif page == "PDF Processor":
    st.header("PDF Processor")

    st.markdown("""
    ### Set-up the details:

    1. Set an **index name** for your document (e.g., "covid19-index" or any name you prefer).
    2. Provide a **chatbot name** (e.g., "COVID19 Assistant" or any name you choose).
    3. Write a **chatbot description** (e.g., "A chatbot that answers questions based on the uploaded COVID19 document").

    Once you upload the PDF and define these fields, you can start chatting with the information contained in the document by heading back to **Chatbot** page!
    """)


    index_name = st.text_input("Index Name")
    chatbot_name = st.text_input("Chatbot Name")
    chatbot_description = st.text_input("Chatbot Description")

    uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        st.header("Existing Index Metadata")
        st.dataframe(df)
    else:
        st.warning("No index information available yet.")

    if st.button("Process PDFs"):
        with st.spinner("Processing your PDFs..."):
            if uploaded_files and index_name and chatbot_name and chatbot_description:
                save_index_info(index_name, chatbot_name, chatbot_description)
                with tempfile.TemporaryDirectory() as temp_dir:
                    for uploaded_file in uploaded_files:
                        temp_path = os.path.join(temp_dir, uploaded_file.name)
                        with open(temp_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                    process_pdfs(temp_dir, index_name)
                st.success("PDFs processed and indexed successfully.")
            else:
                st.error("Please upload PDFs and fill out all required fields.")
