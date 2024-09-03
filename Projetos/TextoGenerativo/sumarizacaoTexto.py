from transformers import pipeline

def summarize(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

text = "Modelos de Transformadores (Transformers Models) são um tipo de arquitetura de rede neural desenvolvida para processar dados sequenciais, como texto e linguagem natural. Eles são particularmente eficazes em tarefas de processamento de linguagem natural (PLN) devido à sua capacidade de lidar com dependências a longo prazo nos dados."
summary = summarize(text)
print(summary)