# AVANT Launch Landing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Atualizar a landing da AVANT para o lançamento baseado no Prêmio Virtus, mantendo o fluxo de leads existente e deixando a operação pronta para deploy no domínio conectado ao Cloudflare Pages.

**Architecture:** A implementação reaproveita a estrutura atual de páginas estáticas (`avant/`, `avant/obrigado/`, `avant/orbita/`) e o backend já existente de captura de leads. O trabalho se concentra em reposicionar a mensagem, ajustar o fluxo de conversão para o `Raio X de Presença Digital`, revisar a página de obrigado, validar o painel de leads e documentar o processo de deploy sem afetar os outros sites do mesmo projeto.

**Tech Stack:** HTML estático, Tailwind via CDN, JavaScript vanilla no frontend, rotas `/api/avant-leads` e `/api/avant-leads-export`, Cloudflare Pages/Workers, D1.

---

### Task 1: Mapear o subprojeto AVANT e congelar escopo

**Files:**
- Modify: `/Users/victorpimentel/Documents/AVANT/docs/superpowers/specs/2026-04-21-avant-launch-strategy-design.md`
- Create: `/Users/victorpimentel/Documents/AVANT/docs/superpowers/plans/2026-04-21-avant-launch-landing.md`
- Inspect: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/index.html`
- Inspect: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/obrigado/index.html`
- Inspect: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/orbita/index.html`

- [ ] **Step 1: Confirmar que a implementacao vai mexer apenas na experiencia da AVANT**

Verificar que os arquivos abaixo existem e sao os unicos a mudar neste subprojeto:

```text
/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/index.html
/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/obrigado/index.html
/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/orbita/index.html
```

- [ ] **Step 2: Registrar no plano os objetivos de conversao da landing**

Confirmar no plano que a pagina deve:

```text
1. Posicionar a AVANT como agencia nascida da execucao do Premio Virtus
2. Vender o Raio X de Presenca Digital como porta de entrada
3. Levar para reuniao consultiva, nao para uma venda generica
4. Manter o fluxo de captura, dashboard e exportacao funcionando
```

- [ ] **Step 3: Revisar o escopo e travar o que nao entra agora**

Registrar que esta fase nao inclui:

```text
- reescrever APIs
- mudar schema do D1 sem necessidade
- refatorar outros sites do projeto
- adicionar email transactional neste momento
```

### Task 2: Reescrever a homepage da AVANT para o lancamento

**Files:**
- Modify: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/index.html`
- Reference: `/Users/victorpimentel/Documents/AVANT/COPY-LANDING-LANCAMENTO-AVANT.md`
- Reference: `/Users/victorpimentel/Documents/AVANT/OFERTA-DE-ENTRADA-AVANT.md`

- [ ] **Step 1: Fazer backup local do HTML atual**

Run:

```bash
cp '/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/index.html' \
   '/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/index.pre-launch-backup.html'
```

Expected: arquivo `index.pre-launch-backup.html` criado no mesmo diretorio.

- [ ] **Step 2: Atualizar o `<title>` e a `<meta description>`**

Substituir os textos atuais por:

```html
<title>AVANT | Raio X de Presença Digital para empresas do Prêmio Virtus</title>
<meta
  name="description"
  content="A agência por trás do marketing do Prêmio Virtus agora abre uma rodada de Raio X de Presença Digital com reunião consultiva para empresas da região."
/>
```

- [ ] **Step 3: Reescrever o hero com a nova mensagem**

Trocar headline, subtitulo e CTA principal para refletir:

```html
<h1 class="font-display mt-6 max-w-3xl text-5xl font-bold leading-[0.94] md:text-7xl">
  A agência por trás do marketing do
  <span style="color:#6ff4e4;">Prêmio Virtus</span>
  agora abre uma rodada de diagnóstico para empresas da região.
</h1>
<p class="mt-6 max-w-2xl text-lg leading-relaxed text-white/86 md:text-xl">
  Receba um Raio X da sua Presença Digital e descubra, com clareza, os pontos fortes, os gargalos e as oportunidades da sua marca no digital.
</p>
```

- [ ] **Step 4: Substituir a lógica de “oferta especial” pela lógica de “Raio X + reunião consultiva”**

Trocar os rótulos institucionais do bloco de captura para:

```html
<span class="text-xs font-bold uppercase tracking-[0.28em]" style="color:#dffdfa;">
  Rodada inicial de diagnóstico
</span>
```

e

```html
<h2 class="font-display text-4xl font-bold leading-none md:text-5xl">
  Quero receber meu
  <span style="color:#6ff4e4;">Raio X digital.</span>
</h2>
<p class="mt-4 text-base leading-relaxed text-white/76">
  Preencha em menos de 1 minuto. A AVANT vai priorizar empresas com contexto claro e maior potencial para a reunião consultiva.
</p>
```

- [ ] **Step 5: Adicionar seções explicando prova, dor e entrega**

Inserir abaixo do hero ao menos tres blocos com:

```text
- prova: AVANT nasceu da execucao do Premio Virtus
- dor: muitas empresas boas comunicam abaixo do que constroem
- entrega: o que entra no Raio X de Presenca Digital
```

Os blocos devem usar a paleta ja existente e manter a linguagem da AVANT.

- [ ] **Step 6: Ajustar o botao final do formulario**

Trocar:

```html
Receber minha oferta especial
```

por:

```html
Receber meu Raio X
```

### Task 3: Ajustar o formulario para refletir a nova oferta sem quebrar a API

