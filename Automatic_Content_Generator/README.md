# Automated Content Generation Tool

This project is an automated content generation tool that generates blog content based on given topics using a language model from Hugging Face, integrated with TensorFlow. The application is built using Flask for the web interface and LangChain for managing the language model interactions.

<img width="726" alt="Screenshot 2024-07-19 at 17 17 45" src="https://github.com/user-attachments/assets/dff805f4-5cb3-4322-bdc0-928e81c412a0">

## Features

- Generates blog content based on user-provided topics.
- Uses Hugging Face's GPT-2 model with TensorFlow for text generation.
- Web interface built with Flask for easy interaction.
- Allows customization of generation parameters like temperature.

## Requirements

- Python 3.8+
- Flask
- TensorFlow
- Transformers (Hugging Face)
- LangChain

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ChandniAk/GenerativeAI/Automatic_Content_Generator.git
    cd content-generator-tool
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask server:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter the topic you want to generate content for and click "Generate".

## Configuration

You can adjust the text generation parameters such as temperature directly in the code:

```python
# Define a prompt template
prompt = f"Generate a detailed blog post on the topic: {topic}"

# Generate text with the Hugging Face model
generated_text = model.generate(
    input_ids=tokenizer.encode(prompt, return_tensors='tf'),
    max_length=500,
    num_return_sequences=1,
    temperature=0.7  # Adjust temperature here
)


