import requests
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

history = []

def generate_response(prompt):
    """
    Takes in a user prompt and appends it to the history of prompts.
    It then sends a request to the API with the concatenated history as the prompt.
    If the response is valid, it returns the response from the server.
    If the response is invalid, it prints an error message to the console
    """
    
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "coder",
        "prompt": final_prompt,   # fixed lowercase
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        actual_response = result.get("response", "")
        return actual_response
    else:
        print("error:", response.text)
        return "Error: " + response.text


interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt here..."),
    outputs="text"
)

interface.launch()



# import requests
# import json
# import gradio as gr

# url="http://localhost:11434/api/generate"

# headers={

#     'Content-Type':'appplication/json'
# }

# history=[]

# def generate_response(prompt):
# /*************  ✨ Windsurf Command ⭐  *************/
#     """
#     Takes in a user prompt and appends it to the history of prompts.
#     It then sends a request to the API with the concatenated history as the prompt.
#     If the response is valid, it returns the response from the server.
#     If the response is invalid, it prints an error message to the console
#     """
    
# /*******  0a517f53-76ec-4da3-b7b6-f7fb8a59e743  *******/
#     history.append(prompt)
#     final_prompt="\n".join(history)
#     data={
#         "model":"coder",
#         "Prompt":final_prompt,
#         "stream":False
#     }

#     response=requests.post(url,headers=headers,data=json.dumps(data))

#     if response.status_code==200:
#         response=response.text
#         data=json.loads(response)
#         actual_response=data["response"]
#         return actual_response
#     else:
#         print("error:",response.text)


# interface=gr.Interface(
#     fn=generate_response,
#     inputs= gr.Textbox(lines=4,placeholder="Enter your prompt here..."),
#     outputs="text"
# )
# interface.launch()