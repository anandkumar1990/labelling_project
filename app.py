import streamlit as st
import os
import json
from st_ner_annotate import st_ner_annotate
from styles.custom import get_custom_css
from auto_labeler import auto_label_text, train_model

# Set page config and apply styling
st.set_page_config(layout="wide", page_title="Resume NER Annotation Tool")
st.markdown(get_custom_css(), unsafe_allow_html=True)

def load_text_files(folder_path):
    """Load text files from given folder path"""
    files_dict = {}
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith('.txt'):
                try:
                    with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                        files_dict[file] = f.read()
                except Exception as e:
                    st.error(f"Error reading file {file}: {e}")
    return files_dict

def reset_session_state(files_dict):
    """Reset the session state when loading new files"""
    st.session_state.current_file_idx = 0
    st.session_state.annotations = {filename: [] for filename in files_dict.keys()}

def format_for_export(annotations_dict, files):
    # Modified to accept files dictionary as parameter
    formatted_data = []
    for filename, annotations in annotations_dict.items():
        if filename in files:  # Only process if file exists
            text = files[filename]
            entities_list = []
            for ann in annotations:
                entities_list.append((
                    ann['start'],
                    ann['end'],
                    ann['label']
                ))
            formatted_data.append((
                text,
                {"entities": entities_list}
            ))
    return formatted_data

st.title("Resume NER Annotation Tool")

# Use session state to track current folder
if 'current_folder' not in st.session_state:
    st.session_state.current_folder = ""

# Load files from current folder (move this up before top row)
files = load_text_files(st.session_state.current_folder)

# Top row: folder path and buttons
top_col1, top_col2 = st.columns([3, 1])
with top_col1:
    folder_path = st.text_input(
        "Enter folder path containing .txt files:",
        placeholder="Enter the full path to your .txt files folder"
    )
with top_col2:
    load, export = st.columns(2)
    with load:
        if st.button("Load Files", use_container_width=True):
            if not os.path.exists(folder_path):
                st.error("Directory does not exist!")
            else:
                if 'annotations' in st.session_state:
                    del st.session_state.annotations
                if 'current_file_idx' in st.session_state:
                    del st.session_state.current_file_idx
                if 'current_folder' in st.session_state:
                    del st.session_state.current_folder
                st.session_state.current_folder = folder_path
    with export:
        if st.button("Export Labelled Data", use_container_width=True):
            formatted_data = format_for_export(st.session_state.annotations, files)
            st.download_button(
                label="📥 Download",
                data=json.dumps(formatted_data, indent=2),
                file_name="annotations.json",
                mime="application/json",
                use_container_width=True
            )

# Use session state to track current folder
if 'current_folder' not in st.session_state:
    st.session_state.current_folder = folder_path

# Load files from current folder
files = load_text_files(st.session_state.current_folder)

if not files:
    st.error("No .txt files found in the specified folder")
else:
    # Initialize session state for annotations
    if 'current_file_idx' not in st.session_state or 'annotations' not in st.session_state:
        reset_session_state(files)

    # Navigation row
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    with nav_col1:
        if st.button("Previous", use_container_width=True):
            if st.session_state.current_file_idx > 0:
                st.session_state.current_file_idx -= 1
    with nav_col2:
        current_file = list(files.keys())[st.session_state.current_file_idx]
        st.markdown(
            f"<div style='text-align:center;font-size:2rem;font-weight:600;'>Current file : {current_file}</div>",
            unsafe_allow_html=True
        )
    with nav_col3:
        if st.button("Next", use_container_width=True):
            if st.session_state.current_file_idx < len(files) - 1:
                st.session_state.current_file_idx += 1

    # Entity select row
    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
    entity_col1, entity_col2 = st.columns([1, 3])
    with entity_col1:
        current_entity_type = st.selectbox(
            "Select Entity Type",
            ["NAME", "EMAILID", "PHONE", "COMPANIES_WORKED_AT", "SKILLS", "DESIGNATION", "EDUCATION", "EXPERIENCE"]
        )

    # Main area: resume content (left), annotations/statistics (right)
    main_col1, main_col2 = st.columns([2.5, 1])
    with main_col1:
        entities = st_ner_annotate(
            current_entity_type,
            files[current_file],
            st.session_state.annotations[current_file],
            key=f"annotator_{current_file}"
        )
        st.session_state.annotations[current_file] = entities

    with main_col2:
        st.subheader("Current Annotations")
        st.json(entities)
        st.subheader("Statistics")
        entity_counts = {}
        for e in entities:
            label = e['label']
            entity_counts[label] = entity_counts.get(label, 0) + 1
        if entity_counts:
            for label, count in entity_counts.items():
                st.text(f"{label}: {count} annotations")
        else:
            st.text("No annotations yet")

    # Add Auto-labeling section
    st.markdown("<hr>", unsafe_allow_html=True)
    auto_label_col1, auto_label_col2 = st.columns([1, 1])
    
    with auto_label_col2:
        if st.button("Auto-label Remaining Files", use_container_width=True):
            with st.spinner("Auto-labeling remaining files..."):
                unlabeled_files = [f for f in files.keys() 
                                 if not st.session_state.annotations.get(f, [])]
                for file in unlabeled_files:
                    text = files[file]
                    entities = auto_label_text(text)
                    # Debug: print entities to Streamlit
                    st.write(f"Auto-labeled entities for {file}:", entities)
                    st.session_state.annotations[file] = entities
                st.success(f"Auto-labeled {len(unlabeled_files)} files!")