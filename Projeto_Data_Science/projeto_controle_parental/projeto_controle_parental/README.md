# Controle parental: proteção infantojuvenil no mundo digital
### Análise de dados com CRISP-DM (SaferNet e TIC Kids Online Brasil 2025)


**Integrantes:** Graziela Marcela Alvarenga Silva Viana · Gabriela Marcela Alvarenga Silva Viana

## Perguntas de análise

| Pergunta | Responsável | Técnica | Resposta |
|---|---|---|---|
| **P1.** A série de denúncias de imagens de abuso e exploração sexual infantil (SaferNet, 2006–2025) pode ser projetada com uma tendência simples? | Graziela | Regressão linear e validação com origem móvel | **Não.** Os três previsores empatam com o modelo ingênuo (MAE de 8,4 a 8,7 mil denúncias) |
| **P2.** Em que faixa etária a mediação parental fica atrás da exposição e da autonomia digital? | Gabriela | Índices por faixa etária, regressão linear e análise de sensibilidade | **Não há ponto de corte único.** Aos 15–17 anos a exposição supera a mediação nos 9 pares testados |

## Principais resultados

| Resultado | Valor | Fonte |
|---|---|---|
| Denúncias novas de imagens de abuso e exploração sexual infantil, 2025 | 63.214 (+19,3% sobre 2024) | SaferNet |
| Pico histórico da série | 71.867 em 2023 | SaferNet |
| 2025 em relação a 2019 | 2,48x (CAGR de 16,3% ao ano) | Notebook, Fase 3 |
| Tendência log-linear 2019–2025 | 12,5% ao ano, R² 0,56, n = 7 | Notebook, Fase 4 |
| Erro (MAE) da validação 2012–2025: ingênuo · média 3 anos · tendência linear | 8.558 · 8.408 · 8.685 | Notebook, Fase 4 |
| Faixa de referência para 2026 (não é previsão confiável) | 62.693 a 65.803, erro típico ≈ 8,4 mil | Notebook, Fase 4 |
| Mediação restritiva (IMR) por faixa: 9–10 · 11–12 · 13–14 · 15–17 | 43 · 44 · 30 · 15 | TIC Kids 2025 |
| Exposição e autonomia (IEA) por faixa: 9–10 · 11–12 · 13–14 · 15–17 | 29 · 44 · 57 · 60 | TIC Kids 2025 |
| Inclinação por ano de idade: IMR · IEA (descritivo, n = 4) | −4,6 p.p. · +4,8 p.p. | Notebook, Fase 4 |
| Pares de indicadores em que a exposição supera a mediação aos 15–17 anos | 9 de 9 | Notebook, Fase 5 |
| Faixa em que a exposição passa a superar a mediação (varia com o indicador) | 11–12 anos em 4 de 9 pares; de 9–10 a 15–17 nos demais | Notebook, Fase 5 |
| Responsáveis que usam recurso técnico para limitar o tempo na Internet | 37% | TIC Kids 2025 |
| Responsáveis que conversam sobre o que o filho faz online | 44% | TIC Kids 2025 |
| Aprendem sobre uso seguro com a própria criança ou adolescente | 50% | TIC Kids 2025 |

**Como ler os índices.** IMR é a média de três indicadores (pais colocam regras para o celular, olham o celular, deixam o filho sem o celular por um tempo). IEA é a média de três (usou IA generativa, pesquisou produtos para comprar, realizou compras). São escolhas de modelagem, não medidas oficiais. Por isso há a análise de sensibilidade com os 9 pares.

## Observações

- **Os dois critérios de sucesso definidos na Fase 1 não foram atingidos**, e isso está no notebook como resultado, não escondido. O critério de P2 não foi relaxado depois de ver os dados.
- **Denúncias medem reporte, não ocorrência.** A alta pode vir de mais crimes, de mais canais de denúncia ou de ambos. Não se afirma causalidade.
- **n pequeno.** 20 anos (P1) e 4 faixas etárias (P2). Os números de inclinação e R² são descritivos.
- **Divergência entre edições da SaferNet:** a edição 2024 traz 25.166 (2011) e 17.443 (2015); a de 2025 traz 25.116 e 17.433. Foi usada a mais recente.
- **Próximo passo possível:** com os microdados do TIC Kids 2025 seria possível agrupar famílias por perfil de mediação (K-means) e prever quem não usa recurso técnico.

## Estrutura

```
├── dados/                          tabelas em CSV (fonte e confiança em cada linha)
├── notebooks/
│   └── crispdm_controle_parental.ipynb   6 fases do CRISP-DM, já executado
├── dashboard/                      3 páginas em PNG (Pandas, Matplotlib, Seaborn)
├── scripts/
│   ├── criar_dados.py              monta os CSVs
│   └── montar_notebook.py          gera o notebook
├── requirements.txt
└── README.md
```

## Como executar

```bash
pip install -r requirements.txt
python scripts/criar_dados.py
jupyter nbconvert --to notebook --execute --inplace notebooks/crispdm_controle_parental.ipynb
```

## Fontes

- SAFERNET BRASIL. *Indicadores: denúncias 2025.* [S. l.]: SaferNet Brasil, 2025. Disponível em: https://arquivos.safernet.org.br/pdfs/INDICADORES-DenunciasSaferNet2025.pdf. Acesso em: 4 nov. 2026.

- CETIC.BR; NIC.BR. *TIC Kids Online Brasil 2025: principais resultados.* São Paulo: Cetic.br; NIC.br, 2025. Disponível em: https://cetic.br/media/analises/tic_kids_online_brasil_2025_principais_resultados.pdf. Acesso em: 4 nov. 2026.

- FUNDAÇÃO TELEFÔNICA VIVO. *Divulgada pesquisa sobre o uso da internet por crianças e adolescentes: TIC Kids Online Brasil 2025.* [S. l.], 31 out. 2025. Disponível em: https://www.fundacaotelefonicavivo.org.br/wp-content/uploads/pdfs/NotaTecnicaTICKidsOnline2025.pdf. Acesso em: 4 nov. 2026.

- CHAPMAN, Pete et al. *CRISP-DM 1.0: step-by-step data mining guide.* [S. l.]: SPSS, 2000. Disponível em: https://www.the-modeling-agency.com/crisp-dm.pdf. Acesso em: 4 nov. 2026.
