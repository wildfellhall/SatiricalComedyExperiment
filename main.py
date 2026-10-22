"""
Cell 1: Define corpus and process text
"""

import os
import re
import urllib.request
from datasets import Dataset

import os
import re
import urllib.request
from datasets import Dataset

# All 100 URLs updated to the https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt format
sources = [
    "https://www.gutenberg.org/cache/epub/1080/pg1080.txt",
    "https://www.gutenberg.org/cache/epub/829/pg829.txt",
    "https://www.gutenberg.org/cache/epub/4737/pg4737.txt",
    "https://www.gutenberg.org/cache/epub/1090/pg1090.txt",
    "https://www.gutenberg.org/cache/epub/121/pg121.txt",
    "https://www.gutenberg.org/cache/epub/86/pg86.txt",
    "https://www.gutenberg.org/cache/epub/599/pg599.txt",
    "https://www.gutenberg.org/cache/epub/3178/pg3178.txt",
    "https://www.gutenberg.org/cache/epub/883/pg883.txt",
    "https://www.gutenberg.org/cache/epub/1906/pg1906.txt",
    "https://www.gutenberg.org/cache/epub/4558/pg4558.txt",
    "https://www.gutenberg.org/cache/epub/897/pg897.txt",
    "https://www.gutenberg.org/cache/epub/2686/pg2686.txt",
    "https://www.gutenberg.org/cache/epub/2675/pg2675.txt",
    "https://www.gutenberg.org/cache/epub/2731/pg2731.txt",
    "https://www.gutenberg.org/cache/epub/2844/pg2844.txt",
    "https://www.gutenberg.org/cache/epub/2823/pg2823.txt",
    "https://www.gutenberg.org/cache/epub/2796/pg2796.txt",
    "https://www.gutenberg.org/cache/epub/1935/pg1935.txt",
    "https://www.gutenberg.org/cache/epub/2859/pg2859.txt",
    "https://www.gutenberg.org/cache/epub/61072/pg61072.txt",
    "https://www.gutenberg.org/cache/epub/20001/pg20001.txt",
    "https://www.gutenberg.org/cache/epub/19942/pg19942.txt",
    "https://www.gutenberg.org/cache/epub/1081/pg1081.txt",
    "https://www.gutenberg.org/cache/epub/45858/pg45858.txt",
    "https://www.gutenberg.org/cache/epub/10430/pg10430.txt",
    "https://www.gutenberg.org/cache/epub/968/pg968.txt",
    "https://www.gutenberg.org/cache/epub/652/pg652.txt",
    "https://www.gutenberg.org/cache/epub/44520/pg44520.txt",
    "https://www.gutenberg.org/cache/epub/5231/pg5231.txt",
    "https://www.gutenberg.org/cache/epub/619/pg619.txt",
    "https://www.gutenberg.org/cache/epub/7381/pg7381.txt",
    "https://www.gutenberg.org/cache/epub/27533/pg27533.txt",
    "https://www.gutenberg.org/cache/epub/21816/pg21816.txt",
    "https://www.gutenberg.org/cache/epub/6053/pg6053.txt",
    "https://www.gutenberg.org/cache/epub/1051/pg1051.txt",
    "https://www.gutenberg.org/cache/epub/3190/pg3190.txt",
    "https://www.gutenberg.org/cache/epub/3172/pg3172.txt",
    "https://www.gutenberg.org/cache/epub/21822/pg21822.txt",
    "https://www.gutenberg.org/cache/epub/10095/pg10095.txt",
    "https://www.gutenberg.org/cache/epub/6758/pg6758.txt",
    "https://www.gutenberg.org/cache/epub/6761/pg6761.txt",
    "https://www.gutenberg.org/cache/epub/4092/pg4092.txt",
    "https://www.gutenberg.org/cache/epub/2329/pg2329.txt",
    "https://www.gutenberg.org/cache/epub/2615/pg2615.txt",
    "https://www.gutenberg.org/cache/epub/1473/pg1473.txt",
    "https://www.gutenberg.org/cache/epub/21337/pg21337.txt",
    "https://www.gutenberg.org/cache/epub/38411/pg38411.txt",
    "https://www.gutenberg.org/cache/epub/9909/pg9909.txt",
    "https://www.gutenberg.org/cache/epub/2075/pg2075.txt",
    "https://www.gutenberg.org/cache/epub/1079/pg1079.txt",
    "https://www.gutenberg.org/cache/epub/804/pg804.txt",
    "https://www.gutenberg.org/cache/epub/20257/pg20257.txt",
    "https://www.gutenberg.org/cache/epub/58070/pg58070.txt",
    "https://www.gutenberg.org/cache/epub/46621/pg46621.txt",
    "https://www.gutenberg.org/cache/epub/46622/pg46622.txt",
    "https://www.gutenberg.org/cache/epub/12793/pg12793.txt",
    "https://www.gutenberg.org/cache/epub/4793/pg4793.txt",
    "https://www.gutenberg.org/cache/epub/55035/pg55035.txt",
    "https://www.gutenberg.org/cache/epub/67888/pg67888.txt",
    "https://www.gutenberg.org/cache/epub/39726/pg39726.txt",
    "https://www.gutenberg.org/cache/epub/46467/pg46467.txt",
    "https://www.gutenberg.org/cache/epub/3191/pg3191.txt",
    "https://www.gutenberg.org/cache/epub/19484/pg19484.txt",
    "https://www.gutenberg.org/cache/epub/60900/pg60900.txt",
    "https://www.gutenberg.org/cache/epub/30343/pg30343.txt",
    "https://www.gutenberg.org/cache/epub/41950/pg41950.txt",
    "https://www.gutenberg.org/cache/epub/46125/pg46125.txt",
    "https://www.gutenberg.org/cache/epub/75943/pg75943.txt",
    "https://www.gutenberg.org/cache/epub/47427/pg47427.txt",
    "https://www.gutenberg.org/cache/epub/21514/pg21514.txt",
    "https://www.gutenberg.org/cache/epub/12803/pg12803.txt",
    "https://www.gutenberg.org/cache/epub/7089/pg7089.txt",
    "https://www.gutenberg.org/cache/epub/6453/pg6453.txt",
    "https://www.gutenberg.org/cache/epub/66123/pg66123.txt",
    "https://www.gutenberg.org/cache/epub/73620/pg73620.txt",
    "https://www.gutenberg.org/cache/epub/23390/pg23390.txt",
    "https://www.gutenberg.org/cache/epub/2164/pg2164.txt",
    "https://www.gutenberg.org/cache/epub/77997/pg77997.txt",
    "https://www.gutenberg.org/cache/epub/77028/pg77028.txt",
    "https://www.gutenberg.org/cache/epub/26481/pg26481.txt",
    "https://www.gutenberg.org/cache/epub/623/pg623.txt",
    "https://www.gutenberg.org/cache/epub/5225/pg5225.txt",
    "https://www.gutenberg.org/cache/epub/581/pg581.txt",
    "https://www.gutenberg.org/cache/epub/28105/pg28105.txt",
    "https://www.gutenberg.org/cache/epub/39119/pg39119.txt",
    "https://www.gutenberg.org/cache/epub/51017/pg51017.txt",
    "https://www.gutenberg.org/cache/epub/68133/pg68133.txt",
    "https://www.gutenberg.org/cache/epub/29189/pg29189.txt",
    "https://www.gutenberg.org/cache/epub/31155/pg31155.txt",
    "https://www.gutenberg.org/cache/epub/70039/pg70039.txt",
    "https://www.gutenberg.org/cache/epub/158/pg158.txt",
    "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
    "https://www.gutenberg.org/cache/epub/75845/pg75845.txt",
    "https://www.gutenberg.org/cache/epub/75432/pg75432.txt",
    "https://www.gutenberg.org/cache/epub/78245/pg78245.txt",
    "https://www.gutenberg.org/cache/epub/69793/pg69793.txt",
    "https://www.gutenberg.org/cache/epub/76013/pg76013.txt",
    "https://www.gutenberg.org/cache/epub/996/pg996.txt",
    "https://www.gutenberg.org/cache/epub/1200/pg1200.txt"
]

