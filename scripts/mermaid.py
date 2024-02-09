import subprocess

def generate_mermaid_flowchart(input_file):
    try:
        # Call the Mermaid CLI to generate SVG from the Mermaid code
        #subprocess.run(['mmdc', '-i', input_file, '-o', 'output.svg'], check=True)
        
        # Read and display the contents of the generated SVG file
        with open('scripts\output.svg', 'r') as svg_file:
            svg_content = svg_file.read()
            print(svg_content)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Specify the path to the input Mermaid file using raw string or escape backslashes
input_mermaid_file = r'D:\Onedrive\Documents\TCSGenAIBot\scripts\input.mmd'

# Call the function with the input file
generate_mermaid_flowchart(input_mermaid_file)
