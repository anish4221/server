import google.generativeai as genai
from flask import Flask, jsonify, request, send_file
import os

app = Flask(__name__)
api_key = os.getenv("gemini_API_KEY")
if api_key is None:
    raise ValueError("API_KEY environment variable not set")
genai.configure(api_key=api_key)


@app.route('/api/hello/<question>', methods=['GET'])
def hello(question):
    response = geminiResponse(question)
    return jsonify({"response": response})


def geminiResponse(question):
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
        history=[
        ]
    )
    response = chat_session.send_message(question)
    return response.text


app.run(host='0.0.0.0', port=5000)
