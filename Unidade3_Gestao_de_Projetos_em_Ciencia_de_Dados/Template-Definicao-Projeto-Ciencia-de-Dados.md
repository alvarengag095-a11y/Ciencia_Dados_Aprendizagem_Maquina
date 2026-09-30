# Template - Definição do Projeto de Ciência de Dados

**Unidade:** III - Gestão de Projetos  
**Metodologia:** PBL + trabalho em equipes  
**Entregável:** Documento de definição do projeto

> **Finalidade:** delimitar um problema real e orientar o desenvolvimento do projeto de Ciência de Dados. Preencha todos os campos com informações objetivas, verificáveis e coerentes entre si.

## 1. Identificação do projeto

| Campo | Preenchimento |
|---|---|
| Título provisório do projeto |FERRAMENTAS DE CONTROLE PARENTAL: UMA ANÁLISE COMPARATIVA PARA A PROTEÇÃO INFNTOJUVENIL À LUZ DA LGPD E DO ECA DIGITAL |
| Curso / disciplina |CIÊNCIA DE DADOS |
| Turma | SISTEMAS DE INFORMAÇÃO |
| Equipe |GABRIELA MARCELA ALVARENGA / GRAZIELA MARCELA ALVARENGA |
| Integrantes e funções iniciais |GABRIELA MARCELA ALVARENGA / GRAZIELA MARCELA ALVARENGA |
| Professor(a) |FLÁVIA |
| Data de elaboração | 16/09/2026|
| Versão do documento |16.09 |

## 2. Visão geral

### 2.1 Resumo do projeto

Em até 100 palavras, apresente o problema, o público-alvo, a proposta de análise e o resultado esperado.

**Preenchimento:**

Problema: crianças e adolescentes estão expostos a riscos cibernéticos (grooming, sextorsão, cyberbullying, sharenting) nas redes sociais, agravados pelo uso dual da IA, sem que as ferramentas de controle parental sejam auditadas tecnicamente.

Público-alvo: pais/responsáveis, adolescentes, desenvolvedores e reguladores.

Proposta de análise: avaliação comparativa de cinco ferramentas (Google Family Link, Qustodio, Kaspersky Safe Kids, Microsoft Family Safety, KidsControl) por matriz multicritério e testes simulados, verificando mecanismos de PLN/ML na detecção de risco, transparência algorítmica (XAI), governança de dados e usabilidade (IHC), sob a LGPD e o ECA Digital.

Resultado esperado: ranking técnico auditado indicando quais ferramentas atendem a esses requisitos.

### 2.2 Declaração do projeto em uma frase

O projeto utilizará dados gerados em testes simulados de risco, somados à documentação técnica e às políticas de privacidade das ferramentas, para compreender a eficácia da detecção automatizada e o grau de transparência no tratamento dos dados, apoiando famílias e desenvolvedores na decisão de qual ferramenta adotar e quais requisitos exigir de sistemas de proteção infantojuvenil.

**Versão da equipe:**

________________________________________________________________________________

## 3. Contexto e definição do problema

### 3.1 Contexto

Descreva a situação atual, o ambiente em que o problema ocorre e as evidências iniciais que demonstram sua relevância.

- Onde o problema ocorre? Em redes sociais, aplicativos de mensagens, jogos e plataformas gamificadas acessadas por crianças e adolescentes, majoritariamente em dispositivos móveis de uso doméstico.
- Quem é afetado? Crianças e adolescentes de 9 a 17 anos, diretamente e pais e responsáveis, que assumem a mediação sem informação técnica suficiente.
- Quais sinais, dados ou relatos indicam sua existência? 93% das crianças e adolescentes brasileiros de 9 a 17 anos usam internet (cerca de 25 milhões), e 23% iniciaram o acesso antes dos 6 anos.
Cerca de 300 milhões de crianças e jovens no mundo sofreram algum tipo de crime cibernético em 12 meses, segundo relatório das Nações Unidas.
Estima-se que 19% do público de 12 a 17 anos já sofreu violência sexual facilitada por meios tecnológicos (UNICEF Innocenti, ECPAT, Interpol).
- Por que é importante investigá-lo agora? A entrada em vigor do ECA Digital (Lei nº 15.211/2025) cria obrigações novas de verificação de idade, supervisão parental e tratamento de dados de menores, mas não existe avaliação técnica independente que verifique se as ferramentas já disponíveis no mercado cumprem esses requisitos ou se elas próprias respeitam essa privacidade.


