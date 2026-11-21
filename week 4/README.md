WEEK 4 – Tokenizer Lab: BPE, WordPiece and SentencePiece
Aim
To compare different tokenization methods such as BPE, WordPiece, and SentencePiece using English, Telugu, and Hindi sentences, and observe their tokens, token IDs, and token counts.
Technologies Used
- Python
- Hugging Face Transformers
- BPE (GPT-2)
- WordPiece (Multilingual BERT)
- SentencePiece (XLM-R)
- Pandas
Tools Used
- Google Colab
- Python
- Hugging Face Tokenizers
Folder Structure
WEEK4/
├── WEEK4_Tokenizer_Lab_BPE_WordPiece_SentencePiece.ipynb
└── README.md
Installation Steps
1. Open the WEEK4 notebook in Google Colab.
2. Install the required libraries by running the first code cell:
pip install transformers sentencepiece
3. Import the tokenizer library:
from transformers import AutoTokenizer
4. Run the notebook cells in order.
Note: The notebook downloads the selected pretrained tokenizer files when they are first loaded, so an internet connection is required.
Execution Steps
Run all notebook cells from top to bottom.
1. Install the Transformers and SentencePiece libraries.
2. Import AutoTokenizer.
3. Define the three tokenizers:
   - BPE – GPT-2 (gpt2)
   - WordPiece – Multilingual BERT (bert-base-multilingual-cased)
   - SentencePiece – XLM-R (xlm-roberta-base)
4. Provide sample sentences in English, Telugu, and Hindi.
5. Load all three pretrained tokenizers.
6. Encode each sentence using each tokenizer.
7. Display the generated tokens, token IDs, and token counts.
8. Create a Pandas comparison table showing token counts for each language and tokenizer.
Expected Output
The notebook displays the tokens, token IDs, and token count for every language and tokenizer.

Example input:
English: Artificial intelligence is changing the world.
Telugu: కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.
Hindi: कृ त्रिम बुद्धिमत्ता दुनिया को बदल रही है।
A comparison table is displayed with these columns:
Language
BPE - GPT-2
WordPiece - Multilingual BERT
SentencePiece - XLM-R
The exact token counts depend on the tokenizer vocabulary and the input text.
Result
Successfully compared BPE, WordPiece, and SentencePiece tokenization methods using English, Telugu, and Hindi text, and observed their tokens, token IDs, and token counts.
