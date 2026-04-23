# Manual Operacional da AVANT

## Objetivo

Este manual organiza a operacao da AVANT, agencia digital, usando as skills ja instaladas no ambiente. A ideia e padronizar descoberta, estrategia, criacao, execucao, analise e entrega.

## Stack Principal

### Estrategia

- `orchestrator`: coordena fluxos com varias skills
- `business-analyst`: discovery, briefing e entendimento do cliente
- `research`: pesquisa de mercado, concorrencia e conteudo
- `marketing-ideas`: ideias de canais, campanhas e crescimento
- `brand-voice`: definicao de voz e tom de marca

### Copy e Conteudo

- `copywriter`: copy de conversao
- `content-creation`: pecas por canal
- `content-research-writer`: pesquisa para conteudo aprofundado
- `hook`: aberturas e ganchos
- `script-writer`: roteiros
- `social-media-generator`: posts por plataforma
- `youtube-content`: transforma videos em ativos reaproveitaveis

### Design e Criacao

- `web-design-expert`: direcao visual e branding web
- `typography-expert`: tipografia
- `design-system-creator`: sistema visual
- `icon-set-generator`: icones customizados
- `imagegen` e `ai-image-generator`: imagens de campanha
- `meme-generation`: memes e criativos rapidos
- `storyboard-creation`: storyboard para video
- `visual-content`: carrosseis, apresentacoes e materiais visuais

### Video, Audio e Social

- `sora`: video com IA
- `text-to-speech`: locucao
- `voice-audio-engineer`: refinamento de voz e audio
- `instagram-automation`: operacao Instagram
- `projeto-hive`: criacao e agenda de posts

### Operacao e Entrega

- `google-workspace`: Docs, Sheets, Drive, Gmail e Calendar
- `powerpoint`: decks e apresentacoes
- `spreadsheet`: planilhas operacionais e relatorios
- `doc`: documentos editaveis
- `pdf`: PDFs finais
- `ocr-and-documents`: extracao de conteudo de arquivos

### Inteligencia e Monitoramento

- `business-intelligence`: KPIs, dashboards e narrativas executivas
- `blogwatcher`: monitoramento de fontes e blogs
- `duckduckgo-search`: pesquisa web complementar
- `scrapling`: coleta estruturada de paginas
- `playwright`: verificacao visual e automacao no navegador

## Modelo Operacional

### 1. Onboarding do Cliente

Objetivo: transformar pedido solto em direcionamento claro.

Fluxo:

1. Use `business-analyst` para captar negocio, publico, oferta, objecoes e meta.
2. Use `research` para mapear concorrentes, referenciais e oportunidades.
3. Use `brand-voice` para definir voz, tom, proibicoes e exemplos.
4. Use `orchestrator` para consolidar a linha de trabalho.

Entregaveis:

- briefing mestre
- mapa de publico
- analise competitiva
- diretriz de marca e voz
- plano inicial de canais

Prompt base:

```text
Use business-analyst + research + brand-voice para montar o onboarding estrategico deste cliente.
Entregue:
- resumo do negocio
- ICP e dores
- concorrentes
- oportunidades de posicionamento
- voz da marca
- prioridades de canais para os proximos 90 dias
```

### 2. Planejamento de Campanha

Objetivo: sair de "precisamos divulgar" para um plano acionavel.

Fluxo:

1. Use `marketing-ideas` para gerar 3 a 5 abordagens viaveis.
2. Use `copywriter` para lapidar promessa e CTA principal.
3. Use `web-design-expert` para definir direcao visual.
4. Use `content-creation` para organizar pecas por canal.

Entregaveis:

- conceito de campanha
- promessa principal
- CTA
- calendario de pecas
- direcao criativa

Prompt base:

```text
Use marketing-ideas + copywriter + web-design-expert + content-creation.
Monte uma campanha para [produto/servico] com:
- grande ideia
- angulos de mensagem
- canais
- pecas necessarias
- CTA principal
- direcao visual
```

### 3. Landing Page e Paginas Comerciais

Objetivo: criar paginas que convertam.

Fluxo:

1. Use `copywriter` para headline, subheadline, secoes e CTA.
2. Use `web-design-expert` para hierarquia, layout e visual.
3. Use `frontend-skill` se a pagina precisar ser implementada.
4. Use `playwright` para validacao visual e smoke test.