### 3.2 Problema central

Pais e responsáveis enfrentam a ausência de informação técnica comparável e verificável sobre ferramentas de controle parental, no contexto da crescente exposição infantojuvenil a crimes cibernéticos potencializados por inteligência artificial, produzindo escolhas de proteção baseadas em marketing e não em evidência, com risco de adotar soluções ineficazes na detecção de conteúdo de risco ou excessivamente invasivas em relação aos dados do próprio menor.

### 3.3 Evidências iniciais

| Evidência | Fonte | O que ela indica? | Confiabilidade / limitação |
|---|---|---|---|
| 1. |	93% dos brasileiros de 9 a 17 anos usam internet; 23% começaram antes dos 6 anos | Exposição precoce e praticamente universal, ampliando a superfície de risco|Alta (pesquisa oficial). Não mede incidentes, apenas acesso |
| 2. |	300 milhões de crianças e jovens vítimas de crime cibernético em 12 meses | Dimensão global do problema|Alta credibilidade institucional; estimativa agregada, sem recorte Brasil |
| 3. | 	19% do público de 12 a 17 anos sofreu violência sexual facilitada por tecnologia|Gravidade e prevalência dos crimes de natureza sexual online |Alta; metodologia de autorrelato pode gerar subnotificação |

## 4. Público-alvo e partes interessadas

### 4.1 Público-alvo principal

| Aspecto | Descrição |
|---|---|
| Quem são os usuários ou beneficiários? | Pais e responsáveis por crianças e adolescentes de 9 a 17 anos e os próprios menores monitorados. Secundariamente, desenvolvedores de software e órgãos reguladores|
| Quais necessidades possuem? |Proteger o menor sem depender de conhecimento técnico avançado; entender o que a ferramenta coleta e por que bloqueia; preservar a relação de confiança com o adolescente; cumprir o dever legal de cuidado |
| Como são afetados pelo problema? |Escolhem ferramentas sem base comparativa; podem confiar em soluções que falham na detecção de risco real ou que coletam dados sensíveis do menor além do necessário; adolescentes ficam sujeitos a decisões automatizadas sem explicação |
| Que decisão ou ação poderão tomar com os resultados? | Selecionar a ferramenta mais adequada ao seu contexto familiar, ajustar configurações de privacidade, e — no caso de desenvolvedores e reguladores — adotar ou exigir requisitos mínimos de transparência e minimização de dados|

### 4.2 Partes interessadas

| Parte interessada | Interesse no projeto | Influência | Forma de envolvimento |
|---|---|---|---|
|Famílias (pais e responsáveis) |	Escolher proteção eficaz e não invasiva |Alta |	Público-alvo dos resultados; validação da clareza do ranking |
|Desenvolvedores de software |Requisitos claros de Privacy by Design e XAI | Alta |	Destinatários do framework de requisitos proposto |
|Reguladores (ANPD, conselhos de direitos) |Fiscalizar a aplicação da LGPD e do ECA Digital | Alta |	Potenciais usuários dos indicadores de conformidade |
| Crianças e adolescentes|	Ser protegido sem vigilância arbitrária; direito à explicação | Média|	Considerados como usuários na avaliação de IHC (interface do lado supervisionado) |

## 5. Objetivos do projeto

### 5.1 Objetivo geral

Avaliar, por meio de uma matriz multicritério aplicada em testes simulados, o desempenho técnico de cinco ferramentas de controle parental quanto à detecção automatizada de conteúdo de risco, à transparência algorítmica, à governança de dados e à usabilidade, a fim de subsidiar a escolha informada por famílias e a definição de requisitos de projeto para desenvolvedores, no contexto da LGPD e do ECA Digital.

________________________________________________________________________________

### 5.2 Objetivos específicos

Defina de três a cinco objetivos mensuráveis e compatíveis com o prazo do projeto.

