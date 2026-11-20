
from transformers import AutoTokenizer

TOKENIZERS = {
    "BPE - GPT-2": "gpt2",
    "WordPiece - Multilingual BERT": "bert-base-multilingual-cased",
    "SentencePiece - XLM-R": "xlm-roberta-base"
}

TEXTS = {
    "English": "Artificial intelligence is changing the world.",
    "Telugu": "కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.",
    "Hindi": "कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।"
}


def load_tokenizers():
    loaded = {}

    for name, model in TOKENIZERS.items():
        print(f"\nLoading {name}...")
        loaded[name] = AutoTokenizer.from_pretrained(model)

    return loaded


def compare_text(text, language, tokenizers):

    print("\n" + "=" * 75)
    print("LANGUAGE / PROMPT:", language)
    print("INPUT TEXT:", text)
    print("=" * 75)

    for name, tokenizer in tokenizers.items():

        encoded = tokenizer(
            text,
            add_special_tokens=True,
            truncation=False
        )

        token_ids = encoded["input_ids"]
        tokens = tokenizer.convert_ids_to_tokens(token_ids)

        print(f"\n{name}")
        print("Tokens     :", tokens)
        print("Token IDs  :", token_ids)
        print("Token count:", len(token_ids))


def main():

    tokenizers = load_tokenizers()

    # Given practical sentences
    print("\n========== GIVEN TEXTS ==========")

    for language, text in TEXTS.items():
        compare_text(text, language, tokenizers)

    # User's own prompts
    print("\n========== YOUR OWN PROMPTS ==========")

    while True:

        prompt = input("\nEnter your own prompt (or type exit): ")

        if prompt.lower() == "exit":
            break

        if not prompt.strip():
            print("Please enter some text.")
            continue

        compare_text(prompt, "Custom Prompt", tokenizers)


if __name__ == "__main__":
    main()