Checklist:

- headline clara
- prova social
- objecoes respondidas
- CTA repetido
- visual consistente com a marca
- mobile aceitavel

Prompt base:

```text
Use copywriter + web-design-expert.
Crie a estrutura de uma landing page de alta conversao para [oferta].
Entregue:
- hero
- beneficios
- prova social
- FAQ
- CTA
- direcao visual da pagina
```

### 4. Conteudo Organico

Objetivo: transformar estrategia em conteudo recorrente.

Fluxo:

1. Use `research` para mapear topicos.
2. Use `hook` para aberturas.
3. Use `content-creation` para blog, newsletter, post e legenda.
4. Use `social-media-generator` para adaptar por canal.
5. Use `brand-voice` para manter consistencia.

Entregaveis:

- calendario editorial
- pecas por canal
- variacoes de hook
- CTA por peca

Prompt base:

```text
Use research + hook + content-creation + social-media-generator.
Monte um plano de conteudo para 30 dias sobre [tema].
Quero:
- pilares editoriais
- 12 ideias de conteudo
- formato ideal por canal
- hook de abertura
- CTA sugerido
```

### 5. Reaproveitamento de Conteudo

Objetivo: extrair o maximo de uma peca central.

Fluxo:

1. Use `youtube-content` para extrair transcript, resumo, capitulos e quotes.
2. Use `content-creation` para blog, email e post.
3. Use `social-media-generator` para cortes por plataforma.
4. Use `script-writer` para novos derivados em video.

Entregaveis:

- resumo
- thread
- blog post
- carrossel
- shorts/reels ideas
- email/newsletter

Prompt base:

```text
Use youtube-content + content-creation + social-media-generator.
Pegue este video e transforme em:
- resumo executivo
- artigo
- thread
- carrossel
- 5 cortes curtos com gancho
URL: [cole aqui]
```

### 6. Criativos e Pecas Visuais

Objetivo: produzir ativos com coerencia visual.

Fluxo:

1. Use `web-design-expert` para direcionamento visual.
2. Use `imagegen` ou `ai-image-generator` para imagens.
3. Use `meme-generation` para pecas rapidas de engajamento.
4. Use `visual-content` para apresentacoes e carrosseis.

Entregaveis:

- key visual
- variacoes de criativo
- carrosseis
- memes
- imagens para ads ou posts

Prompt base:

```text
Use web-design-expert + imagegen.
Crie a direcao criativa e os prompts visuais para uma campanha de [produto].
Quero:
- conceito visual
- paleta
- tipografia
- 3 linhas de criativos
- prompts prontos para gerar imagens
```

### 7. Video e Audio

Objetivo: ampliar alcance com formatos audiovisuais.

Fluxo:

1. Use `script-writer` para roteiro.
2. Use `storyboard-creation` para cenas.
3. Use `sora` para video.
4. Use `text-to-speech` e `voice-audio-engineer` para voz e finalizacao.

Entregaveis:

- roteiro
- storyboard
- video-base
- narracao
- adaptacoes por formato

Prompt base:

```text
Use script-writer + storyboard-creation + sora.
Crie um video promocional para [oferta].
Entregue:
- roteiro
- estrutura de cenas
- sugestao de narracao
- prompt para geracao do video
```

### 8. Social Media Operacional

Objetivo: manter cadencia e execucao.

Fluxo:

1. Use `social-media-generator` para textos.
2. Use `projeto-hive` para montar posts com imagem e legenda.
3. Use `instagram-automation` quando a operacao exigir automacao.

Entregaveis:

- legenda
- criativo
- hashtags
- agenda de postagem

Prompt base:

```text
Use social-media-generator + projeto-hive.
Crie 7 posts para Instagram sobre [tema], com:
- legenda
- conceito visual
- CTA
- ideia de imagem
- ordem ideal de publicacao
```

### 9. Propostas, Relatorios e Apresentacoes

Objetivo: entregar material comercial e executivo de alta qualidade.

Fluxo:

1. Use `powerpoint` para pitch, proposta e relatorio.
2. Use `spreadsheet` para indicadores e tabelas.
3. Use `business-intelligence` para narrativa de KPI.
4. Use `pdf` para versao final de envio.

