"""
Monta as tabelas de dados do projeto a partir de números PÚBLICOS já publicados.
Nenhum valor é simulado. Cada linha traz a fonte e o nível de confiança da extração:

  confirmado_texto  -> o número aparece escrito em texto (nota técnica, matéria ou tabela)
  leitura_grafico   -> o número foi lido de um gráfico do PDF "Principais Resultados"
                       (conferir nas tabelas oficiais do Cetic.br antes de entregar)
"""
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados"
DADOS.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# 1) SaferNet - denúncias NOVAS (links únicos) de imagens de abuso e
#    exploração sexual infantil, 2006-2025
#    Fonte: SaferNet Brasil, "Indicadores Denúncias 2025" (PDF)
#    https://arquivos.safernet.org.br/pdfs/INDICADORES-DenunciasSaferNet2025.pdf
# ---------------------------------------------------------------------------
csam = {
    2006: 13750, 2007: 34895, 2008: 56115, 2009: 41269, 2010: 33909,
    2011: 25116, 2012: 24073, 2013: 24993, 2014: 22789, 2015: 17433,
    2016: 17645, 2017: 21473, 2018: 24618, 2019: 25518, 2020: 46019,
    2021: 53960, 2022: 40572, 2023: 71867, 2024: 52999, 2025: 63214,
}
pd.DataFrame(
    {"ano": list(csam), "denuncias_novas_csam": list(csam.values()),
     "fonte": "SaferNet - Indicadores Denuncias 2025"}
).to_csv(DADOS / "safernet_csam_2006_2025.csv", index=False)

# ---------------------------------------------------------------------------
# 2) SaferNet - denúncias novas por tipo de crime, 2024 x 2025 (mesma fonte)
# ---------------------------------------------------------------------------
tipos = [
    ("Imagens de abuso e exploração sexual infantil", 52999, 63214, "infantojuvenil"),
    ("Intolerância religiosa", 954, 1145, "outros"),
    ("Neonazismo", 814, 1341, "outros"),
    ("Apologia e incitação a crimes contra a vida", 2710, 4752, "outros"),
    ("Racismo", 2032, 3220, "outros"),
    ("LGBTfobia", 1463, 1819, "outros"),
    ("Misoginia", 2686, 8728, "outros"),
    ("Maus tratos contra animais", 741, 1137, "outros"),
    ("Tráfico de pessoas", 438, 442, "outros"),
    ("Xenofobia", 3449, 755, "outros"),
]
df_tipos = pd.DataFrame(tipos, columns=["crime", "ano_2024", "ano_2025", "recorte"])
df_tipos["variacao_pct"] = ((df_tipos.ano_2025 / df_tipos.ano_2024 - 1) * 100).round(1)
df_tipos["fonte"] = "SaferNet - Indicadores Denuncias 2025"
df_tipos.to_csv(DADOS / "safernet_tipos_2024_2025.csv", index=False)

# ---------------------------------------------------------------------------
# 3) TIC Kids Online Brasil 2025 - indicadores por faixa etária (9 a 17 anos)
#    Fonte: Cetic.br/NIC.br, "TIC Kids Online Brasil 2025 - Principais Resultados"
#    (22/10/2025); amostra de 2.370 crianças/adolescentes e 2.370 responsáveis
#    https://www.cetic.br/media/analises/tic_kids_online_brasil_2025_principais_resultados.pdf
#    Notas de apoio: Fundação Telefônica Vivo (nota técnica de 31/10/2025) e
#    TeleTime (22/10/2025), para conferir os totais.
# ---------------------------------------------------------------------------
GRUPOS = ["Total", "9-10", "11-12", "13-14", "15-17"]
PDF = "Cetic.br - Principais Resultados 2025"

def linha(bloco, indicador, valores, universo, conf, obs=""):
    """valores: lista alinhada a GRUPOS (None quando o grupo não se aplica)."""
    return [
        dict(bloco=bloco, indicador=indicador, grupo=g, valor_pct=v,
             universo=universo, confianca=conf, fonte=PDF, observacao=obs)
        for g, v in zip(GRUPOS, valores) if v is not None
    ]

L = []
# --- Mediação parental (restritiva e de acompanhamento)
L += linha("mediacao", "Pais colocam regras para usar o celular",
           [37, 58, 50, 35, 18], "9-17", "leitura_grafico",
           "Total 37% confirmado na nota técnica da Fundação Telefônica; "
           "valores por faixa lidos do gráfico")
L += linha("mediacao", "Pais olham o celular (com quem fala / o que faz)",
           [35, 46, 49, 36, 18], "9-17", "leitura_grafico")
L += linha("mediacao", "Pais deixam sem usar o celular por algum tempo",
           [20, 26, 34, 18, 10], "9-17", "leitura_grafico")
L += linha("mediacao", "Percebe que os pais sabem 'muito' do que faz online",
           [53, 62, 65, 51, 42], "9-17", "leitura_grafico",
           "Total 53% confirmado na nota técnica da Fundação Telefônica")
