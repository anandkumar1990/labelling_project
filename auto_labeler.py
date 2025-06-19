import spacy
from spacy.tokens import DocBin
from spacy.training import Example
from typing import List, Tuple, Dict
import random
from transformers import pipeline
import torch
import re

def prepare_training_data(annotations: List[Tuple[str, Dict]]):
    """Convert our annotation format to spaCy training format"""
    nlp = spacy.blank("en")
    db = DocBin()
    
    for text, annot in annotations:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    
    return db

def train_ner_model(training_data: List[Tuple[str, Dict]], output_dir: str = "model"):
    """Train a spaCy NER model on the annotated data"""
    nlp = spacy.blank("en")
    
    # Add NER pipeline
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    
    # Add labels
    for _, annotations in training_data:
        for _, _, label in annotations["entities"]:
            ner.add_label(label)
    
    # Prepare training data
    train_examples = []
    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        train_examples.append(example)
    
    # Train the model
    optimizer = nlp.begin_training()
    for _ in range(30):  # 30 iterations
        random.shuffle(train_examples)
        losses = {}
        for example in train_examples:
            nlp.update([example], sgd=optimizer, losses=losses)
    
    # Save the model
    nlp.to_disk(output_dir)
    return nlp

class AutoLabeler:
    def __init__(self):
        self.ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
        self.label_map = {
            'PER': 'NAME',
            'ORG': 'COMPANIES_WORKED_AT',
            'MISC': 'SKILLS'
        }

    def regex_entities(self, text):
        entities = []
        # Email
        for match in re.finditer(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text):
            entities.append({'start': match.start(), 'end': match.end(), 'label': 'EMAILID'})
        # Phone (simple pattern)
        for match in re.finditer(r"\b\d{10}\b", text):
            entities.append({'start': match.start(), 'end': match.end(), 'label': 'PHONE'})
        return entities

    def predict(self, text):
        """Predict entities in text"""
        results = self.ner(text)
        entities = []
        
        for result in results:
            ent_type = result['entity'].split('-')[-1]
            if ent_type in self.label_map:
                entities.append({
                    'start': result['start'],
                    'end': result['end'],
                    'label': self.label_map[ent_type]
                })
        # Add regex-based entities
        entities.extend(self.regex_entities(text))
        return entities

def auto_label_text(text):
    """Use transformer model to auto-label text"""
    labeler = AutoLabeler()
    return labeler.predict(text)

def train_model(training_data, output_dir="trained_model"):
    # Placeholder for compatibility; not used with transformers pipeline
    return True
