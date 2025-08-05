# Editor de Imagens - Prototipagem

Este é um protótipo funcional de uma aplicação de edição de imagens com Streamlit, desenvolvido como parte de uma atividade de Processamento de Imagens. A aplicação simula o funcionamento de uma rede social, permitindo que o usuário envie uma imagem, aplique filtros e edições, visualize o resultado e baixe a imagem final.

## Funcionalidades

O usuário pode:

- Enviar uma imagem via upload ou capturar com a webcam.
- Aplicar transformações geométricas:
  - Rotação (graus)
  - Escala (zoom)
  - Cisalhamento horizontal e vertical
- Fazer ajustes de intensidade:
  - Brilho
  - Contraste
  - Transformações logarítmica ou gama
- Aplicar efeito negativo.
- Visualizar lado a lado a imagem original e a editada.
- Escolher o nome do arquivo e baixar a imagem final.
- Resetar individualmente cada grupo de ajustes (geométricos, intensidade e filtro).

## Como rodar localmente

### 1. Clone o repositório ou baixe os arquivos

```bash
git clone https://github.com/seu-usuario/editor-imagens.git
cd editor-imagens
```

### 2. Crie um ambiente virtual (opcional)

```python
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o app com Streamlit

```bash
streamlit run app.py 
```

A aplicação abrirá automaticamente no navegador (geralmente em http://localhost:8501).

## Estrutura do Projeto

```
editor-imagens/
├── app.py
├── requirements.txt
├── README.md
├── output/                # Pasta opcional para salvar exemplos
└── utils/
    ├── display.py
    ├── filters.py
    ├── geometry.py
    ├── intensity.py
    └── load_image.py
```

# Observações
A resolução das imagens capturadas pela webcam pode variar conforme o dispositivo.

O botão de download gera arquivos no formato PNG.

O nome do arquivo pode ser personalizado pelo usuário no campo abaixo da visualização.


