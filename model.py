from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch, pickle
url: str = "t5-small"
tokenizer = AutoTokenizer.from_pretrained(url)
model = AutoModelForSeq2SeqLM.from_pretrained(url)


input_text = "translate English to French: Hello"
input_ids = torch.tensor(tokenizer.encode(input_text)).unsqueeze(0)

outputs = model.generate(input_ids, max_length=50)
predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Input:", input_text)
print("Translation:", predicted_text)

with open("modelTokenizer.pkl", "wb") as f:
    pickle.dump([model,tokenizer], f)