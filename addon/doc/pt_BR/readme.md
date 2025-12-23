# Vision Assistant Pro

**Vision Assistant Pro** é um assistente de IA avançado e multimodal para NVDA. Ele utiliza os modelos Gemini do Google para fornecer capacidades inteligentes de leitura de tela, tradução, ditado por voz e análise de documentos.

_Este add-on foi lançado para a comunidade em homenagem ao Dia Internacional da Pessoa com Deficiência._

## 1. Configuração

Vá para **Menu NVDA > Preferências > Configurações > Vision Assistant Pro**.

- **Chave de API:** Obrigatória. O campo está oculto por padrão por segurança (use "Mostrar Chave de API" para visualizar). Obtenha uma chave gratuita em [Google AI Studio](https://aistudio.google.com/).
- **Modelo:** Escolha os modelos mais recentes do Gemini Flash.
- **Idiomas:** Defina os idiomas de Origem, Destino e Resposta da IA.
- **Troca Inteligente:** Troca automaticamente os idiomas se o texto de origem corresponder ao idioma de destino.
- **Saída Direta:** Ignora a janela de chat e anuncia a resposta diretamente por voz.
- **Integração com Área de Transferência:** Copia automaticamente a resposta da IA para a área de transferência.

## 2. Camada de Comandos & Atalhos

Para evitar conflitos de teclado, este add-on usa uma **Camada de Comandos**.  

1. Pressione **NVDA + Shift + V** (Tecla Mestre) para ativar a camada (você ouvirá um beep).  
2. Solte as teclas e pressione uma das seguintes teclas únicas:

| Tecla | Função | Descrição |
| ------- | -------- | ----------- |
| **T** | Tradutor Inteligente | Traduz o texto sob o cursor do NVDA ou seleção. |
| **Shift + T** | Tradutor da Área de Transferência | Traduz o conteúdo atualmente na área de transferência. |
| **R** | Refinador de Texto | Resume, Corrige Gramática, Explica ou executa **Comandos Personalizados**. |
| **V** | Visão de Objetos | Descreve o objeto atual do NVDA. |
| **O** | Visão de Tela Cheia | Analisa todo o layout e conteúdo da tela. |
| **Shift + V** | Análise de Vídeo Online | Analisa vídeos do **YouTube** ou **Instagram** via URL. |
| **D** | Análise de Documento | Conversa com arquivos PDF/TXT/MD/PY. |
| **F** | OCR de Arquivo | OCR direto de arquivos de imagem/PDF/TIFF (suporte a TIFF multi-página). |
| **A** | Transcrição de Áudio | Transcreve arquivos MP3/WAV/OGG. |
| **C** | Resolução de CAPTCHA | Captura e resolve CAPTCHA automaticamente. |
| **S** | Ditado Inteligente | Converte fala em texto. Pressione para iniciar a gravação e novamente para parar/digitar. |
| **L** | Relatório de Status | Anuncia o status atual (ex.: "Enviando...", "Ocioso"). |
| **U** | Verificar Atualizações | Verifica no GitHub a versão mais recente. |

## 3. Comandos Personalizados & Variáveis

Crie comandos em Configurações: `Nome:Texto do Prompt` (separados por `|` ou novas linhas).

### Variáveis Disponíveis

| Variável | Descrição | Tipo de Entrada |
| ---------- | ----------- | ----------------- |
| `[selection]` | Texto atualmente selecionado | Texto |
| `[clipboard]` | Conteúdo da área de transferência | Texto |
| `[screen_obj]` | Captura do objeto do NVDA | Imagem |
| `[screen_full]` | Captura de tela completa | Imagem |
| `[file_ocr]` | Seleciona imagem/PDF/TIFF (padrão: "Extrair texto") | Imagem, PDF, TIFF |
| `[file_read]` | Seleciona documento de texto | TXT, Código, PDF |
| `[file_audio]` | Seleciona arquivo de áudio | MP3, WAV, OGG |

### Exemplos de Comandos Personalizados

- **OCR Rápido:** `Meu OCR:[file_ocr]`  
- **Traduzir Imagem:** `Traduzir Img:Extrair texto desta imagem e traduzir para Persa. [file_ocr]`  
- **Analisar Áudio:** `Resumir Áudio:Ouça esta gravação e resuma os pontos principais. [file_audio]`  
- **Depurador de Código:** `Depurar:Encontre erros neste código e explique-os: [selection]`  

**Observação:** É necessária conexão ativa com a internet para todas as funções de IA. TIFFs multi-página são processados automaticamente.

## Alterações para 3.5.0

- **Camada de Comandos:** Introduzido sistema de Camada de Comandos (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestre. Por exemplo, em vez de pressionar `NVDA+Control+Shift+T` para tradução, agora você pressiona `NVDA+Shift+V` seguido de `T`.  
- **Análise de Vídeo Online:** Adicionada funcionalidade para analisar vídeos do YouTube e Instagram diretamente via URL.

## Alterações para 3.1.0

- **Modo de Saída Direta:** Adicionada opção para pular o diálogo de chat e ouvir respostas da IA diretamente, para experiência mais rápida.  
- **Integração com Área de Transferência:** Adicionada configuração para copiar automaticamente respostas da IA para a área de transferência.

## Alterações para 3.0

- **Novos Idiomas:** Adicionado suporte a **Persa** e **Vietnamita**.  
- **Modelos de IA Expandidos:** Lista de seleção de modelos reorganizada com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) e suporte para **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.  
- **Estabilidade do Ditado:** Melhorias significativas no Ditado Inteligente. Checagem de segurança para ignorar áudios menores que 1 segundo.  
- **Manipulação de Arquivos:** Corrigido problema ao enviar arquivos com nomes não ingleses.  
- **Otimização de Prompts:** Melhorada lógica de Tradução e estrutura dos resultados de Visão.

## Alterações para 2.9

- Traduções em Francês e Turco adicionadas.  
- Botão "Ver Formatado" em diálogos de chat adicionado para visualização com estilo.  
- Configuração "Limpar Markdown no Chat" adicionada.  
- Correções em múltiplas janelas de diálogo e melhoria na UX.

## Alterações para 2.8

- Tradução em Italiano adicionada.  
- **Relatório de Status:** Novo comando (NVDA+Control+Shift+I).  
- Exportação HTML aprimorada.  
- Melhorias na UI de Configurações e suporte a novos modelos e idiomas.  
- Correções em comandos de Refinar Texto e Ditado.

## Alterações para 2.7

- Estrutura do projeto migrada para o Template oficial da NV Access.  
- Implementada lógica de repetição automática para erros HTTP 429.  
- Otimização dos prompts de tradução e lógica de "Smart Swap".  
- Tradução Russa atualizada.

## Alterações para 2.6

- Suporte à tradução Russa adicionado.  
- Mensagens de erro atualizadas para melhor feedback.  
- Idioma padrão de destino alterado para Inglês.

## Alterações para 2.5

- Comando de OCR nativo adicionado (NVDA+Control+Shift+F).  
- Botão "Salvar Chat" adicionado.  
- Suporte completo à localização (i18n).  
- Feedback de áudio migrado para tons nativos do NVDA.  
- Uso da API Gemini File para PDF e áudio.  
- Corrigido crash ao traduzir textos com chaves.

## Alterações para 2.1.1

- Corrigido problema com variável [file_ocr] em Comandos Personalizados.

## Alterações para 2.1

- Padronização de atalhos para NVDA+Control+Shift.

## Alterações para 2.0

- Sistema de Atualização Automática implementado.  
- Cache de Tradução Inteligente adicionado.  
- Memória de Conversa adicionada para refinar resultados.  
- Comando de Tradução Direta da Área de Transferência adicionado.  
- Prompts de IA otimizados para respeitar idioma de saída.  
- Corrigido crash com caracteres especiais.

## Alterações para 1.5

- Suporte a mais de 20 idiomas novos.  
- Diálogo Interativo de Refinamento implementado.  
- Ditado Inteligente nativo adicionado.  
- Categoria "Vision Assistant" no diálogo de Gestos de Entrada do NVDA.  
- Corrigidos crashes COMError no Firefox e Word.  
- Mecanismo de repetição automática para erros de servidor adicionado.

## Alterações para 1.0

- Lançamento inicial.
