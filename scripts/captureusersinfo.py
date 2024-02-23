import datetime
import getpass
import socket
import os
import openai

# Set up OpenAI API
openai.api_type = "azure"
openai.api_base = "https://genaiusecases.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = 'API_KEY'

# Function to save user information to file
def save_user_info_to_file(username, ip_address):
    try:
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('user_info.txt', 'a') as file:
            file.write(f"{current_datetime}|{username}|{ip_address}\n")
        print("User information saved to 'user_info.txt' successfully.")
    except Exception as e:
        print(f"Error saving user information: {str(e)}")

# Get Windows username
windows_username = getpass.getuser()

# Get IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Save user information to a file
save_user_info_to_file(windows_username, ip_address)

# Set up OpenAI message
message_text = [{"role": "system", "content": "You are an AI assistant that helps people find information."},
                {"role": "user", "content": "Convert below requirement into BDD: An icon shall be selected during detailed design to show a gate in a closed position.\nAn icon shall be selected during detailed design to show a gate in an open position.\nAn icon shall be selected during detailed design to show a gate in a partially open (15%) open position.\nThe gate icon shall be configurable to show the name of the gate with the icon.\nThe gate icon shall be configurable to show the state of the gate (e.g., open or close).\nThe gate icon shall be configurable to show the status of the gate (operational, failed, or no data).  The color of the gate icon shall be changed to show the status of the gate.\nWhen the operator moves the mouse over a gate icon a text window shall be displayed showing a summary of the gate status.  The details of the summary status display will be defined in the GUI design document.\nThe operator shall be able to activate a detailed device status window for the selected gate by double left clicking on the icon.  This action shall cause a circle to be displayed over the gate icon for as long as the detailed device status window is displayed for that gate.\nThe operator shall be able to activate a device control window for the selected gate by right clicking on the icon.  The right click on the icons shall display a pop-up menu of available device actions from which the user may select.  This action shall cause a circle to be displayed over the gate icon for as long as the device control window is displayed for that gate."}]

# Call OpenAI ChatCompletion
completion = openai.ChatCompletion.create(
  engine="AzureOpenAI",
  messages=message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

# Get the generated content from OpenAI response
content = completion['choices'][0]['message']['content']

# Print the generated content
print(content)
