from gpt4all import GPT4All

model_path = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
gpt = GPT4All(model_path)

def askGPT(text):
    prompt = f"""
    You are a helpful assistant. Please extract the following details from the receipt text:
    1. List of items with their prices.
    2. Total amount.
    3. Purchase date.

    Here is the receipt text:
    {text}

    ONLY PROVIDE the output in this JSON format. Do not include any other information.:
    {{
        "Shop": <Name of Store/Shop>
        "items": [
            {{"item": "<Item Name>", "price": <Price>}},
            ...
        ],
        "total": <Total Amount>,
        "date": "<Purchase Date>"
    }}
    """

    response = gpt.generate(prompt)
    return response