def expurgate_gutenberg(text):
    # 1. Strip Legal License Headers and Footers
    start_match = re.search(r"\*\*\*\s*START OF TH(IS|E) PROJECT GUTENBERG EBOOK.*?\*\*\*", text, re.IGNORECASE)
    end_match = re.search(r"\*\*\*\s*END OF TH(IS|E) PROJECT GUTENBERG EBOOK.*?\*\*\*", text, re.IGNORECASE)

    if start_match and end_match:
        text = text[start_match.end():end_match.start()]
    elif start_match:
        text = text[start_match.end():]

    # 2. Expurgate Transcriber Notes, Annotations, and Bracketed Metadata
    text = re.sub(r"\[Transcriber'?s?\s*Note:?.*?\]", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"\[Illustration:?.*?\]", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"\[Footnote:?.*?\]", "", text, flags=re.IGNORECASE | re.DOTALL)

    # 3. Strip Chapter Headings, Roman Numerals, and Section Headers
    text = re.sub(r"^\s*(CHAPTER|BOOK|VOLUME|PART|SECTION|CANTO|ACT|SCENE)\s+([0-9IVXLCDM]+|\w+)\b.*$", "", text, flags=re.IGNORECASE | re.MULTILINE)
    text = re.sub(r"^\s*[IVXLCDM]{1,10}\.\s*$", "", text, flags=re.MULTILINE)

    # 4. Remove Publisher Colophons, Printers, and Gutenberg Archive Metadata
    text = re.sub(r"Printed by\s+.*$", "", text, flags=re.IGNORECASE | re.MULTILINE)
    text = re.sub(r"London\s*:\s*Published by\s+.*$", "", text, flags=re.IGNORECASE | re.MULTILINE)
    text = re.sub(r"End of (the )?Project Gutenberg EBook.*$", "", text, flags=re.IGNORECASE | re.MULTILINE)

    # 5. Normalize Typography and Excessive Whitespace
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()

