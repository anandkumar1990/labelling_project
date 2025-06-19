# Resume NER Annotation Tool

A Streamlit-based tool for annotating Named Entities in resume text files. Supports manual annotation and auto-labeling using transformer models.

## Features

- Load `.txt` resume files from a folder
- Annotate entities interactively
- Auto-label using a transformer-based NER model
- Export labeled data as JSON

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Folder Structure

- `app.py` - Main Streamlit app
- `auto_labeler.py` - Auto-labeling logic
- `styles/` - Custom CSS for the app

## License

MIT License
