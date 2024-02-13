import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def compute_similarity(sentence, text):
    doc_sentence = nlp(sentence)
    doc_text = nlp(text)
    return doc_sentence.similarity(doc_text)

def compare_sentence_to_paragraphs(sentence, paragraph1, paragraph2):
    similarity_to_p1 = compute_similarity(sentence, paragraph1)
    similarity_to_p2 = compute_similarity(sentence, paragraph2)
    print(similarity_to_p1, similarity_to_p2)
    if similarity_to_p1 > similarity_to_p2:
        return "Paragraph 1"
    elif similarity_to_p1 < similarity_to_p2:
        return "Paragraph 2"
    else:
        return "Both paragraphs are equally similar"

# Example usage:
sentence = "i like technology"
paragraph1 = "This is the first paragraph. It talks about technology and science."
paragraph2 = "This is the second paragraph. It discusses art and literature."

result = compare_sentence_to_paragraphs(sentence, paragraph1, paragraph2)
print("The sentence is more similar to:", result)