Entregaveis:

- proposta comercial
- deck de estrategia
- relatorio mensal
- apresentacao executiva

Prompt base:

```text
Use business-intelligence + powerpoint.
Monte um relatorio executivo mensal com:
- resumo do periodo
- KPIs principais
- leitura dos resultados
- recomendacoes
- proximos passos
```

### 10. Monitoramento Continuo

Objetivo: gerar insights e oportunidades sem depender so da intuicao.

Fluxo:

1. Use `blogwatcher` para acompanhar fontes fixas.
2. Use `duckduckgo-search` para pesquisa pontual.
3. Use `scrapling` para extrair paginas estruturadas.
4. Use `business-intelligence` para transformar dados em decisao.

Entregaveis:

- radar de tendencias
- monitoramento de concorrentes
- clippings
- oportunidades de pauta e campanha

Prompt base:

```text
Use blogwatcher + duckduckgo-search + research.
Monte um radar semanal de mercado para [nicho].
Quero:
- novidades relevantes
- movimentos de concorrentes
- tendencias de conteudo
- oportunidades para a marca agir
```

## SOPs por Servico

### Branding

Entrada:

- briefing
- referencias
- concorrentes

Saida:

- voz da marca
- posicionamento
- direcao visual

Skills:

- `business-analyst`
- `research`
- `brand-voice`
- `web-design-expert`

### Social Media

Entrada:

- objetivo do mes
- ofertas
- datas importantes

Saida:

- calendario
- copys
- criativos
- agenda

Skills:

- `content-creation`
- `social-media-generator`
- `projeto-hive`
- `imagegen`

### Conteudo Longo

Entrada:

- tema
- canal
- palavra-chave

Saida:

- outline
- rascunho
- CTA
- derivados

Skills:

- `research`
- `content-research-writer`
- `content-creation`
- `hook`

### Trafego e Performance

Entrada:

- oferta
- publico
- budget

Saida:

- angulos
- copys
- criativos
- leitura de resultados

Skills:

- `marketing-ideas`
- `copywriter`
- `imagegen`
- `business-intelligence`

### Comercial

Entrada:

- contexto do lead
- proposta de valor
- escopo

Saida:

- proposta
- deck
- follow-up

Skills:

- `copywriter`
- `good-prose`
- `powerpoint`
- `pdf`

## Prompts Mestres

### Prompt Mestre de Discovery

```text
Use business-analyst + research.
Quero um discovery completo para este cliente.
Organize em:
- negocio
- publico
- dores
- concorrentes
- diferenciais
- oportunidades de marketing
```

### Prompt Mestre de Campanha

```text
Use orchestrator para coordenar marketing-ideas, copywriter, web-design-expert e content-creation.
Crie uma campanha completa para [produto].
Entregue:
- conceito
- mensagem principal
- canais
- pecas
- CTA
- cronograma sugerido
```

### Prompt Mestre de Conteudo

```text
Use research + hook + content-creation + brand-voice.
Crie conteudo para [canal] sobre [tema].
Quero:
- angulos
- hooks
- estrutura
- CTA
- ajuste ao tom da marca
```

### Prompt Mestre de Relatorio

```text
Use business-intelligence + good-prose.
Transforme estes numeros em um relatorio claro para o cliente.
Inclua:
- o que aconteceu
- por que aconteceu
- impacto no negocio
- o que fazer a seguir
```

## Prioridade de Uso

Quando houver duvida sobre qual skill usar:

1. Comece por `orchestrator` em tarefas amplas.
2. Use `research` antes de criar quando o contexto estiver fraco.
3. Use `brand-voice` antes de produzir volume de conteudo.
4. Use `copywriter` para conversao e `content-creation` para adaptacao por canal.
5. Use `business-intelligence` sempre que houver numeros ou leitura de desempenho.

## Proximos Passos Recomendados

1. Criar um briefing padrao da agencia em `.md`.
2. Criar um template de proposta comercial.
3. Criar um template de relatorio mensal.
4. Configurar as skills que exigem setup, como `google-workspace` e `blogwatcher`.
5. Definir quais servicos a agencia vai vender primeiro.
