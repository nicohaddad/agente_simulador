# 🧑‍⚖️ Agente Simulador de Juicio Oral con IA 🇲🇽

Este repositorio contiene un simulador de juicio oral penal mexicano, impulsado por agentes GPT.

## 📂 Estructura del proyecto

- `agentscourt_simulador_CORREGIDO_v2.ipynb`: Notebook principal
- `agent.py`: Lógica del agente GPT
- `role_config.json`: Configuración de personajes (Juez, MP, Defensa)
- `data/case001.json`: Caso de ejemplo
- `environment_con_jupyter_y_voz.yml`: Entorno reproducible

## ▶️ Cómo ejecutar

```bash
conda env create -f environment_con_jupyter_y_voz.yml
conda activate agentscourt
jupyter notebook
