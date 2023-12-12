from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    input_text = request.json.get('input', '')
    
    # Replace this with the actual logic to run your Python script
    # For simplicity, echoing the input text as output
    output_text = f"Output: {input_text}"

    return jsonify({'output': output_text})

if __name__ == '__main__':
    app.run(debug=True)
