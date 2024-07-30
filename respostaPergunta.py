from transformers import pipeline

def answer_question(question, context):
    qa_pipeline = pipeline("question-answering")
    result = qa_pipeline(question=question, context=context)
    return result['answer']

context = "Alice was a young girl who lived in a small village. She loved to explore the woods and discover hidden secrets. One day, she found an old, mysterious book in the attic."
question = "What did Alice find in the attic?"
answer = answer_question(question, context)
print(answer)