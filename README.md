Trabalho 3va comapração de desempenho do spacy portugues

pt_core_news_sm
pt_core_news_md
pt_core_news_lg

# Model Comparison

This document provides a comparison of three SpaCy models trained for named entity recognition (NER) on our dataset. The models evaluated are:

- `model_sm` (Small)
- `model_md` (Medium)
- `model_lg` (Large)

## Evaluation Metrics

We evaluated the models using Precision, Recall, and F1-score metrics. The results are summarized in the table below.

| Model     | Precision | Recall  | F1-score |
|-----------|-----------|---------|----------|
| `model_sm` | 0.7340    | 0.7580  | 0.7432   |
| `model_md` | 0.7485    | 0.7600  | 0.7521   |
| `model_lg` | 0.8045    | 0.7869  | 0.7939   |

## Model Performance

![Model Performance](path/to/your/plot.png)

### Analysis

- **`model_sm`**: 
  - The smallest model has balanced precision and recall but slightly lower metrics compared to the other models. It may be suitable if computational resources are limited.

- **`model_md`**: 
  - Shows improved precision and recall over `model_sm`, indicating a more effective model for entity recognition. The improvement in F1-score suggests it offers a better balance between precision and recall.

- **`model_lg`**: 
  - The largest model delivers the highest precision, recall, and F1-score, making it the most effective for entity recognition. Its superior performance likely results from its increased complexity and capacity to understand and process data.

### Conclusion

The `model_lg` demonstrates the best overall performance, making it the preferable choice if computational resources are available. The `model_md` offers a good balance of performance and efficiency, while `model_sm` is best suited for environments with limited resources.

### Recommendations

- **If computational resources are a constraint**: Consider using `model_md` for a good balance of performance and efficiency.
- **For the best performance**: `model_lg` is the best choice, provided that you can handle the increased computational cost.
- **Further tuning**: You might want to explore fine-tuning hyperparameters or data augmentation techniques to potentially boost the performance of the models even further.

## Files

- [Comparison Script](path/to/compareModel.md)
- [Dataset](path/to/dataset.jsonl)
- [Plot Image](path/to/your/plot.png)