| Nº | Objetivo específico | Evidência de conclusão |
|---:|---|---|
| 1 |	Construir uma matriz multicritério |Matriz validada pela orientadora, com definição operacional de cada critério e da régua de pontuação |
| 2 |Levantar e catalogar a documentação técnica, os termos de uso e as políticas de privacidade das cinco ferramentas selecionadas|Base documental estruturada, com data de coleta e extração das cláusulas relativas a coleta, retenção e compartilhamento de dados |
| 3 |	Executar um protocolo padronizado de testes simulados de risco em ambiente controlado, registrando detecções, alertas e bloqueios de cada ferramenta |Planilha de registro com um caso de teste por linha e resultado observado |
| 4 | 	Analisar comparativamente os resultados, gerando pontuação por dimensão e taxas de detecção, falso positivo e falso negativo por ferramenta|Painel de visualizações e ranking técnico consolidado |
| 5 | | |

### 5.3 Verificação dos objetivos

Marque após revisar:

- [X] São específicos e escritos com clareza.
- [X] Podem ser verificados por meio de entregáveis ou métricas.
- [X] São viáveis com os dados, recursos e tempo disponíveis.
- [X] Estão diretamente relacionados ao problema central.
- [X] Consideram os usuários e a decisão que será apoiada.

## 6. Perguntas de negócio

As perguntas de negócio orientam a coleta, a análise e a comunicação dos resultados. Evite perguntas que possam ser respondidas apenas com “sim” ou “não”.

| Nº | Pergunta de negócio | Decisão apoiada | Dados necessários | Análise ou indicador possível |
|---:|---|---|---|---|
| 1 |	Em que medida cada ferramenta detecta conteúdo textual de risco em português brasileiro, incluindo gírias e grafias evasivas? |Escolha da ferramenta por famílias | Registros dos casos de teste simulados e respostas de cada ferramenta| Taxa de detecção, falso negativo e falso positivo por ferramenta|
| 2 |	Que grau de explicação as ferramentas oferecem ao responsável e ao menor quando bloqueiam conteúdo ou emitem alerta? |Exigência de explicabilidade em contratos e políticas |Capturas de tela dos alertas e mensagens de bloqueio nas duas interfaces | Índice de explicabilidade (escala 0–3) por ferramenta e por tipo de evento|
| 3 |Quais categorias de dados pessoais cada ferramenta coleta e por quanto tempo os retém, em relação ao estritamente necessário? | Avaliação de conformidade com a minimização prevista na LGPD| Políticas de privacidade, permissões solicitadas pelo app e configurações disponíveis|Índice de minimização: razão entre dados coletados e dados justificados pela finalidade declarada |
| 4 | De que forma o fluxo de consentimento das ferramentas influencia a decisão do responsável de autorizar coleta adicional?|Recomendações de design para desenvolvedores |Sequência de telas de onboarding e opções pré-marcadas |Contagem e tipificação de dark patterns identificados por ferramenta |

## 7. Hipóteses iniciais

Registre suposições que serão investigadas, sem apresentá-las como conclusões.

| Hipótese | Como poderá ser testada? | Resultado que a refutaria? |
|---|---|---|
| 	Há relação inversa entre volume de dados coletados e clareza da explicação oferecida ao usuário: quanto mais a ferramenta coleta, menos explica |Cruzamento entre o índice de minimização e o índice de explicabilidade das cinco ferramentas | Ausência de relação, ou ferramentas que coletam mais e também explicam mais|
|A interface do lado supervisionado (menor) oferece menos informação sobre o monitoramento do que a interface do responsável | Avaliação heurística comparada das duas interfaces, com o mesmo conjunto de heurísticas de Nielsen|Paridade informacional entre as duas interfaces |
|	Nenhuma das cinco ferramentas atende integralmente aos requisitos combinados de eficácia, minimização de dados e explicabilidade |Verificação do atendimento pleno aos critérios das três dimensões da matriz |Pelo menos uma ferramenta com pontuação máxima nas três dimensões |

## 8. Dados necessários e viabilidade

| Conjunto ou fonte de dados | Variáveis principais | Formato | Acesso / responsável | Qualidade esperada |
|---|---|---|---|---|
|Registros dos testes simulados de risco |ID do caso, categoria de risco, ferramenta, detecção (sim/não), tipo de alerta, tempo de resposta, texto exibid |Tabela | Gerado pela equipe| Alta |
|Estatísticas públicas de exposição e incidentes |Faixa etária, tipo de incidente, ano, região |Relatórios (PDF) e tabelas |SaferNet, TIC Kids Online Brasil, ONU, UNICEF |Alta  |
|Permissões e metadados dos aplicativos | Permissões solicitadas, versão, última atualização, faixa etária declarada| Ficha da loja de aplicativos| Público; equipe| Alta para permissões; média para descrições comerciais|