cleaned_texts = []
print("Downloading and sanitizing corpus from cached endpoints...")

for url in sources:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            raw_content = response.read().decode('utf-8-sig', errors='ignore')
            sanitized = expurgate_gutenberg(raw_content)
            if len(sanitized) > 1000:
                cleaned_texts.append(sanitized)
    except Exception as e:
        print(f"Skipping {url} due to error: {e}")

print(f"Successfully processed {len(cleaned_texts)} works.")

# Save raw merged text for Tokenizer training
with open("sanitized_satire_corpus.txt", "w", encoding="utf-8") as f:
    f.write("\n\n<|endoftext|>\n\n".join(cleaned_texts))

"""
Cell 2: Train custom tokenizer
"""
import os
from tokenizers import ByteLevelBPETokenizer
from transformers import PreTrainedTokenizerFast

# Train a 12,288 vocab tokenizer (Saves embedding parameters)
special_tokens = ["<|endoftext|>", "<|pad|>"]

bpe_tokenizer = ByteLevelBPETokenizer()
bpe_tokenizer.train(
    files=["sanitized_satire_corpus.txt"],
    vocab_size=12288,
    min_frequency=2,
    special_tokens=special_tokens
)

os.makedirs("satire_tokenizer", exist_ok=True)
bpe_tokenizer.save_model("satire_tokenizer")

tokenizer = PreTrainedTokenizerFast(
    tokenizer_file="satire_tokenizer/vocab.json",
    vocab_file="satire_tokenizer/vocab.json",
    merges_file="satire_tokenizer/merges.txt",
    bos_token="<|endoftext|>",
    eos_token="<|endoftext|>",
    pad_token="<|pad|>"
)
"""
Cell 3: Initialize 30M Parameter Random GPT 2 Head
"""
import json
import torch
from transformers import GPT2Config, GPT2LMHeadModel

