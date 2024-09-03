from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text(prompt):
    model_name = 'gpt2'
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=100, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

prompt = "In a galaxy far, far away, there was a planet known for its mysterious inhabitants. One day, a young explorer named Zara arrived on this planet with a mission to uncover its secrets."
generated_text = generate_text(prompt)
print(generated_text)