### 8.1 Avaliação inicial dos dados

- **Disponibilidade:** os dados primários dependem apenas da execução do protocolo pela equipe; os secundários são públicos e de acesso imediato.
- **Volume e período coberto:** estimados 3 ferramentas × cerca de 15 casos de teste; documentação referente às versões vigentes no mesmo período.
- **Dados ausentes, duplicados ou inconsistentes previstos:** ausência de informação sobre técnicas de IA; possível divergência entre o que a política declara e o que o aplicativo solicita em permissões.
- **Necessidade de integração entre fontes:** sim — a pontuação final exige unir registros de teste, codificação das interfaces e extração das políticas por meio de um identificador comum de ferramenta e critério.
- **Restrições legais, contratuais ou institucionais:** os termos de uso de algumas ferramentas restringem engenharia reversa e uso automatizado; a auditoria se limita à observação de comportamento na interface, sem interceptação de tráfego ou descompilação.

### 8.2 Privacidade, ética e segurança

- [X] A equipe verificou se há dados pessoais ou sensíveis.
- [X] A coleta e o uso dos dados possuem finalidade legítima e explícita.
- [X] O acesso será limitado às pessoas autorizadas.
- [X] Dados pessoais serão minimizados, anonimizados ou pseudonimizados quando necessário.
- [X] Possíveis vieses e impactos sobre grupos serão analisados.
- [X] A divulgação dos resultados evitará reidentificação ou exposição indevida.

**Cuidados específicos deste projeto:** Nenhuma criança ou adolescente real participa dos testes: os cenários de risco são simulados em contas e dispositivos de teste criados pela própria equipe, com perfis fictícios. Não há coleta de conversas reais, prints de terceiros ou dados de usuários das plataformas. O conteúdo textual usado nos testes é construído pela equipe a partir de tipologias descritas na literatura, sem reproduzir material de abuso. As capturas de tela publicadas no trabalho serão tratadas para remover identificadores de conta. Os resultados serão apresentados como avaliação técnica de produtos.

________________________________________________________________________________

## 9. Escopo do projeto

| Dentro do escopo | Fora do escopo |
|---|---|
|três ferramentas: Google Family Link, Qustodio, Microsoft Family Safety |Desenvolvimento ou treinamento de modelo próprio de PLN/ML |
|Testes simulados de detecção em ambiente controlado |Interceptação de tráfego, engenharia reversa ou análise de código-fonte |
|Verificação de aderência à LGPD (com ênfase no art. 14) e ao ECA Digital |Ferramentas fora da lista definida e plataformas exclusivas de outros mercados |

**Restrições conhecidas:** Prazo curto; versões gratuitas ou de teste das ferramentas podem limitar funcionalidades avaliáveis; ausência de APIs públicas de classificação impede medição direta de acurácia dos modelos, restringindo a análise ao comportamento observável na interface; equipe de duas integrantes conciliando outras disciplinas.

________________________________________________________________________________

## 10. Resultados e entregáveis previstos

| Entregável | Descrição | Formato | Responsável | Critério de aceite |
|---|---|---|---|---|
| Base tratada | 	Registros dos testes e extração das políticas, unificados por ferramenta e critério|Tabela | Gabriela|	Sem registros duplicados; todos os casos de teste com resultado preenchido e evidência associada |
| Análise exploratória | | | | |
| Visualizações / painel |Pontuação de cada ferramenta nos critérios |tabela no TCC |Equipe |	Cada pontuação rastreável a uma evidência registrada |
| Relatório ou apresentação | Monografia completa e apresentação para a banca| Documento e slides|Equipe |Aderente às normas ABNT e ao cronograma da orientação |
| Outro | | | | |

## 11. Critérios de sucesso

Defina como a equipe saberá se o projeto alcançou seus objetivos.

