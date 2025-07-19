# Projeto de Classificação de Campanha de Marketing

Este projeto tem como objetivo aplicar técnicas de **Machine Learning supervisionado** para prever o sucesso de campanhas de marketing, utilizando um conjunto de dados **fictício**. Foi conduzido todo o fluxo de um projeto de ciência de dados, desde a exploração dos dados até a explicação dos modelos com SHAP.

---

## Objetivo

Construir um modelo preditivo capaz de classificar corretamente se uma campanha será **bem-sucedida (1)** ou **mal-sucedida (0)**, com base em dados comportamentais e financeiros dos clientes.

---

## Estrutura do Projeto

```bash
marketing-project/
│
├── data/ # Dados brutos e limpos
│ └── df_temp.csv
│
├── notebooks/ # Notebooks do projeto
│ ├── 01_EDA.ipynb
│ ├── 02_Modelagem_XGBoost.ipynb
│ ├── 03_Validacao_Cruzada.ipynb
│ └── 04_SHAP_Explicabilidade.ipynb
│
├── images/ # Gráficos salvos
│ ├── confusion_matrix.png
│ ├── roc_curve.png
│ └── shap_summary.png
│
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo
```

---

## 🔍 Etapas Realizadas

### 1. Pré-processamento
- Exclusão e imputação de dados faltantes
- Codificação de variáveis categóricas
- Extração de partes de datas
- Normalização de colunas numéricas, se necessário

### 2. Análise Exploratória (EDA)
- Avaliação da distribuição das variáveis
- Análise bivariada entre `sucesso` e variáveis preditoras
- Verificação de outliers e colinearidade

### 3. Modelagem com XGBoost
- Separação treino/teste com `train_test_split`
- Avaliação com `classification_report` e matriz de confusão
- **Validação cruzada estratificada (k=5)** com `StratifiedKFold`
- Cálculo de métricas globais como F1 Macro

### 4. Interpretação do Modelo
- Análise de `feature_importances_` do XGBoost
- Interpretação com `SHAP` (importância global e impacto individual)

---

## 📈 Resultados

### 📌 Validação Cruzada (F1 Macro)

```text
F1 macro por fold: [0.5417, 0.5139, 0.6827, 0.5249, 0.4327]
Média do F1 macro: 0.5392
📉 Curva ROC

AUC = 0.54

Modelo tem desempenho próximo ao aleatório, sinalizando que ajustes são necessários

🧾 Matriz de Confusão (exemplo)

💡 Principais Insights
O modelo tem dificuldade em generalizar, possivelmente por:

Baixo número de amostras (150 linhas)

Alta dimensionalidade (283 colunas)

Possível desbalanceamento das classes

A classe 1 (sucesso) é melhor reconhecida que a classe 0

AUC e F1 abaixo de 0.60 sugerem desempenho insuficiente para uso real

🔧 Tecnologias Utilizadas
Python 3.10+

pandas, numpy, matplotlib, seaborn

scikit-learn

XGBoost

SHAP

Jupyter Notebook

⚠️ Observações
Os dados utilizados são fictícios e não representam clientes reais.

Este projeto tem fins educacionais e demonstrativos.

🚀 Próximos Passos
🔍 Aplicar redução de dimensionalidade (SelectKBest, PCA)

⚖️ Balanceamento de classes com SMOTE

🔄 Testar outros algoritmos (RandomForest, LightGBM, LogisticRegression)

📊 Realizar tuning com GridSearchCV

📈 Avaliar performance em novos conjuntos de dados simulados
