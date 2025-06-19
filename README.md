# Resume NER Annotation Tool

A Streamlit-based tool for annotating Named Entities in resume text files. Supports manual annotation and auto-labeling using transformer models.

## Features

- Load `.txt` resume files from a folder
- Annotate entities interactively in the browser
- Auto-label using a transformer-based NER model
- Export labeled data as JSON

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/labelling_project.git
cd labelling_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

### 4. Open the app in your browser

- After running the above command, Streamlit will display a local URL (e.g., `http://localhost:8501`).
- Open this URL in your web browser.

## How to Use

### 1. Load Text Files

- Enter the full path to the folder containing your `.txt` resume files in the input box at the top of the app.
- Click **"Load Files"** to load all `.txt` files from that folder.

### 2. Annotate Entities

- Use the **"Select Entity Type"** dropdown to choose the type of entity you want to label (e.g., NAME, EMAILID, PHONE, etc.).
- Highlight text in the resume content area to annotate it with the selected entity type.
- Use the **"Previous"** and **"Next"** buttons to navigate between files.

### 3. Auto-label Remaining Files

- Click **"Auto-label Remaining Files"** to automatically annotate files that have not been manually labeled, using a transformer-based NER model.

### 4. Export Labeled Data

- Click **"Export Labelled Data"** to prepare your annotations for download.
- Then click the **"📥 Download"** button to download the labeled data as a JSON file.

#### Export Format

The exported file is a JSON array, where each item is a tuple:

```json
[
  [
    "resume text here",
    {
      "entities": [
        [start_char, end_char, "LABEL"],
        ...
      ]
    }
  ],
  ...
]
```

- `start_char` and `end_char` are character offsets in the text.
- `"LABEL"` is the entity type (e.g., NAME, EMAILID, etc.).

## Folder Structure

- `app.py` - Main Streamlit app
- `auto_labeler.py` - Auto-labeling logic
- `styles/` - Custom CSS for the app

## License

MIT License
