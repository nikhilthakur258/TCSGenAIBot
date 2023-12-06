from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Generate_Requirements')
def Generate_Requirements():
    return render_template('Generate_Requirements.html')
    
@app.route('/Generate_TestCases')
def Generate_TestCases():
    return render_template('Generate_TestCases.html')
    
@app.route('/Generate_APITestCases')
def Generate_APITestCases():
    return render_template('Generate_APITestCases.html')   
    

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        data = request.get_json()
        script_path = os.path.join('scripts', data['scriptPath'])  # Adjust the path
        input_text = data['inputText']

        # Run the Python script using subprocess
        result = subprocess.check_output(['python', script_path, input_text], text=True)

        return jsonify(success=True, output=result)
    except subprocess.CalledProcessError as e:
        print(f"CalledProcessError: {e}")
        print(f"Output: {e.output}")
        return jsonify(success=False, error=e.output)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify(success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
