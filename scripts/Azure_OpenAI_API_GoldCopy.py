#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://genaiusecases.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = 'API_KEY'

message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"Convert below requirement into BDD: An icon shall be selected during detailed design to show a gate in a closed position.\nAn icon shall be selected during detailed design to show a gate in an open position.\nAn icon shall be selected during detailed design to show a gate in a partially open (15%) open position.\nThe gate icon shall be configurable to show the name of the gate with the icon.\nThe gate icon shall be configurable to show the state of the gate (e.g., open or close).\nThe gate icon shall be configurable to show the status of the gate (operational, failed, or no data).  The color of the gate icon shall be changed to show the status of the gate.\nWhen the operator moves the mouse over a gate icon a text window shall be displayed showing a summary of the gate status.  The details of the summary status display will be defined in the GUI design document.\nThe operator shall be able to activate a detailed device status window for the selected gate by double left clicking on the icon.  This action shall cause a circle to be displayed over the gate icon for as long as the detailed device status window is displayed for that gate.\nThe operator shall be able to activate a device control window for the selected gate by right clicking on the icon.  The right click on the icons shall display a pop-up menu of available device actions from which the user may select.  This action shall cause a circle to be displayed over the gate icon for as long as the device control window is displayed for that gate."}]

completion = openai.ChatCompletion.create(
  engine="AzureOpenAI",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

content = completion['choices'][0]['message']['content']
print(content)