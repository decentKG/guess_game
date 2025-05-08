import tkinter as tk
import requests

# Your SerpAPI Key Application Progrmming Interface
API_KEY = "your_serpapi_key_here"

# Create a function to query the API
def search_query(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": API_KEY,
        "engine": "google"
    }
    try:
        response = requests.get(url, params=params)
        # Check if the response status code is OK (200)
        if response.status_code == 200:
            # Print the response for debugging
            print(f"Response Status Code: {response.status_code}")
            print(f"API Response: {response.json()}")  # Print the JSON response
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error making request: {e}")
        return None

# Function to process user input and get results
def get_response():
    query = user_input.get()
    if query:
        print(f"User Query: {query}")  # Log user query for debugging
        results = search_query(query)
        
        # Check if results are returned and if organic_results exist
        if results:
            # Check organic results first
            if 'organic_results' in results and len(results['organic_results']) > 0:
                answer = results['organic_results'][0].get('snippet', 'No snippet available.')
            # Check if there are news results
            elif 'news_results' in results and len(results['news_results']) > 0:
                answer = results['news_results'][0].get('snippet', 'No snippet available.')
            # If no results found in organic or news, check paid results
            elif 'paid_results' in results and len(results['paid_results']) > 0:
                answer = results['paid_results'][0].get('snippet', 'No snippet available.')
            else:
                answer = "No results found for this query."
        else:
            answer = "No results found for this query."
        
        print(f"Bot Response: {answer}")  # Log bot response for debugging
        
        chat_box.insert(tk.END, "You: " + query + "\n")
        chat_box.insert(tk.END, "Bot: " + answer + "\n\n")
        user_input.delete(0, tk.END)

# Create the GUI
root = tk.Tk()
root.title("News Chatbot")

# Create a chat box
chat_box = tk.Text(root, height=20, width=60)
chat_box.pack(padx=10, pady=10)

# Create a user input field
user_input = tk.Entry(root, width=50)
user_input.pack(padx=10, pady=10)

# Create a button to send the query
send_button = tk.Button(root, text="Send", command=get_response)
send_button.pack(padx=10, pady=10)

# Start the GUI loop
root.mainloop()