| Critério | Indicador ou evidência | Meta | Forma de verificação |
|---|---|---|---|
| Relevância para o problema |Resultados dos testes | Todas as plataformas| 	Conferência entre a a pergunta central e o capítulo de resultados|
| Qualidade dos dados |Casos de teste executados |≥ 95% dos casos previstos |Auditoria da base tratada |
| Qualidade da análise |Células da matriz com justificativa rastreável | 100%| 	Revisão cruzada entre as integrantes e validação da orientadora|
| Utilidade para o público-alvo | Ranking compreensível por leitor sem formação técnica| Aprovado em leitura|Leitura-teste informal antes da entrega final |
| Comunicação dos resultados | Apresentação entregue no prazo e de acordo com a ABNT| Sem pendências |Validação da orientadora e da banca |

## 12. Plano inicial de trabalho

| Etapa | Atividades principais | Responsável(is) | Prazo | Dependências |
|---|---|---|---|---|
| 1. Definição |Ajuste do título e do problema, revisão do referencial (crimes cibernéticos, IA, marco regulatório, IHC)|Equipe|	Setembro/2026| |
| 2. Obtenção dos dados |Seleção final das ferramentas, criação das contas de teste, coleta das políticas e permissões | Equipe| Outubro/2026|	Etapa 1 e definição sobre versões pagas |
| 3. Preparação dos dados |Construção da matriz multicritério, do protocolo de testes e da planilha de codificação |Equipe |Outubro/2026 |Etapa 2|
| 4. Análise / modelagem |Execução dos testes simulados, pontuação da matriz, análise exploratória e visualizações |Equipe |Outubro–Novembro/2026 |Etapa 3 |
| 5. Validação | Revisão cruzada das pontuações, verificação das hipóteses, validação com a orientadora|Equipe  |Novembro/2026 |Etapa 4 |
| 6. Comunicação | Redação do ranking e do framework, conclusão, revisão ABNT e apresentação| Equipe |Novembro–Dezembro/2026 |Etapa 5 |

## 13. Riscos do projeto

| Risco | Probabilidade | Impacto | Estratégia de resposta | Responsável |
|---|---|---|---|---|
|Atualização das ferramentas durante o período de testes, alterando comportamento | Média |  Médio  |	Registrar número de versão e data em cada teste; concentrar a coleta em janela curta |Equipe |
| Atraso pelo acúmulo com outras disciplinas|Média |  Alto | Reuniões semanais de acompanhamento aos sábados; entregas parciais por capítulo|Equipe e Flávia |
|Documentação técnica insuficiente sobre as técnicas de IA empregadas |Média | Alto |Tratar a opacidade como resultado da auditoria, pontuando-a no critério de transparência | Equipe|

## 14. Organização da equipe

| Integrante | Papel principal | Responsabilidades | Apoio necessário |
|---|---|---|---|
| Profa. Flávia|Orientação |Validação do recorte técnico, do instrumento de avaliação e das entregas por capítulo |Reuniões semanais aos sábados, às 14h30 |
| Graziela Marcela Alvarenga Silva Viana| Levantamento documenta|Coleta das políticas e permissões, execução do protocolo de teste | Dispositivo dedicado para os testes; revisão cruzada das pontuações|
|Gabriela Marcela Alvarenga Silva Viana |Coordenação técnica | Matriz multicritério, tratamento da base, análise exploratória, redação dos capítulos de metodologia e resultados|Validação metodológica da orientadora; acesso às versões de teste das ferramentas |


## 15. Validação da definição do projeto

Antes da entrega, confirme:

- [X] O problema é real, relevante e delimitado.
- [X] O público-alvo e as partes interessadas estão identificados.
- [X] O objetivo geral e os objetivos específicos são coerentes.
- [X] As perguntas de negócio orientam decisões concretas.
- [X] Há dados potencialmente disponíveis para responder às perguntas.
- [X] O escopo é compatível com o prazo e os recursos.
- [X] Os critérios de sucesso são mensuráveis.
- [X] Riscos, privacidade, ética e segurança foram considerados.
- [X] Funções e responsabilidades foram distribuídas.

## 16. Aprovação e registro de ajustes

| Responsável | Validação / observação | Data |
|---|---|---|
| Representante da equipe | | |
| Professor(a) / orientador(a) |Flávia | |

### Ajustes solicitados após a apresentação inicial

________________________________________________________________________________

________________________________________________________________________________

