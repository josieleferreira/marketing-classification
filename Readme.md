# Projeto de Classificação de Campanha de Marketing

Este projeto tem como objetivo aplicar técnicas de **Machine Learning supervisionado** para prever o sucesso de campanhas de marketing, utilizando um conjunto de dados fictício. Abrange todas as etapas de um projeto de ciência de dados, desde a exploração e modelagem até a explicabilidade e a disponibilização em produção via **API Flask** com **Docker**.



## Objetivo

Construir um modelo preditivo capaz de classificar corretamente se uma campanha será **bem-sucedida (1)** ou **mal-sucedida (0)**, com base em dados comportamentais e financeiros dos clientes.


## Estrutura do Projeto

```bash
marketing-classification/
│
├── Data/
│   └── Projetos_para_Treinamento.csv        # Dados para modelagem
│
├── FLASK/
│   ├── app.py                               # API Flask com endpoint /predict
│   ├── Dockerfile                           # Dockerfile da aplicação
│   ├── docker-compose.yml                   # Orquestração da API com Docker
│   └── random_forest_model.pkl              # Modelo treinado serializado
│
├── Notebooks/
│   ├── Experiments.ipynb                    # Experimentos e validações
│   └── Modelo_Producao.ipynb                # Preparação para produção
│
├── mlruns/                                  # Rastreamento de experimentos com MLflow
├── mlartifacts/                             # Artefatos de modelos treinados
├── requirements.txt                         # Dependências do projeto
└── README.md
```


##  Etapas Realizadas

### 1. Pré-processamento
- Exclusão e imputação de dados faltantes
- Codificação de variáveis categóricas
- Extração de partes de datas
- Normalização de colunas numéricas, se necessário

### 2. Análise Exploratória (EDA)
- Avaliação da distribuição das variáveis
- Análise bivariada entre `sucesso` e variáveis preditoras
- Verificação de outliers e colinearidade

### 3.Treinamento de Modelos
- Modelos testados:
        XGBoost
        Random Forest
        Logistic Regression
- Validação cruzada (StratifiedKFold)
- Métricas: F1 Macro, ROC AUC, matriz de confusão

### 4. Interpretação do Modelo
- Análise de `feature_importances_` do XGBoost
- Interpretação com `SHAP` (importância global e impacto individual)
- Feature Importance


## Produção
- Serialização do melhor modelo (random_forest_model.pkl)
- Construção de API com Flask
- Deploy com Docker (docker-compose.yml)
- Rota /predict para realizar previsões via JSON


## Resultados

### Validação Cruzada (F1 Macro)
```bash
F1 macro por fold: [0.5417, 0.5139, 0.6827, 0.5249, 0.4327]
Média do F1 macro: 0.5392
```

### Curva ROC
```bash
AUC = 0.54
```
Modelo tem desempenho próximo ao aleatório, sinalizando que ajustes são necessários

### Principais Insights
O modelo tem dificuldade em generalizar, possivelmente por:
- Baixo número de amostras (150 linhas)
- Alta dimensionalidade (283 colunas)
- Possível desbalanceamento das classes
- A classe 1 (sucesso) é melhor reconhecida que a classe 0
- AUC e F1 abaixo de 0.60 sugerem desempenho insuficiente para uso real

### Tecnologias Utilizadas
- Python 3.10+
- pandas, numpy, matplotlib, seaborn
- scikit-learn
- XGBoost
- SHAP
- Jupyter Notebook
- MlFlow
- API Flask
- Docker

### Próximos Passos
- Aplicar redução de dimensionalidade (SelectKBest, PCA)
- Balanceamento de classes com SMOTE
- Testar outros algoritmos (RandomForest, LightGBM, LogisticRegression)
- Realizar tuning com GridSearchCV
- Avaliar performance em novos conjuntos de dados simulados
