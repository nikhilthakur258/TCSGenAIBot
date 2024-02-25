import openai
import requests
from datetime import datetime, timedelta

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Set your Jira API credentials and URL
jira_username = 'YOUR_JIRA_USERNAME'
jira_token = 'YOUR_JIRA_API_TOKEN'
jira_url = 'YOUR_JIRA_URL'

def get_recent_jira_data():
    # Calculate the date 6 months ago from today
    six_months_ago = (datetime.now() - timedelta(days=180)).isoformat()

    # Define Jira JQL query to retrieve issues created or updated in the last 6 months
    jql_query = f"created >= '{six_months_ago}' OR updated >= '{six_months_ago}'"

    # Jira REST API endpoint for searching issues
    jira_search_url = f"{jira_url}/rest/api/3/search"

    # Set up headers for Jira API request
    headers = {
        "Accept": "application/json",
    }

    # Set up Jira API request parameters
    params = {
        "jql": jql_query,
        "maxResults": 100,  # You may adjust this based on your needs
    }

    # Basic authentication for Jira API
    auth = (jira_username, jira_token)

    # Make the Jira API request
    response = requests.get(jira_search_url, headers=headers, params=params, auth=auth)

    if response.status_code == 200:
        # Parse and return the relevant Jira data
        jira_data = response.json().get('issues', [])
        return jira_data
    else:
        print(f"Failed to fetch Jira data. Status Code: {response.status_code}")
        return None

def generate_response(prompt, jira_data):
    # Use OpenAI's GPT-3 for generative language model
    model_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None
    )
    
    # Retrieve Jira data based on the generated content
    jira_response = retrieve_jira_data(model_response['choices'][0]['text'], jira_data)
    
    # Combine the model output with Jira data
    combined_response = f"{model_response['choices'][0]['text']}\n\nSupplemental Jira Data:\n{jira_response}"
    
    return combined_response

def retrieve_jira_data(generated_text, jira_data):
    # Use a simple keyword-based retrieval for Jira data
    relevant_issues = []

    for issue in jira_data:
        if issue.get('fields'):
            summary = issue['fields'].get('summary', '')
            description = issue['fields'].get('description', '')
            
            if summary.lower() in generated_text.lower() or description.lower() in generated_text.lower():
                relevant_issues.append(issue)

    # Convert relevant Jira data to a formatted string
    jira_response = ""
    for issue in relevant_issues:
        jira_response += f"Summary: {issue['fields']['summary']}\nDescription: {issue['fields']['description']}\n\n"

    return jira_response

# Example usage
prompt_text = "Describe the solution architecture for the new feature"
jira_data_recent = get_recent_jira_data()

if jira_data_recent:
    result = generate_response(prompt_text, jira_data_recent)
    print(result)
