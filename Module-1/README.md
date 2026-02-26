# Module 1 – Prompt-Based Style Explainer

This project builds a prompt-based explanation generator using the Groq API.

It generates creative, style-controlled responses based on selected character modes.

---

## 🚀 Features

- Dynamic style-based explanation generation
- Role-conditioned output (Shakespeare / Pirate / Bandit)
- System and user prompt separation
- Temperature-controlled creativity
- Clean modular structure

---

## 📁 Project Structure

style_explainer/
│
├── app.py
├── prompts.py
├── requirements.txt
├── .env
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone or Create Project Folder

Create a folder and place all project files inside.

---

### 2️⃣ Install Dependencies

pip install -r requirements.txt

---

### 3️⃣ Add Environment Variables

Create a `.env` file and add:

GROQ_API_KEY=your_actual_key_here

---

### 4️⃣ Run the Program

python app.py