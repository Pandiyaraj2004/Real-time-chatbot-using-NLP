# Real-time-chatbot-using-NLP
• Built a real-time chatbot capable of understanding and responding to user queries using Natural Language Processing (NLP) • Trained the chatbot on 20,000+ conversational records to enhance contextual understanding and response accuracy •

```markdown
# 🤖 Chatbot using Python + JSON + Intent Data

A simple yet powerful chatbot built with Python, NLTK, and a combination of structured intent-based data (`data.py`) and conversational dataset (`chatbot_data.json`). This bot supports over **16,000 conversation patterns** and responses and 3000 responses.

---

## 📌 Features

- ✅ NLP-based preprocessing (tokenization and stemming)
- ✅ Pattern matching using intents
- ✅ Extended response system using large-scale JSON conversations
- ✅ Easy fallback for unmatched user input
- ✅ Modular and extensible architecture

---

## 📁 Project Structure

```

chatbot\_project/
├── chatbot.py             # Main chatbot script
├── data.py                # Intent patterns and categorized responses
├── chatbot\_data.json      # Large conversational dataset (16,000+ entries)
└── README.md              # Project documentation

````

---

## 🔧 Requirements

- Python 3.7+
- NLTK

### 📦 Install dependencies:

```bash
pip install nltk
````

Also, download NLTK tokenizer data:

```python
import nltk
nltk.download('punkt')
```

---

## 🚀 How to Run

```bash
python chatbot.py
```

**Exit:** Type `exit` during the conversation to end the chat.

---

## 🧠 How It Works

1. **User Input** → Preprocessed with NLTK (tokenized and stemmed).
2. **Intent Matching** → Checked against patterns from `data.py`.
3. **Fallback to JSON** → If no intent matches, checks `chatbot_data.json`.
4. **Default Reply** → If no match is found in either dataset.

---

## 📚 Dataset Details

### `data.py`

* Contains categories like `greetings`, `questions`, `farewells`, etc.
* Each intent is mapped to a response category for structured replies.

### `chatbot_data.json`

* Flat list of 16,000+ conversation pairs.
* Format:

```json
[
  {
    "input": "hi, how are you doing?",
    "response": "i'm fine. how about yourself?"
  },
  ...
]
```

---

## 🛠️ Customization

* To **add new intents**, update `data.py`.
* To **extend chat knowledge**, append to `chatbot_data.json`.

---

## 👨‍💻 Author

* Name: Pandiyaraj (Chatbot Developer)
---

## 📄 License

This project is open-source and free to use under the MIT License.

```

---

Let me know if you want me to auto-generate this into a `.md` file or if you want a version with Tamil descriptions too.
```
