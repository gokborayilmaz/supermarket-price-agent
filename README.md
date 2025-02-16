# 🛒 Supermarket Price  Agent - Day 20/21

This agent is part of the **Everyday New AI Agent** series - **Day 20/21** 🚀

## 📌 Overview

The **Market Price Tracker Agent** helps users compare product prices across multiple online retailers using **BrowserUse and Upsonic AI**.

### 🔹 Features:

- 🛍️ **Finds your desired product** across different markets like Walmart, Target, and Amazon.
- 💰 **Compares prices** and shows the best deals.

---

## 🛠️ Installation & Setup

### **Prerequisites**

- Python 3.9 or higher
- Git
- Virtual environment (recommended)
- **BrowserUse** and Playwright for web scraping

### **Installation**

1️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

2️⃣ Set up BrowserUse & Playwright:

```bash
playwright install
```

3️⃣ Create a `.env` file in the root directory and configure it as follows:

```env
AZURE_OPENAI_API_KEY= "YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_ENDPOINT= "YOUR_AZURE_OPENAI_ENDPOINT"
AZURE_OPENAI_MODEL_NAME= "YOUR_AZURE_OPENAI_MODEL_NAME"
AZURE_OPENAI_DEPLOYMENT= "YOUR_AZURE_OPENAI_DEPLOYMENT"
AZURE_OPENAI_API_VERSION= "YOUR_AZURE_OPENAI_API_VERSION"
```

---

## 🚀 Running the Agent

Start the FastAPI server:

```bash
python upsonicai.py
```

---

🚀 **UpsonicAI - Making AI Agents Simple & Scalable!**


