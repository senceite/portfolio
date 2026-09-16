# Site do portfólio — Rafaela Senceite

HTML estático com Tailwind. Sem framework, sem runtime: o que vai pro ar é o conteúdo
desta pasta menos `src/`, `node_modules/` e os dois scripts.

## Rodar

```bash
npm install          # uma vez
npm run build        # gera as páginas e o CSS
```

Para ver, abra `index.html` no navegador ou sirva a pasta:

```bash
python -m http.server 8080
```

`npm run watch` recompila só o CSS enquanto você mexe nas classes.

## Onde fica o quê

| Caminho | O que é |
| --- | --- |
| `build.py` | Conteúdo dos seis cases e gerador das páginas. É aqui que se edita texto. |
| `src/tailwind.css` | Tokens de cor, tipografia e as classes próprias (`.wrap`, `.label`, `.prose-p`). |
| `assets/img/<case>/` | Imagens em WebP, uma versão de 1600px e outra de 800px. |
| `index.html`, `cases/*.html` | Gerados. Não edite à mão: o próximo build sobrescreve. |

## Estado

`DRAFT = True` no topo do `build.py` liga a tarja de rascunho e o `noindex`. Vire para
`False` quando o texto estiver aprovado e o contato preenchido.

Falta preencher `SITE["phone"]`, `SITE["email"]` e `SITE["whatsapp"]`, hoje com marcador
ou vazios. A tarja de rascunho lista sozinha o que ainda está faltando.

O WhatsApp vai em `SITE["whatsapp"]` só com dígitos e código do país, por exemplo
`5521999998888`. Enquanto estiver vazio, o botão "Agende uma conversa" sai desabilitado
em vez de virar um `wa.me` quebrado. A mensagem que já vem digitada para quem clica está
em `SITE["whatsapp_message"]`. Os créditos de
Reconhecer e Reparar e de Nem 1 Pra Trás dependem das respostas da seção 9 do documento
compartilhado; até lá esses dois cases saem sem bloco de créditos.

## Decisões que valem manter

Lato é a única família, por exigência da Rafaela.

O site tem duas escalas de cor. A home e o chrome — cabeçalho e rodapé de todas as
páginas — usam a paleta do currículo dela. As páginas de case ficam neutras, para que o
vermelho do Múltiplo, o ciano do Nem 1 Pra Trás e o amarelo do Budapeste apareçam sem
disputar com o roxo. Isso atende ao "pode mudar tudo, exceto a tipografia" sem furar o
"que evidencie e privilegie os projetos" da seção 5 do documento.

A paleta foi amostrada do PDF do currículo, não escolhida de olho:

| Papel | Token | Hex | Contraste sobre o roxo |
| --- | --- | --- | --- |
| Fundo | `--color-deep` | `#312254` | — |
| Títulos | `--color-yellow` | `#E9C615` | 8,44:1 |
| Cargos e rótulos | `--color-aqua` | `#66CBBC` | 7,28:1 |
| Corpo | `--color-lavender` | `#C5BBE0` | 7,77:1 |
| Gradiente | `--color-magenta` | `#EB0F89` | 3,34:1 |
| Gradiente | `--color-plum` | `#B5309B` | — |

A lavanda do PDF é `#9788BA` e dá 4,40:1, abaixo do mínimo, então subiu para `#C5BBE0`
mantendo o tom. O magenta fica em 3,34:1 e por isso só aparece em gradiente e em réguas,
nunca em texto.

Dentro de `.on-brand` o HTML usa `text-lavender` e `border-white/15` diretamente. Não
adianta redefinir `.text-muted` ou `.border-line` dentro de `.on-brand`: no Tailwind v4 a
camada `utilities` vence a camada `components` por camada, não por especificidade.

Cada projeto ainda entra com a própria cor nas páginas de case, na tarja do topo, nos
marcadores de lista e no fundo da capa. A capa fica contida sobre essa tarja em vez de
recortada num formato fixo, porque as capas variam entre retrato e paisagem.

O texto de case nunca usa a cor do projeto: ela aparece só em faixas e marcadores, que
não precisam passar no limite de 4,5:1.

## Cabeçalho

Na home o cabeçalho começa fora da tela e entra quando o hero sai de vista. Ele é
`fixed` ali, não `sticky`: escondido, um `sticky` continuaria reservando a própria
altura e abriria um vão de 80px no topo do hero.

Quem esconde é o script no fim de `index.html`. Sem JS ele nunca ganha `.is-hidden` e
continua visível, que é o estado seguro. No estado escondido usa `visibility: hidden`,
senão os links seguiriam no tab order e o foco iria parar num cabeçalho invisível.

Nas páginas de case o cabeçalho é `sticky` e fica sempre visível.

## Trocar imagens

`tools/build-assets.py` gera os WebP a partir da pasta da Rafaela no Drive: ele lê a
seleção de arquivos por case e salva as duas larguras. Para uma troca pontual, basta
exportar `<nome>.webp` com 1600px de largura e `<nome>@sm.webp` com 800px dentro de
`assets/img/<case>/` e citar o nome na lista `images` do case em `build.py`.
