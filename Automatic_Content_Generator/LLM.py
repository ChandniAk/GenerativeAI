import tensorflow as tf
from transformers import TFAutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify, render_template

# Initialize the Hugging Face model and tokenizer
model_name = "gpt2"
model = TFAutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


# Function to generate content
def generate_content(topic, keywords, tone, temperature=0.6):
    # Create the prompt based on the inputs
    prompt = f"Write a {tone} blog post about {topic} mentioning the following keywords: {', '.join(keywords)}."

    # Encode the prompt
    input_ids = tokenizer.encode(prompt, return_tensors='tf')

    # Generate the output
    output = model.generate(input_ids, max_length=150, num_return_sequences=1, temperature=temperature)

    # Decode the output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text


# Flask app setup
app = Flask(__name__)


# Route for rendering the form to input topics
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle form submission and generate content
@app.route('/generate', methods=['POST'])
def generate():
    # Get the data from the POST request
    topic = request.form.get('topic')
    keywords = request.form.get('keywords').split(',')  # assuming keywords are entered as comma-separated values
    tone = request.form.get('tone')

    # Generate the content
    content = generate_content(topic, keywords, tone, temperature=0.6)

    # Return the generated content
    return render_template('blog.html', topic=topic, content=content)


if __name__ == '__main__':
    app.run(debug=True)
