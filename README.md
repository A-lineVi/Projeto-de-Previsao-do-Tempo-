# ✧⁠*∘⁠˚⁠✿ Previsão do Tempo Regional ✿˳⁠°

Este é um projeto em Python que consome a API **Open-Meteo** para fornecer dados climáticos em tempo real das diferentes zonas de São Paulo.

## 🚀 Funcionalidades
- Busca temperatura, velocidade do vento e pressão barométrica (MSL).
- **Análise Barométrica:** O sistema interpreta a pressão atmosférica para indicar tendências climáticas:
    - **Pressão Alta (> 1013 mbar):** Indica tempo estável e céu limpo.
    - **Pressão Baixa (< 1010 mbar):** Indica alerta de instabilidade e possíveis tempestades.
- Filtro por região (Zona Sul, Norte, Leste e Oeste de São Paulo).

## 🛠️ Tecnologias
- [Python 3](https://www.python.org/)
- [Requests Library](https://requests.readthedocs.io/)
- [Open-Meteo API](https://open-meteo.com/)

## 📖 O que aprendi neste projeto
Neste projeto, explorei como a **pressão barométrica** é um indicador crucial para a meteorologia. Entendi que a queda brusca de pressão indica que o ar está subindo e condensando, o que facilita a formação de chuva. Também apliquei conceitos de **tratamento de erros (try/except)** e manipulação de dicionários em Python.

---
*Projeto desenvolvido para fins de estudo em técnicas de programação e integração de APIs.*