**Files:**
- Modify: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/index.html`
- Inspect: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant-leads.js`

- [ ] **Step 1: Manter os campos atuais compativeis com o backend**

Nao renomear estes `name` attributes:

```html
fullName
companyName
phone
email
instagram
painPoints
```

- [ ] **Step 2: Ajustar o texto de ajuda do bloco de dor**

Substituir o helper atual por:

```html
<p class="text-sm leading-relaxed text-white/72">
  Selecione a opção que melhor representa a principal dificuldade da sua empresa hoje no digital.
</p>
```

- [ ] **Step 3: Ajustar a mensagem de erro de selecao**

Trocar:

```javascript
"Selecione a maior dor no marketing para continuar."
```

por:

```javascript
"Selecione a principal dor da empresa no marketing para continuar."
```

- [ ] **Step 4: Ajustar o estado de envio para a nova oferta**

Trocar o texto temporario do botao para:

```javascript
"Enviando diagnóstico..."
```

### Task 4: Reescrever a pagina de obrigado para aquecer a reuniao

**Files:**
- Modify: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/obrigado/index.html`

- [ ] **Step 1: Atualizar o titulo da pagina**

Substituir por:

```html
<title>AVANT | Pedido de Raio X confirmado</title>
```

- [ ] **Step 2: Reescrever headline e textos**

Substituir a mensagem atual por uma versao que reforce:

```text
- o Raio X foi solicitado
- a empresa entrou na rodada inicial
- a proxima etapa e a reuniao consultiva
```

Texto sugerido:

```html
<p class="mt-8 text-xs font-bold uppercase tracking-[0.28em]" style="color:#6ff4e4;">Pedido confirmado</p>
<h1 class="font-display mt-5 text-5xl font-bold leading-[0.94] md:text-7xl">
  Seu Raio X de
  <span style="color:#6ff4e4;">Presença Digital</span>
  entrou na rodada inicial.
</h1>
<p class="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-white/82 md:text-xl">
  A AVANT vai analisar os principais sinais da presença digital da sua empresa e, se o perfil estiver dentro desta rodada, o próximo passo será uma reunião consultiva curta para apresentar os pontos mais importantes.
</p>
<p class="mx-auto mt-4 max-w-2xl text-base leading-relaxed text-white/64">
  Não é uma resposta automática comum. É o início de uma leitura estratégica sobre como sua empresa está sendo percebida no digital.
</p>
```

### Task 5: Validar painel e exportacao sem alterar o contrato atual

**Files:**
- Inspect: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/orbita/index.html`
- Inspect: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant-leads.js`
- Inspect: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant-leads-export.js`

- [ ] **Step 1: Ler os handlers antes de mudar qualquer contrato**

Verificar no codigo do backend que o frontend continua enviando:

```json
{
  "fullName": "...",
  "companyName": "...",
  "phone": "...",
  "email": "...",
  "instagram": "...",
  "painPoints": ["..."]
}
```

- [ ] **Step 2: Confirmar que o painel oculto continua funcional**

Garantir que o painel `avant/orbita/index.html` nao dependa de textos antigos da “oferta especial” e pode permanecer estruturalmente igual se o contrato de dados estiver preservado.

- [ ] **Step 3: Validar a exportacao CSV**

Checar que `avant-leads-export.js` continua lendo o mesmo schema antes de qualquer deploy.

### Task 6: Preparar deploy seguro no projeto compartilhado

**Files:**
- Inspect: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/`
- Create: `/Users/victorpimentel/Documents/AVANT/CHECKLIST-DEPLOY-AVANT.md`

- [ ] **Step 1: Documentar exatamente quais arquivos da AVANT mudaram**

Criar checklist com:

```text
- avant/index.html
- avant/obrigado/index.html
- qualquer asset novo adicionado apenas para AVANT
```

- [ ] **Step 2: Registrar que o projeto tem outros sites e o deploy deve isolar o escopo**

Anotar no checklist:

```text
Nao refatorar estrutura global do projeto
Nao mover arquivos de outros sites
Nao quebrar rotas existentes de Virtus e outros materiais
```

- [ ] **Step 3: Documentar pre-deploy manual**

Incluir estes passos no checklist:

```text
1. Abrir localmente a landing
2. Testar envio do formulario
3. Verificar redirect para /avant/obrigado
4. Abrir /avant/orbita
5. Validar exportacao CSV
```

### Task 7: Verificacao final da experiencia de lancamento

**Files:**
- Test: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/index.html`
- Test: `/Users/victorpimentel/Documents/Site Virtus Educa/Site Pronto/avant/obrigado/index.html`

- [ ] **Step 1: Revisar a pagina contra a estrategia aprovada**

Confirmar que a landing responde positivamente a estas perguntas:

```text
- Fica claro que a AVANT nasceu da execucao do Premio Virtus?
- Fica claro que a oferta e o Raio X de Presenca Digital?
- Fica claro que o proximo passo e uma reuniao consultiva?
- A pagina evita parecer uma agencia generica?
```

- [ ] **Step 2: Validar copy e atrito**

Revisar se:

```text
- a headline esta clara
- o formulario continua curto
- o CTA esta alinhado com diagnostico
- a pagina de obrigado aquece o lead
```

- [ ] **Step 3: Registrar pronta para implementacao**

Ao final, marcar no plano que o subprojeto esta pronto para execucao no codigo e depois para deploy controlado no Cloudflare Pages.

