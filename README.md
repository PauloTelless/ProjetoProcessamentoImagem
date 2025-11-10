# 🧠 Spectrum — Ferramenta de Análise e Correção de Imagens

## 📘 Objetivo do Módulo

O módulo principal do **Spectrum** tem como objetivo **integrar e coordenar todas as etapas do processo de análise, transformação e correção de imagens digitais**, garantindo que o usuário possa realizar **ajustes visuais com controle, qualidade e rastreabilidade**.

---

## 🔧 Funcionalidades Principais

### 1.  Importação de Imagem
Permite que o usuário carregue uma imagem a partir de um diretório local.  
Essa etapa inicial valida o formato do arquivo e prepara os dados para o processamento posterior.

### 2.  Parametrização
Após a importação, o usuário define os parâmetros desejados para o processamento — como **brilho**, **contraste** ou **valor de gamma** — por meio de uma interface interativa.  
Essa função garante **flexibilidade** e **controle** sobre o resultado final.

### 3.  Processamento Linear
Aplica transformações lineares para ajuste de brilho e contraste, **modificando os níveis de intensidade de forma proporcional**.  
Utilizado para **correções básicas de exposição** e **realce global da imagem**.

### 4.  Processamento Não Linear
Executa operações como **correção gama** e **função logarítmica**, que modificam a relação entre níveis de intensidade de maneira não proporcional.  
Essas transformações permitem **realçar detalhes em regiões claras ou escuras**, aprimorando a percepção visual.

### 5.  Equalização de Histograma
Redistribui os níveis de intensidade da imagem, equilibrando a luminosidade e melhorando o contraste.  
Ideal para corrigir imagens com **iluminação irregular** ou **baixa definição tonal**.

### 6. Análise de Histograma
Gera e exibe o histograma da imagem **antes e depois** das transformações, permitindo avaliar a eficácia das operações aplicadas.  
Fornece **dados quantitativos** sobre a distribuição dos níveis de cinza e o impacto visual obtido.

### 7.  Comparação de Resultados
Apresenta lado a lado a **imagem original** e a **imagem processada**, permitindo uma avaliação visual direta.  
Também calcula **métricas comparativas**, como variação média de intensidade ou contraste percentual.

### 8.  Registro e Rastreamento
Cada operação é registrada com **data, parâmetros utilizados e resultados obtidos**, formando um histórico detalhado de execução.  
Esse registro garante **reprodutibilidade** e **transparência** nas análises.

---

## 🔁 Fluxo de Execução

O ciclo de execução do módulo segue uma sequência lógica e controlada:

1. **Importação da imagem** → o usuário seleciona a imagem desejada.
2. **Parametrização** → define brilho, contraste, gamma e demais variáveis.
3. **Processamento** → o sistema aplica as transformações lineares e/ou não lineares.
4. **Equalização e análise** → gera o histograma e aplica equalização se necessário.
5. **Comparação de resultados** → exibe as imagens original e processada.
6. **Registro e salvamento** → grava as operações e resultados obtidos.

🔄 Esse fluxo é **iterativo**: caso o usuário não esteja satisfeito com o resultado, pode retornar à etapa de parametrização e ajustar os valores até alcançar o efeito desejado.

---

## 👥 Equipe — Grupo 5
- Transformações Lineares e Não-Lineares
- Unidade II — Processamento Digital de Imagens
- Projeto desenvolvido com **Python**, **OpenCV**, **NumPy** e **Matplotlib**.

---

## 💾 Execução Rápida

```bash
# Clonar o repositório
git clone https://github.com/PauloTelless/ProjetoProcessamentoImagem.git
cd ProjetoProcessamentoImagem

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # (Windows)

# Instalar dependências
pip install -r requirements.txt

# Executar o módulo principal
python main.py
