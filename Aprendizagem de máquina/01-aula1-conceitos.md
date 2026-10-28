<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Aula 1 — Conceitos e classificação de problemas

## Identificação

- Estudante ou equipe: Gabriela Marcela Alvarenga
- Turma: Sistemas de Informação
- Data de realização: Não se aplica
- Integrantes e contribuições (se em equipe): Não se aplica

## Objetivos

Distinguir programação tradicional e Machine Learning, identificar atributos e alvo e diferenciar classificação, regressão e agrupamento.

## 1. Explicação com suas palavras

1. Como um modelo aprende com dados? Um modelo de Aprendizagem de Máquina aprende por meio da análise de dados, identificando padrões e relações entre as informações. Durante o treinamento, ele ajusta seus parâmetros com base nos exemplos recebidos para reduzir erros
2. Qual diferença entre algoritmo e modelo? O algoritmo é o conjunto de regras ou método utilizado para aprender com os dados e o modelo é o resultado desse aprendizado após o treinamento.
3. Compare uma regra de bloqueio de palavra com um modelo de spam. Uma regra de bloqueio de palavra bloqueia mensagens que contêm termos específicos previamente definidos. Já um modelo de spam aprende com exemplos de mensagens para identificar padrões e classificar mensagens suspeitas como spam.
4. Dê um exemplo de atributo e alvo e defina o momento da previsão. Prever se um aluno será aprovado ou reprovado.
- Atributos: notas das provas e quantidade de faltas.
- Alvo: aprovado ou reprovado.
- Momento da previsão: ao final do primeiro semestre, usando apenas as notas e faltas registradas até esse período, para identificar alunos que precisam de apoio antes do fim do ano letivo.

## 2. Quadro comparativo

| Critério | Supervisionado | Não supervisionado |
| --- | --- | --- |
| Presença de alvo no treino | Sim: cada exemplo vem com o valor. | Não: os dados não têm alvo definido. |
| Pergunta que pode responder | "Qual será a categoria ou o valor para este novo caso?" | "Que estruturas, grupos ou padrões existem nestes dados?" |
| Tipo de saída | Uma classe (categoria) ou um número. | Grupos, segmentos ou padrões descobertos. |
| Tarefas e exemplo | Classificação (spam ou legítima) e regressão (estimar vendas da próxima semana). | Agrupamento (segmentar clientes por perfil de compra) e detecção de operações atípicas. |
| Dados necessários | Atributos mais alvo conhecido, em volume e qualidade suficientes. | Apenas atributos, sem necessidade de rótulos. |
| Forma de avaliação | Comparar previsões com o alvo real em dados de teste (acurácia, precisão, recall, erro médio etc.). | Não há resposta correta para comparar; usa-se coesão e separação dos grupos e, principalmente, a interpretação e a utilidade para o problema. |
| Limitação | Rotular dados é caro e demorado, e o modelo reproduz vieses e erros dos rótulos. | Os grupos podem não ter significado prático, dependem de escolhas (como o número de grupos) e são difíceis de validar objetivamente. |

## 3. Situações-problema

Os casos são cenários didáticos. Escolha **pelo menos cinco** e justifique sua classificação pelo significado do alvo ou por sua ausência.

| Caso | Situação-problema |
| --- | --- |
| 1 Educação | Prever evadiu/permaneceu com histórico rotulado de turmas anteriores. |
| 2 Saúde | Estimar o tempo de espera em minutos a partir de registros de atendimento. |
| 3 Comércio | Descobrir perfis de compra sem categorias prévias de clientes. |
| 4 Finanças | Prever inadimplente/adimplente com contratos e desfechos conhecidos. |
| 5 Segurança digital | Distinguir spam/legítima com mensagens já revisadas. |
| 6 Comércio | Estimar o total de vendas em reais na próxima semana. |
| 7 Educação | Agrupar perfis de acesso ao ambiente virtual sem rótulo de evasão. |
| 8 Saúde | Classificar exames em categorias previamente definidas por especialistas. |

| Caso escolhido | Alvo ou ausência de alvo | Categoria, quantidade ou grupos? | Abordagem e justificativa | Dados necessários e limitação |
| --- | --- | --- | --- | --- |
| 1 Educação | Alvo: evadiu ou permaneceu (rótulo conhecido das turmas anteriores). | Categoria (duas classes). | Aprendizado supervisionado, classificação binária. O alvo é uma categoria e existem exemplos rotulados para treinar. | Dados: notas, faltas, acessos, perfil da turma, com o desfecho de cada estudante. Limitação: classes desbalanceadas (poucos evadidos) e risco de usar informações que só existem depois da evasão. |
| 2 Saúde | Alvo: tempo de espera em minutos. | Quantidade (valor numérico contínuo). | Aprendizado supervisionado, regressão. O alvo é um número, não uma categoria. | Dados: horário de chegada, tipo de atendimento, nível de urgência, equipe disponível, tempo de espera real. Limitação: eventos imprevisíveis (picos de emergência) geram erro e o modelo só vale para o padrão de atendimento já registrado. |
| 3 Comércio | Ausência de alvo: não há categorias prévias de clientes. | Grupos (perfis descobertos). |Aprendizado não supervisionado, agrupamento (clustering). Busca-se estrutura nos dados, não uma resposta correta conhecida.  | Dados: histórico de compras (frequência, valor, categorias de produtos). Limitação: os grupos precisam ser interpretados por pessoas e o resultado depende de escolhas como o número de grupos e a escala dos atributos. |
| 5 Segurança digital | Alvo: spam ou legítima (mensagens já revisadas). | Categoria (duas classes). | Aprendizado supervisionado, classificação. Há rótulos fornecidos pela revisão das mensagens. | Dados: texto das mensagens, remetente, links, com o rótulo da revisão. Limitação: spammers mudam de estratégia (os dados envelhecem) e falsos positivos podem bloquear mensagens importantes. |
| 7 Educação | Ausência de alvo: não há rótulo de evasão. | Grupos (perfis de acesso). | Aprendizado não supervisionado, agrupamento. O objetivo é descobrir perfis de uso, sem um desfecho a prever. | Dados: registros de acesso ao ambiente virtual (frequência, horários, tempo de uso, materiais acessados). Limitação: os grupos não indicam causa nem prevêem evasão por si só, e exigem interpretação pedagógica. |

## 4. Raciocínio crítico

“Detectar fraude” define sozinho o tipo de aprendizado? Compare o uso de exemplos rotulados e a busca de operações atípicas sem rótulos. Não. “Detectar fraude” é só o objetivo. O tipo de aprendizado depende de quais dados a gente tem. A detecção de fraudes pode usar aprendizado supervisionado, quando existem exemplos de operações fraudulentas e normais, ou aprendizado não supervisionado, quando o modelo identifica operações fora do padrão. O supervisionado reconhece fraudes parecidas com as anteriores, enquanto o não supervisionado pode encontrar situações novas, mas também gerar alertas falsos. Por isso, as duas formas podem ser usadas juntas para melhorar a detecção de fraudes.

## Entrega

Salve este arquivo preenchido. Critérios: distinção conceitual, pertinência dos dados, justificativa e clareza. [Voltar ao início](README.md).
