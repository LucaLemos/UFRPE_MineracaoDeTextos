Trabalho 3va comapração de desempenho do spacy portugues

pt_core_news_sm
pt_core_news_md
pt_core_news_lg

## Evaluation Metrics

Nós avaliamos os modelos utilizando as métricas de Precisão, Recall e F1-score. Os resultados estão resumidos na tabela abaixo.

| Model     | Precision | Recall  | F1-score |
|-----------|-----------|---------|----------|
| `model_sm` | 0.7340    | 0.7580  | 0.7432   |
| `model_md` | 0.7485    | 0.7600  | 0.7521   |
| `model_lg` | 0.8045    | 0.7869  | 0.7939   |

## Model Performance

![Model Performance](compareModel_files/compareModel_8_0.png)

### Analysis

- **`model_sm`**: 
  - O model_sm apresenta uma precisão e um recall bastante equilibrados, com um F1-score relativamente bom. No entanto, comparado aos modelos maiores, ele tem um desempenho um pouco inferior.

- **`model_md`**: 
  - O model_md mostra uma leve melhoria em precisão e recall em relação ao model_sm. O F1-score também é um pouco melhor, o que indica uma performance um pouco mais robusta e equilibrada.

- **`model_lg`**: 
  - O model_lg se destaca com as melhores métricas entre os três modelos. A precisão e o recall são significativamente maiores, e o F1-score é o melhor de todos. Isso sugere que o model_lg é o mais eficaz para a tarefa de reconhecimento de entidades, possivelmente devido ao seu maior tamanho e complexidade.

### Conclusion

O modelo model_lg demonstra o melhor desempenho geral, com precisão, recall e F1-score mais altos, indicando que ele é o mais capaz de identificar e classificar as entidades no seu conjunto de dados. Os modelos menores (model_sm e model_md) ainda são eficazes, mas a performance deles é um pouco inferior comparada ao modelo maior. Se o custo computacional não for um problema, o model_lg é a melhor escolha para a tarefa.
