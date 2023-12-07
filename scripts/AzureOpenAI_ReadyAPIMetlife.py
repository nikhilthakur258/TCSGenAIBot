import openai
import argparse

# Set up OpenAI API key
openai.api_key = '7f66b5661345437d80e661020d74a2c9'
openai.api_base = 'https://genaiusecases.openai.azure.com/'
openai.api_type = 'azure'
openai.api_version = '2023-07-01-preview'  # this may change in the future
deployment_name = 'OpenAIPOC'
output_file = "Requirement_UI.txt"


# Function to generate test cases using OpenAI GPT-3
def generate_test_cases(description_to_append):
    #prompt = description_to_append
    #response = openai.Completion.create(engine=deployment_name, prompt=prompt, temperature=0.0, max_tokens=2000,
                                        #top_p=0.95, frequency_penalty=0, presence_penalty=0, stop=None)
    with open('scripts/MetLife_API_output/readyAPI.txt') as f:
        content = f.read()                           
        print(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transform requirements into Gherkins")
    parser.add_argument("cleaned_description", help="Cleaned description to use for generating test cases.")
    
    args = parser.parse_args()

    try:
        # Use provided cleaned_description
        cleaned_description = "Write code in Java selenium to test below scenario: \n" + args.cleaned_description

        # Append to file
        with open(output_file, 'w') as file:
            file.write(cleaned_description)

        # Generate test cases
        generated_test_cases = generate_test_cases(cleaned_description)

    except Exception as e:
        print(f"An error occurred: {e}")
