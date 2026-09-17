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
| | | Baixa / Média / Alta | |
| | | Baixa / Média / Alta | |
| | | Baixa / Média / Alta | |

## 5. Objetivos do projeto

### 5.1 Objetivo geral

Escreva um objetivo que indique o que será analisado, para qual finalidade e em qual contexto. Inicie com um verbo no infinitivo.

**Objetivo geral:**

________________________________________________________________________________

### 5.2 Objetivos específicos

Defina de três a cinco objetivos mensuráveis e compatíveis com o prazo do projeto.

| Nº | Objetivo específico | Evidência de conclusão |
|---:|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

### 5.3 Verificação dos objetivos

Marque após revisar:

- [ ] São específicos e escritos com clareza.
- [ ] Podem ser verificados por meio de entregáveis ou métricas.
- [ ] São viáveis com os dados, recursos e tempo disponíveis.
- [ ] Estão diretamente relacionados ao problema central.
- [ ] Consideram os usuários e a decisão que será apoiada.

## 6. Perguntas de negócio

As perguntas de negócio orientam a coleta, a análise e a comunicação dos resultados. Evite perguntas que possam ser respondidas apenas com “sim” ou “não”.

| Nº | Pergunta de negócio | Decisão apoiada | Dados necessários | Análise ou indicador possível |
|---:|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

## 7. Hipóteses iniciais

Registre suposições que serão investigadas, sem apresentá-las como conclusões.

| Hipótese | Como poderá ser testada? | Resultado que a refutaria? |
|---|---|---|
| H1. | | |
| H2. | | |
| H3. | | |

## 8. Dados necessários e viabilidade

| Conjunto ou fonte de dados | Variáveis principais | Formato | Acesso / responsável | Qualidade esperada |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

### 8.1 Avaliação inicial dos dados

- **Disponibilidade:** __________________________________________________________
- **Volume e período coberto:** __________________________________________________
- **Dados ausentes, duplicados ou inconsistentes previstos:** ______________________
- **Necessidade de integração entre fontes:** _____________________________________
- **Restrições legais, contratuais ou institucionais:** _____________________________

### 8.2 Privacidade, ética e segurança

- [ ] A equipe verificou se há dados pessoais ou sensíveis.
- [ ] A coleta e o uso dos dados possuem finalidade legítima e explícita.
- [ ] O acesso será limitado às pessoas autorizadas.
- [ ] Dados pessoais serão minimizados, anonimizados ou pseudonimizados quando necessário.
- [ ] Possíveis vieses e impactos sobre grupos serão analisados.
- [ ] A divulgação dos resultados evitará reidentificação ou exposição indevida.

**Cuidados específicos deste projeto:**

________________________________________________________________________________

## 9. Escopo do projeto

| Dentro do escopo | Fora do escopo |
|---|---|
| | |
| | |
| | |

**Restrições conhecidas:** tempo, acesso a dados, ferramentas, infraestrutura, conhecimento técnico ou normas.

________________________________________________________________________________

## 10. Resultados e entregáveis previstos

| Entregável | Descrição | Formato | Responsável | Critério de aceite |
|---|---|---|---|---|
| Base tratada | | | | |
| Análise exploratória | | | | |
| Visualizações / painel | | | | |
| Relatório ou apresentação | | | | |
| Outro | | | | |

## 11. Critérios de sucesso

Defina como a equipe saberá se o projeto alcançou seus objetivos.

| Critério | Indicador ou evidência | Meta | Forma de verificação |
|---|---|---|---|
| Relevância para o problema | | | |
| Qualidade dos dados | | | |
| Qualidade da análise | | | |
| Utilidade para o público-alvo | | | |
| Comunicação dos resultados | | | |

## 12. Plano inicial de trabalho

| Etapa | Atividades principais | Responsável(is) | Prazo | Dependências |
|---|---|---|---|---|
| 1. Definição | | | | |
| 2. Obtenção dos dados | | | | |
| 3. Preparação dos dados | | | | |
| 4. Análise / modelagem | | | | |
| 5. Validação | | | | |
| 6. Comunicação | | | | |

## 13. Riscos do projeto

| Risco | Probabilidade | Impacto | Estratégia de resposta | Responsável |
|---|---|---|---|---|
| | Baixa / Média / Alta | Baixo / Médio / Alto | | |
| | Baixa / Média / Alta | Baixo / Médio / Alto | | |
| | Baixa / Média / Alta | Baixo / Médio / Alto | | |

## 14. Organização da equipe

| Integrante | Papel principal | Responsabilidades | Apoio necessário |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

## 15. Validação da definição do projeto

Antes da entrega, confirme:

- [ ] O problema é real, relevante e delimitado.
- [ ] O público-alvo e as partes interessadas estão identificados.
- [ ] O objetivo geral e os objetivos específicos são coerentes.
- [ ] As perguntas de negócio orientam decisões concretas.
- [ ] Há dados potencialmente disponíveis para responder às perguntas.
- [ ] O escopo é compatível com o prazo e os recursos.
- [ ] Os critérios de sucesso são mensuráveis.
- [ ] Riscos, privacidade, ética e segurança foram considerados.
- [ ] Funções e responsabilidades foram distribuídas.

## 16. Aprovação e registro de ajustes

| Responsável | Validação / observação | Data |
|---|---|---|
| Representante da equipe | | |
| Professor(a) / orientador(a) | | |

### Ajustes solicitados após a apresentação inicial

________________________________________________________________________________

________________________________________________________________________________