L += linha("mediacao", "Ajuda os pais a fazer algo na Internet",
           [31, 15, 27, 41, 37], "9-17", "confirmado_texto")
# --- Exposição / autonomia
L += linha("exposicao", "Usou IA generativa (ao menos uma atividade)",
           [65, 42, 62, 75, 75], "9-17", "confirmado_texto")
L += linha("exposicao", "Pesquisou produtos na Internet para comprar",
           [63, 42, 60, 72, 72], "9-17", "confirmado_texto")
L += linha("exposicao", "Realizou compras na Internet",
           [20, 4, 11, 23, 33], "9-17", "confirmado_texto")
L += linha("exposicao", "Tentou vender coisas na Internet",
           [4, 3, 1, 5, 8], "9-17", "confirmado_texto")
L += linha("exposicao", "Sabe diferenciar conteúdo patrocinado de não patrocinado",
           [54, None, 30, 63, 64], "11-17", "confirmado_texto")
L += linha("exposicao", "Gastou em jogos online (itens/fases)",
           [21, None, 16, 22, 24], "11-17", "confirmado_texto")
pd.DataFrame(L).to_csv(DADOS / "ticKids2025_por_faixa_etaria.csv", index=False)

# --- Totais nacionais (sem recorte por idade)
T = [
    ("acesso", "Usuários de Internet de 9 a 17 anos", 92, "confirmado_texto",
     "Nota técnica Fundação Telefônica; 24.585.769 usuários nos últimos 3 meses"),
    ("acesso", "Usam o celular para acessar a Internet", 96, "confirmado_texto",
     "Nota técnica Fundação Telefônica"),
    ("acesso", "Começaram a usar a Internet até os 6 anos (2025)", 28, "confirmado_texto",
     "Era 10% em 2016"),
    ("acesso", "Começaram a usar a Internet até os 6 anos (2016)", 10, "confirmado_texto", ""),
    ("acesso", "Acessam a Internet pelo celular na escola (2024)", 51, "confirmado_texto", ""),
    ("acesso", "Acessam a Internet pelo celular na escola (2025)", 37, "confirmado_texto", ""),
    ("mediacao_tecnica", "Recurso que limita o tempo na Internet", 37, "confirmado_texto",
     "TeleTime 22/10/2025"),
    ("mediacao_tecnica", "Recurso para monitorar sites/aplicativos acessados", 34, "leitura_grafico", ""),
    ("mediacao_tecnica", "Recurso que filtra aplicativos que pode baixar", 33, "leitura_grafico", ""),
    ("mediacao_tecnica", "Recurso para bloquear ou filtrar tipos de sites", 33, "leitura_grafico", ""),
    ("mediacao_tecnica", "Recurso que alerta sobre compras em aplicativos", 31, "leitura_grafico", ""),
    ("mediacao_tecnica", "Recurso que limita com quem pode falar (chamadas/mensagens)", 27, "leitura_grafico", ""),
    ("mediacao_tecnica", "Bloqueio de anúncios", 22, "leitura_grafico", ""),
    ("mediacao_dialogo", "Pais conversam sobre o que o filho faz na Internet", 44, "confirmado_texto",
     "Nota técnica Fundação Telefônica; TeleTime"),
    ("fonte_orientacao", "Aprendem sobre uso seguro com a própria criança/adolescente", 50, "confirmado_texto", ""),
    ("fonte_orientacao", "Familiares ou amigos", 48, "confirmado_texto", ""),
    ("fonte_orientacao", "TV, rádio, jornais ou revistas", 42, "leitura_grafico", ""),
    ("fonte_orientacao", "Escola da criança/adolescente", 41, "leitura_grafico", ""),
    ("fonte_orientacao", "Sites com informações sobre segurança", 37, "leitura_grafico", ""),
    ("fonte_orientacao", "Vídeos ou tutoriais online", 36, "leitura_grafico", ""),
    ("fonte_orientacao", "Grupos de pais em redes sociais", 31, "leitura_grafico", ""),
    ("fonte_orientacao", "Provedores de serviços de Internet", 30, "leitura_grafico", ""),
    ("fonte_orientacao", "Governo ou autoridades locais", 25, "leitura_grafico", ""),
    ("fonte_orientacao", "Fabricantes e varejistas de produtos infantis", 21, "leitura_grafico", ""),
    ("fonte_orientacao", "ONGs ou institutos pró-crianças", 19, "leitura_grafico", ""),
    ("riscos", "Contato com propaganda inadequada para a idade (relato dos responsáveis)", 45, "confirmado_texto",
     "Matéria Viva, a partir do TIC Kids 2025"),
    ("riscos", "Pediram algum produto após ver anúncio", 51, "confirmado_texto", ""),
]
pd.DataFrame(T, columns=["bloco", "indicador", "valor_pct", "confianca", "observacao"]).assign(
    fonte=PDF + " / notas de apoio"
).to_csv(DADOS / "ticKids2025_totais.csv", index=False)

print("Arquivos gerados em", DADOS)
for p in sorted(DADOS.glob("*.csv")):
    print(" -", p.name, len(pd.read_csv(p)), "linhas")
