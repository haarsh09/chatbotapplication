# chatbotapplication

# Flight Booking FAQs Chatbot

## Overview
This project is a chatbot designed to assist users with frequently asked questions related to flight bookings. The chatbot is powered by OpenAI's GPT-3.5, using a custom knowledge base created from local documents. The application is built using Streamlit for the web interface.

## Architecture

### Components
1. **Streamlit**: Used to create a simple and interactive web interface for user interaction.
2. **OpenAI GPT-3.5**: The language model used to generate responses.
3. **Llama Index**: Handles document reading and indexing to create a searchable knowledge base.
4. **Environment Variables**: Managed using `dotenv` for secure storage of API keys.

### Directory Structure
chatbot-assignment/
│
├── knowledgebase/ # Directory containing the knowledge base documents
│ ├── document1.txt
│ ├── document2.txt
│ └── ...
├── .env # Environment variables file
├── app.py # Main application script
├── requirements.txt # Dependencies for the project
└── README.md # Project documentation




## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/your-username/flight-booking-faqs.git
    cd flight-booking-faqs
    ```

2. **Create a virtual environment and activate it**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**
    - Create a `.env` file in the root directory and add your OpenAI API key:
    ```sh
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the application**
    ```sh
    streamlit run app.py
    ```

## Design Decisions

### Use of Streamlit
Streamlit was chosen for its simplicity and ease of creating interactive web applications. It allows for rapid prototyping and provides an intuitive interface for users to interact with the chatbot.

### OpenAI GPT-3.5
GPT-3.5 was selected due to its powerful language understanding and generation capabilities. By using a pretrained model, the chatbot can generate coherent and contextually appropriate responses.

### Llama Index
Llama Index is used to handle the knowledge base. It provides a simple API to read documents from a directory and create an index that can be queried. This is essential for integrating the custom knowledge base with GPT-3.5.

### Environment Variables
Using the `dotenv` package ensures that sensitive information, such as API keys, is kept secure and not hardcoded into the source code. This approach also makes it easier to manage configurations across different environments (development, production, etc.).

## Implementation Details

### Loading the Knowledge Base
```python
reader = SimpleDirectoryReader(input_dir='C:\\Users\\Harsh Pathak\\Desktop\\chatbotassignment\\knowledgebase', recursive=True)
docs = reader.load_data()

This documentation covers the key aspects of your project, including an overview, architecture, installation instructions, design decisions, and implementation details. It should provide a comprehensive guide for anyone looking to understand or deploy your chatbot.
