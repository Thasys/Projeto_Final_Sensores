# Sistema de Monitoramento Ambiental - IFS

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

Sistema para monitoramento de condições ambientais (temperatura e umidade) em salas e laboratórios do Instituto Federal de Sergipe.

![Dashboard Preview](screenshots/dashboard.png) <!-- Adicione uma screenshot real -->

## 📋 Tabela de Conteúdos
- [Funcionalidades](#✨-funcionalidades)
- [Pré-requisitos](#📦-pré-requisitos)
- [Instalação](#🚀-instalação)
- [Configuração](#⚙️-configuração)
- [Uso](#💻-uso)
- [Estrutura do Projeto](#📂-estrutura-do-projeto)
- [Contribuição](#🤝-contribuição)
- [Licença](#📄-licença)

## ✨ Funcionalidades
- Monitoramento em tempo real de temperatura e umidade
- Dashboard interativo com gráficos históricos
- CRUD completo para:
  - Salas e laboratórios
  - Sensores físicos e lógicos
  - Parâmetros de operação
- Geração de relatórios:
  - Dados agregados por período
  - Sensores com valores críticos
  - Relatórios personalizados com filtros

## 📦 Pré-requisitos
- Python 3.11+
- PostgreSQL 15+ ou SQLite3
- Git
- pip

## 🚀 Instalação

### 1. Clonar repositório
```bash
git clone https://github.com/seu-usuario/monitoramento-ifs.git
cd monitoramento-ifs