# 30.8M Parameter Configuration
config = GPT2Config(
    vocab_size=12288,
    n_positions=768,
    n_ctx=768,
    n_embd=384,
    n_layer=10,
    n_head=8,
    bos_token_id=tokenizer.convert_tokens_to_ids("<|endoftext|>"),
    eos_token_id=tokenizer.convert_tokens_to_ids("<|endoftext|>"),
    pad_token_id=tokenizer.convert_tokens_to_ids("<|pad|>"),
    tie_word_embeddings=True
)

# Initialize from SCRATCH with random Gaussian weights
model = GPT2LMHeadModel(config)

total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Verified Randomly Initialized Parameters: {total_params:,}")
# Output: ~30,812,160 parameters

"""
Cell 4: Chunking
"""
import torch
from transformers import DataCollatorForLanguageModeling, Trainer, TrainingArguments, TrainerCallback

# Pack text into overlapping 768-token sequences
def chunk_text(texts, block_size=768, stride=384):
    all_input_ids = []
    for text in texts:
        tokens = tokenizer.encode(text)
        for i in range(0, len(tokens), stride):
            chunk = tokens[i:i + block_size]
            if len(chunk) == block_size:
                all_input_ids.append(chunk)
    return Dataset.from_dict({"input_ids": all_input_ids})

dataset = chunk_text(cleaned_texts, block_size=768, stride=384)

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

class SatireSampleCallback(TrainerCallback):
    def __init__(self, tokenizer, sample_prompt="It is a truth universally acknowledged, that a young politician", steps=100):
        self.tokenizer = tokenizer
        self.sample_prompt = sample_prompt
        self.steps = steps
        self._last_logged_step = -1

    def on_step_end(self, args, state, control, model=None, **kwargs):
        if state.global_step > 0 and state.global_step % self.steps == 0 and state.global_step != self._last_logged_step:
            self._last_logged_step = state.global_step

            print(f"\n" + "=" * 18 + f" SAMPLE GENERATION (STEP {state.global_step}) " + "=" * 18)
            model.eval()
            inputs = self.tokenizer(self.sample_prompt, return_tensors="pt").to(model.device)
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=80,
                    temperature=0.75,
                    top_p=0.88,
                    top_k=40,
                    repetition_penalty=1.2,
                    do_sample=True,
                    pad_token_id=self.tokenizer.pad_token_id
                )
            
            sample_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(sample_text)
            print("=" * 63 + "\n")
            model.train()

# Instantiate Callback
satire_callback = SatireSampleCallback(
    tokenizer=tokenizer,
    sample_prompt="It is a truth universally acknowledged, that a young politician",
    steps=100
)

# Trainer Configuration with 100-step Check-ins
training_args = TrainingArguments(
    output_dir="./satire_gpt2_30m",
    overwrite_output_dir=True,
    num_train_epochs=15,
    per_device_train_batch_size=8,
    gradient_accumulation_steps=4,
    learning_rate=5e-4,
    weight_decay=0.01,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    logging_steps=50,
    save_strategy="epoch",
    fp16=torch.cuda.is_available(),
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    train_dataset=dataset,
    callbacks=[satire_callback]
)

# Train the Model
trainer.train()

# Save locally after training finishes
model.save_pretrained("./satire_gpt2_30m_final")
tokenizer.save_pretrained("./satire_gpt2_30m_final")

"""
Testing/Prompting Cell
"""
def continue_prompt(prompt_text, max_new_tokens=150):
    inputs = tokenizer(prompt_text, return_tensors="pt").to(model.device)
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=0.75,
        top_p=0.88,
        top_k=40,
        repetition_penalty=1.2,
        no_repeat_ngram_size=3,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id
    )
    
    continuation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("=== PROMPT CONTINUATION ===")
    print(continuation)

# Example Continuation Prompt
test_prompt = "It is a truth universally acknowledged, that a young politician in possession of a good fortune,"
continue_prompt(test_prompt)
