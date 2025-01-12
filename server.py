import os
from flask import Flask, render_template, render_template_string, request
from flask_cors import CORS

app = Flask(__name__, template_folder=".")
CORS(app) # Enable CORS to allow requets

@app.route("/", methods=["GET"]) # Allow only GET to this endpoint
def index():
    """
    Return the provided html file.
    """
    assert os.path.exists("index.html")
    return render_template("index.html")

@app.route("/result", methods=["POST"]) # Allow only POST to this endpoint
def generate_result():
    """
    Get 2 parameters from frontent a and b. 
    Sum them and return them to the requester.
    """
    data = request.json

    assert data is not None # Make sure there is data in the POST request

    a = data.get("a", "") # Get parameter a 
    b = data.get("b", "") # Get parameter a 

    try:
        result_a = eval(a) if a else "" # Evaluate the data to make sure it is correct
        result_b = eval(b) if b else ""
        result = f"{a} + {b} = {result_a + result_b}"
    except Exception as e:
        result = f"Eroare: {e}"

    return render_template_string(result) # Send back the response

if __name__ == "__main__":
    app.run(debug=True)
