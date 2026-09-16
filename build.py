"""Generate the static portfolio site.

Run:  python build.py
Then: npx @tailwindcss/cli -i src/tailwind.css -o assets/css/site.css --minify

Content lives in CASES below. Images come from assets/img/<slug>/, produced by the
asset script; every image needs a <name>.webp and a <name>@sm.webp.
"""
from __future__ import annotations

import html
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
DRAFT = False  # tarja de rascunho e noindex; Kaz liberou em 2026-09-16

SITE = {
    "name": "Rafaela Senceite",
    "role": "Designer gráfica e diretora de arte",
    "lede": "Sete anos de trabalho em identidade visual, design editorial e comunicação institucional, "
            "entre projetos de marca para clientes e campanhas da Fundação Roberto Marinho.",
    "phone": "+55 21 99383-6881",
    "email": "senceite@gmail.com",
    # Só dígitos, com código do país: "5521999998888". Enquanto ficar vazio, o botão
    # "Agende uma conversa" sai desabilitado em vez de virar link quebrado.
    "whatsapp": "5521993836881",
    "whatsapp_message": "Oi, Rafaela! Vi seu portfólio e queria conversar sobre um projeto.",
    "availability": "Disponível para trabalhar em identidade visual, design editorial e "
                    "comunicação institucional. Rio de Janeiro, Niterói, São Paulo e Belo "
                    "Horizonte, presencial, híbrido ou remoto.",
}


HEADER_REVEAL = """<script>
// O cabeçalho da home só entra depois que o hero sai de vista. Sem JS ele nunca
// ganha .is-hidden, então continua visível — a degradação é o estado seguro.
(function () {
  var header = document.querySelector('.site-header');
  var marca = document.getElementById('fim-do-hero');
  if (!header || !marca) return;
  // Mede o fim do hero uma vez. Durante o scroll só compara com scrollY, que não
  // força reflow, em vez de chamar getBoundingClientRect a cada evento.
  var limite = 0;
  function aplica() {
    header.classList.toggle('is-hidden', window.scrollY < limite);
  }
  function mede() {
    limite = marca.getBoundingClientRect().top + window.scrollY;
    aplica();
  }
  mede();
  addEventListener('scroll', aplica, { passive: true });
  addEventListener('resize', mede, { passive: true });
  addEventListener('load', mede);
})();
</script>
"""


def _pending() -> str:
    faltando = [nome for nome, valor in
                (("telefone", SITE["phone"]), ("e-mail", SITE["email"]),
                 ("WhatsApp", SITE["whatsapp"]))
                if not valor.strip() or valor.strip().startswith("[")]
    return ("Falta preencher: " + ", ".join(faltando) + ".") if faltando else "Texto ainda em revisão."


CASES = [
    {
        "slug": "urbo",
        "vitrine": ['papelaria', 'sacola'],
        "title": "Urbo Gastrobar",
        "area": "Identidade visual",
        "year": "2020",
        "client": "Nicole Katz",
        "kind": "Acadêmico e profissional",
        "partner": "Isadora Duarte",
        "color": "#E86A10",
        "summary": "Identidade de um gastrobar construída a partir de um anel e de um padrão modular "
                   "que cobre superfícies inteiras sem repetir o logotipo.",
        "contexto": [
            "Identidade visual para um gastrobar, desenvolvida em dupla. O projeto vai da marca às "
            "aplicações que o cliente usa no dia a dia: papelaria, cartões da equipe, fachada, cardápio, "
            "embalagem de delivery, sacola, bottons e site.",
        ],
        "conceito": [
            "A marca gira em torno de um “o” que vira um anel laranja, reconhecível sozinho como símbolo. "
            "Do anel sai um padrão de blocos retangulares em roxo, verde, laranja e branco, separados por "
            "linhas finas, que funciona como azulejaria.",
        ],
        "sistema": [
            "Marca “urb + anel” com grade de construção documentada, em versão horizontal e símbolo isolado.",
            "Paleta de quatro cores — roxo, laranja, verde e preto — com branco como respiro.",
            "Lao UI para display e Avenir LT Std para apoio, com a família prevista em todos os pesos.",
            "Padrão modular de blocos aplicado em cheio na sacola, no cardápio, na embalagem e no site.",
            "Assinatura testada em quatro fundos de cor, para garantir leitura em qualquer aplicação.",
        ],
        "aplicacoes": "Cartões de visita nominais da equipe do salão e da cozinha, papelaria e envelope, "
                      "placa de fachada, sacola de tecido, bottons, cardápio digital, site desktop e mobile, "
                      "e embalagem de delivery.",
        "creditos": "Rafaela Senceite e Isadora Duarte. Cliente: Nicole Katz.",
        "images": [
            ("papelaria", "Papelaria da Urbo sobre fundo laranja: bloco de anotações, envelope preto, cartão e caneta."),
            ("marca", "Marca Urbo Gastrobar em roxo e verde, com o anel laranja no lugar da letra o."),
            ("simbolo", "Anel laranja isolado sobre fundo roxo, usado como símbolo da marca."),
            ("construcao", "Grade de construção do logotipo, com guias e proporções do anel."),
            ("padrao", "Padrão modular de blocos em laranja, verde e roxo com a marca aplicada ao centro."),
            ("tipografia", "Página de tipografia: Lao UI para display e Avenir LT Std para apoio."),
            ("assinatura", "Assinatura da marca aplicada em quatro fundos: roxo, laranja, preto e verde."),
            ("cartoes", "Cartões de visita nominais da equipe sobre fundo laranja."),
            ("sacola", "Sacola de tecido com o padrão modular e bottons nas cores da marca."),
            ("fachada", "Placa de fachada com a marca, instalada em uma estrutura verde."),
            ("site", "Site da Urbo em desktop e celular, montado sobre o padrão modular."),
            ("embalagem", "Embalagem de delivery e cardápio com o padrão aplicado."),
        ],
    },
    {
        "slug": "reconhecer",
        "vitrine": ['abertura', 'ife'],
        "title": "Reconhecer e Reparar",
        "area": "Comunicação institucional",
        "year": "2022",
        "client": "Fundação Roberto Marinho",
        "kind": "Profissional",
        "partner": None,
        "color": "#F5372B",
        "summary": "Campanha de mobilização sobre racismo estrutural em que o dado e a fonte são o "
                   "próprio elemento gráfico.",
        "contexto": [
            "Campanha de mobilização sobre racismo estrutural no Brasil, construída em cima de dados e de "
            "citações de pesquisadoras e pesquisadores negros. Cada peça carrega uma informação e a fonte dela.",
        ],
        "conceito": [
            "O conteúdo é o elemento gráfico. Tipografia condensada em caixa alta ocupa a peça inteira e a "
            "cor de fundo muda a cada afirmação, o que dá ritmo à série quando as peças aparecem em sequência.",
        ],
        "sistema": [
            "Prohibition para os títulos e Helvetica para o texto corrido.",
            "Assinatura “Reconhecer e Reparar” com o jogo entre a cerquilha e as duas palavras.",
            "Fundos chapados em vermelho, roxo, verde e rosa, um por peça.",
            "Dado grifado em cor contrastante dentro da frase, com a fonte sempre no rodapé, separada por um fio.",
            "Peças de retrato com ilustração e biografia curta de Maria Firmina dos Reis, Luiz Gama e Luiza Bairros.",
        ],
        "aplicacoes": "Série de cards de dado, citação, conceito e retrato, cartazes da linha IFÉ, peças de "
                      "stories com convidadas e assinatura animada em quatro cores.",
        "creditos": None,
        "images": [
            ("abertura", "Cartaz vermelho com a assinatura #Reconhecer e Reparar em tipografia condensada."),
            ("assinatura", "Página de assinatura da campanha, com o lockup Reconhecer e Reparar."),
            ("tipografia", "Página de tipografia da campanha: Prohibition para título e Helvetica para texto."),
            ("estudos", "Estudos de cartaz com as iniciais RER em verde, vermelho e rosa."),
            ("dado-milhoes", "Card vermelho: mais de 5 milhões de africanos foram sequestrados para o Brasil e escravizados."),
            ("racismo-agora", "Card roxo com a pergunta “Tudo é racismo agora?” entre aspas rosa."),
            ("retratos", "Três cards de retrato: Maria Firmina dos Reis, Luiz Gama e Luiza Bairros."),
            ("dado-56", "Card vermelho com o dado de 56,1% de pessoas autodeclaradas negras no país."),
            ("ife", "Três cartazes da linha IFÉ em amarelo, verde e branco."),
            ("stories", "Peças de stories com a convidada Nina da Hora sobre fundo vermelho e roxo."),
        ],
    },
    {
        "slug": "multiplo",
        "vitrine": ['capa-aberta', 'cronologia'],
        "title": "Múltiplo",
        "area": "Editorial",
        "year": "2021",
        "client": "Disciplina Projeto Editorial, UFRJ",
        "kind": "Acadêmico",
        "partner": None,
        "color": "#E01B1B",
        "summary": "Livro sobre Ferreira Gullar que reúne biografia, cronologia, poemas e obras em um "
                   "só volume, com papel dobrado como imagem-conceito.",
        "contexto": [
            "Livro sobre Ferreira Gullar que reúne biografia, cronologia, poemas e obras em um só volume. "
            "O projeto precisava organizar quatro tipos de conteúdo com pesos diferentes sem transformar o "
            "livro em quatro livros.",
        ],
        "papel": "Projeto gráfico completo: conceito, capa, grid, tipografia, tratamento de imagem e "
                 "diagramação do miolo.",
        "conceito": [
            "O título vira método. Papel dobrado, fotografado em vermelho, branco, amarelo e preto, abre cada "
            "seção. As dobras mudam de forma a cada página e sustentam a ideia de um autor que é várias coisas "
            "ao mesmo tempo.",
        ],
        "sistema": [
            "Paleta reduzida a vermelho, preto e branco, com amarelo só nas dobraduras.",
            "Corte vermelho nas laterais do bloco de texto, que identifica o livro fechado.",
            "Cronologia com os anos em vermelho, correndo na margem externa.",
            "Páginas pretas para os poemas, brancas para o ensaio e vermelhas para as aberturas de seção.",
            "Retratos em preto e branco alternados com duotone vermelho.",
        ],
        "aplicacoes": "Capa e quarta capa, lombada, cronologia, seção “Obras e poemas”, os poemas “Não há "
                      "vagas”, “Êxito” e “Os mortos”, e aberturas em duotone.",
        "creditos": "Rafaela Senceite.",
        "images": [
            ("capa-aberta", "Livro Múltiplo aberto mostrando a capa vermelha e preta com a dobradura branca."),
            ("capa", "Capa fechada do livro Múltiplo, em preto com a dobradura vermelha e branca."),
            ("obras-e-poemas", "Abertura da seção Obras e poemas, em vermelho, com mãos manipulando papel dobrado."),
            ("dobradura", "Dupla com uma dobradura fotografada à esquerda e um losango colorido à direita."),
            ("cronologia", "Dupla da cronologia, com os anos em vermelho na margem."),
            ("citacao", "Dupla preta com a citação “Não quero ter razão, quero é ser feliz”."),
            ("retrato", "Dupla com retrato de Ferreira Gullar em duotone vermelho."),
            ("nao-ha-vagas", "Dupla do poema “Não há vagas”, em vermelho e branco."),
            ("os-mortos", "Dupla preta do poema “Os mortos”, com dobradura em losango."),
        ],
    },
    {
        "slug": "n1pt",
        "vitrine": ['abertura', 'carrossel'],
        "title": "Nem 1 Pra Trás",
        "area": "Campanha institucional",
        "year": "2024",
        "client": "Fundação Roberto Marinho",
        "kind": "Profissional",
        "partner": None,
        "color": "#00A6B8",
        "summary": "Campanha do Dia da Educação com um sistema que fala com estudantes, professores e "
                   "organizações parceiras nos mesmos formatos.",
        "contexto": [
            "Campanha do Dia da Educação, em 28 de abril, com a hashtag #Nem1PraTrás e o site "
            "diadaeducacao.org como ponto de chegada. A campanha precisava falar com três públicos ao mesmo "
            "tempo: estudantes, professores e organizações parceiras.",
        ],
        "conceito": [
            "A campanha usa a moldura de uma janela de navegador ou de um balão de chat como elemento "
            "recorrente. O conteúdo aparece dentro dessa moldura, sobre um fundo que repete as hashtags da "
            "mobilização em tipografia de baixo contraste.",
        ],
        "sistema": [
            "Paleta de cinco cores chapadas: vermelho, amarelo, roxo, ciano e preto.",
            "Lettering “NEM1 PRA TRÁS” com contraste forte de peso entre as duas partes.",
            "Moldura de janela com os três controles no canto, usada como suporte de conteúdo.",
            "Cards de dado com o número em destaque, a frase em corpo médio e a fonte da pesquisa no rodapé.",
            "Cada peça existe em feed quadrado e em stories vertical.",
        ],
        "aplicacoes": "Cards de dados numerados, quiz, carrossel, peças institucionais, mailing, thumbnails "
                      "de vídeo, caça-palavras impresso e kit de peças personalizáveis para organizações parceiras.",
        "creditos": None,
        "images": [
            ("abertura", "Peça ciano com o lettering NEM1 PRA TRÁS e o endereço diadaeducacao.org."),
            ("institucional", "Peça vermelha: em aprendizado, não queremos deixar nem 1 pra trás."),
            ("dado-1", "Card vermelho com o dado sobre jovens que não concluíram a educação básica em 2022."),
            ("dado-3", "Card amarelo: 73% dos jovens fora da escola pretendem retomar os estudos."),
            ("dado-4", "Card roxo: 77% dos jovens que saíram da escola pretendem concluir o ensino médio."),
            ("dado-6", "Card ciano sobre ensino à distância para estudantes fora da escola."),
            ("carrossel", "Carrossel vermelho com fotos de estudantes dentro de molduras de janela."),
            ("quiz", "Peça roxa de quiz perguntando quando é celebrado o Dia da Educação."),
            ("parceiros", "Peça roxa do kit para organizações parceiras, com o lettering da campanha."),
            ("mailing", "Mailing vertical da campanha, em vermelho, com chamadas e vídeos."),
        ],
    },
    {
        "slug": "aruanda",
        "vitrine": ['capa', 'viola-davis'],
        "title": "Revista Aruanda",
        "area": "Editorial",
        "year": "2021",
        "client": "Disciplina Projeto Grid e Tipografia, UFRJ",
        "kind": "Acadêmico, em dupla",
        "partner": "Marco Antonio Martins",
        "color": "#D9922A",
        "summary": "Revista sobre manifestações artísticas de pessoas negras, em que cada edição tem um "
                   "tema e uma cor e a estrutura se mantém.",
        "contexto": [
            "Revista dedicada a manifestações artísticas de pessoas negras, de quem está começando a quem já "
            "é referência. O nome vem de Aruanda, o plano espiritual que na Umbanda acolhe os espíritos que "
            "trabalham pelo bem.",
        ],
        "conceito": [
            "Cada edição tem um tema e uma cor. A número 1, “Vozes”, é laranja. A número 2, “Corpos”, é roxa. "
            "A identidade se mantém e só a cor e o tema mudam, o que dá à revista uma coleção reconhecível.",
        ],
        "sistema": [
            "Grid modular de 5 por 9, diagramado em duas colunas.",
            "Capa tipográfica com o nome quebrado em três linhas, AR / UAN / DA, dentro de um colchete, sobre retrato em duotone.",
            "Estrutura editorial fixa: uma obra principal, duas secundárias e a seção aberta “você em Aruanda”.",
            "Colchete como elemento recorrente, marcando títulos, números de página e aberturas.",
            "Fotografia sempre em duotone na cor da edição.",
        ],
        "aplicacoes": "Capa, expediente, espelho da publicação, páginas de referência, matérias em duas "
                      "colunas e capa da edição 2.",
        "creditos": "Marco Antonio Martins e Rafaela Senceite.",
        "images": [
            ("capa", "Capa da Revista Aruanda número 1, Vozes, com o nome em três linhas sobre retrato em duotone laranja."),
            ("expediente", "Dupla com expediente e sumário, com números dentro de colchetes."),
            ("principia", "Dupla da matéria Principia, com retrato e letra da música em duas colunas."),
            ("emicida", "Dupla sobre Emicida, com a frase “E eu pinto tudo em amarelo” em destaque."),
            ("viola-davis", "Dupla com o discurso de Viola Davis no Emmy de 2015."),
            ("ryane-leao", "Dupla com um poema de Ryane Leão e retrato da autora."),
            ("voce-em-aruanda", "Dupla da seção Você em Aruanda, com Abgail Batista e girassóis em duotone."),
            ("grid", "Página da apresentação explicando o grid modular de 5 por 9 em duas colunas."),
            ("edicao-2", "Capa da edição 2, Corpos, em duotone roxo."),
        ],
    },
    {
        "slug": "budapeste",
        "vitrine": ['capa', 'miolo'],
        "title": "Budapeste",
        "area": "Editorial",
        "year": "2021",
        "client": "Disciplina Projeto Editorial, UFRJ",
        "kind": "Acadêmico",
        "partner": None,
        "color": "#F2B705",
        "summary": "Redesign do romance de Chico Buarque, com a cor tirada de uma frase do próprio livro "
                   "e o título espelhado na quarta capa.",
        "contexto": [
            "Redesign do romance de Chico Buarque, em que um ghost-writer brasileiro se perde em Budapeste e "
            "passa a viver entre duas línguas.",
        ],
        "papel": "Projeto gráfico completo: conceito, capa, tipografia e miolo.",
        "conceito": [
            "A cor sai de uma frase do próprio livro: “uma cidade amarela, eu pensava que Budapeste fosse "
            "cinzenta, mas Budapeste era amarela”. O amarelo toma a capa inteira e o Parlamento húngaro "
            "aparece em meio-tom marrom, recortado como se estivesse rasgado da página.",
        ],
        "sistema": [
            "Amarelo como cor única da capa, contra um miolo em papel creme.",
            "Título repetido na quarta capa em espelho, de cabeça para baixo, marcando a inversão entre as duas línguas do romance.",
            "Meio-tom grosso na imagem do Parlamento, com o recorte irregular servindo de moldura.",
            "Miolo sóbrio, em uma coluna, com fólio centralizado e marca de seção discreta.",
        ],
        "aplicacoes": "Capa, quarta capa, lombada, aberturas de capítulo e páginas de miolo.",
        "creditos": "Rafaela Senceite.",
        "images": [
            ("capa", "Capa amarela de Budapeste com o Parlamento húngaro em meio-tom marrom."),
            ("capa-e-quarta", "Capa e quarta capa lado a lado, com o título espelhado."),
            ("espelho", "Livro aberto mostrando a continuidade da imagem entre capa e quarta capa."),
            ("cidade-amarela", "Página amarela com a citação sobre a cidade amarela e o Parlamento ao fundo."),
            ("miolo", "Livro aberto no miolo, em papel creme, com o texto em uma coluna."),
            ("aberto", "Livro aberto sobre fundo amarelo, mostrando capa e primeiras páginas."),
        ],
    },
]

E = html.escape


def head(title: str, description: str, color: str, depth: int, body_class: str) -> str:
    base = "../" if depth else ""
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
{'<meta name="robots" content="noindex">' if DRAFT else ''}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/site.css">
<style>:root{{--case:{color}}}</style>
</head>
<body class="{body_class} font-sans antialiased">
<a href="#conteudo" class="skip">Pular para o conteúdo</a>
"""


def whatsapp_cta(size: str = "sm") -> str:
    """Botão do WhatsApp. Sem número configurado ele vira um span desabilitado:
    publicar um wa.me quebrado é pior do que publicar um botão apagado."""
    label = "Agende uma conversa"
    pad = "min-h-11 px-4 text-sm" if size == "sm" else "min-h-12 px-6 text-base"
    icon = (
        '<svg viewBox="0 0 24 24" class="size-4 shrink-0" fill="currentColor" aria-hidden="true">'
        '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.97L2 22l5.25-1.38a9.87 9.87 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.13h-.01a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.17 8.17 0 0 1-1.26-4.36c0-4.54 3.7-8.24 8.25-8.24 2.2 0 4.27.86 5.83 2.42a8.19 8.19 0 0 1 2.41 5.83c0 4.54-3.7 8.21-8.24 8.21Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.78.97-.14.16-.29.18-.54.06-.25-.13-1.05-.39-2-1.23-.74-.66-1.24-1.47-1.38-1.72-.15-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.41.09-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.87.85-.87 2.07 0 1.22.89 2.4 1.02 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.08.15-1.18-.06-.11-.22-.17-.47-.29Z"/>'
        "</svg>"
    )
    inner = f'{icon}<span>{label}</span>'
    common = (f"inline-flex items-center justify-center gap-2 rounded-sm font-bold "
              f"tracking-tight {pad}")
    number = SITE["whatsapp"].strip()
    if not number:
        return (f'<span class="{common} cursor-not-allowed bg-neutral-200 text-neutral-500" '
                f'aria-disabled="true" title="Falta o número do WhatsApp">{inner}</span>')
    url = f"https://wa.me/{number}?text={quote(SITE['whatsapp_message'])}"
    return (f'<a href="{url}" class="{common} bg-graphite text-white transition-colors '
            f'hover:bg-neutral-700 focus-ring" target="_blank" rel="noopener">{inner}</a>')


def header(depth: int, current: str = "", overlay: bool = False) -> str:
    """overlay=True deixa o cabeçalho fora do fluxo. É o que a home precisa: escondido,
    um cabeçalho sticky continuaria reservando a própria altura e abriria um vão no
    topo do hero."""
    base = "../" if depth else ""
    posicao = "fixed inset-x-0 top-0" if overlay else "sticky top-0"
    return f"""<header class="site-header on-brand {posicao} z-40 border-b border-white/15">
  <div class="wrap flex flex-wrap items-center justify-between gap-x-6 gap-y-2 py-3 md:h-20 md:flex-nowrap md:py-0">
    <a href="{base}index.html" class="text-sm font-black uppercase tracking-[0.18em] text-yellow">{E(SITE['name'])}</a>
    <div class="flex flex-wrap items-center gap-x-5 gap-y-2">
      <nav aria-label="Principal" class="flex items-center gap-5 text-sm">
        <a href="{base}index.html#projetos" class="link"{' aria-current="page"' if current == 'projetos' else ''}>Projetos</a>
        <a href="{base}index.html#sobre" class="link">Sobre</a>
        <a href="{base}index.html#contato" class="link">Contato</a>
      </nav>
      <span aria-hidden="true" class="hidden h-8 w-px bg-white/25 md:block"></span>
      {whatsapp_cta()}
    </div>
  </div>
</header>
"""


def draft_banner(note: str) -> str:
    if not DRAFT:
        return ""
    return f"""<p role="status" class="bg-ink px-6 py-3 text-center text-sm text-paper">
Rascunho interno. {E(note)}</p>
"""


def footer(depth: int, scripts: str = "") -> str:
    base = "../" if depth else ""
    return f"""<footer class="bg-graphite text-white">
  <nav aria-label="Rodapé" class="mx-auto flex max-w-[956px] flex-wrap items-center justify-center gap-x-8 gap-y-2 px-6 pt-10">
    <a href="{base}index.html" class="menu-link">Portfólio</a>
    <a href="{base}sobre.html" class="menu-link">Sobre</a>
    <a href="{base}contato.html" class="menu-link">Contato</a>
  </nav>
  <p class="mx-auto max-w-[956px] px-6 py-8 text-center text-xs text-neutral-500">© 2026 {E(SITE['name'])}</p>
</footer>
{zap_flutuante()}{scripts}</body>
</html>
"""


def size_of(slug: str, name: str) -> tuple[int, int]:
    from PIL import Image

    with Image.open(ROOT / "assets" / "img" / slug / f"{name}.webp") as img:
        return img.size


def figure(case: dict, name: str, alt: str, *, eager: bool) -> str:
    src = f"../assets/img/{case['slug']}/{name}"
    w, h = size_of(case["slug"], name)
    return f"""<figure class="overflow-hidden rounded-sm bg-shade">
  <img src="{src}.webp" srcset="{src}@sm.webp 800w, {src}.webp 1600w"
       sizes="(min-width: 768px) 50vw, 100vw" alt="{E(alt)}" width="{w}" height="{h}"
       loading="{'eager' if eager else 'lazy'}" decoding="async" class="h-full w-full object-cover">
</figure>"""


def hero(case: dict, name: str, alt: str) -> str:
    """Colour band with the cover contained, so portrait and landscape covers
    both show whole instead of being cropped by a fixed aspect ratio."""
    src = f"../assets/img/{case['slug']}/{name}"
    w, h = size_of(case["slug"], name)
    return f"""<div class="bg-[var(--case)]">
  <img src="{src}.webp" srcset="{src}@sm.webp 800w, {src}.webp 1600w"
       sizes="100vw" alt="{E(alt)}" width="{w}" height="{h}"
       fetchpriority="high" decoding="async"
       class="mx-auto max-h-[78svh] w-auto object-contain">
</div>"""


def case_page(case: dict, prev: dict, nxt: dict) -> str:
    cover, cover_alt = case["images"][0]
    rest = case["images"][1:]
    meta = [("Cliente", case["client"]), ("Ano", case["year"]), ("Área", case["area"]), ("Tipo", case["kind"])]
    if case["partner"]:
        meta.append(("Parceria", case["partner"]))
    meta_html = "".join(
        f'<div><dt class="text-xs uppercase tracking-[0.14em] text-muted">{E(k)}</dt>'
        f'<dd class="mt-1">{E(v)}</dd></div>'
        for k, v in meta
    )
    papel = ""
    if case.get("papel"):
        papel = f"""<section class="section">
  <h2 class="label">Papel</h2>
  <p class="prose-p">{E(case['papel'])}</p>
</section>"""
    creditos = ""
    if case.get("creditos"):
        creditos = f"""<section class="section">
  <h2 class="label">Créditos</h2>
  <p class="prose-p">{E(case['creditos'])}</p>
</section>"""
    contexto = "".join(f'<p class="prose-p">{E(p)}</p>' for p in case["contexto"])
    conceito = "".join(f'<p class="prose-p">{E(p)}</p>' for p in case["conceito"])
    sistema = "".join(f"<li>{E(i)}</li>" for i in case["sistema"])
    grid = "\n".join(figure(case, n, a, eager=False) for n, a in rest)

    return (
        head(f"{case['title']} — {SITE['name']}", case["summary"], case["color"], depth=1,
             body_class="bg-paper text-ink")
        + draft_banner("Os créditos e a divisão de autoria ainda dependem de confirmação da Rafaela.")
        + barra_menu(depth=1)
        + f"""<main id="conteudo">
  <article>
    <div class="rule" aria-hidden="true"></div>
    {hero(case, cover, cover_alt)}
    <div class="wrap">
      <header class="max-w-3xl pt-12">
        <p class="label">{E(case['area'])} · {E(case['year'])}</p>
        <h1 class="mt-4 text-display font-black leading-[0.95] tracking-tight">{E(case['title'])}</h1>
        <p class="mt-6 text-xl leading-relaxed text-muted">{E(case['summary'])}</p>
      </header>
      <dl class="mt-12 grid grid-cols-2 gap-6 border-y border-line py-6 text-sm md:grid-cols-5">{meta_html}</dl>

      <section class="section">
        <h2 class="label">Contexto</h2>
        {contexto}
      </section>
      {papel}
      <section class="section">
        <h2 class="label">Conceito</h2>
        {conceito}
      </section>
      <section class="section">
        <h2 class="label">Sistema visual</h2>
        <ul class="prose-list">{sistema}</ul>
      </section>

      <div class="mt-16 grid gap-4 md:grid-cols-2">
{grid}
      </div>

      <section class="section">
        <h2 class="label">Aplicações</h2>
        <p class="prose-p">{E(case['aplicacoes'])}</p>
      </section>
      {creditos}

      <nav aria-label="Outros projetos" class="mt-20 flex flex-wrap justify-between gap-4 border-t border-line pt-8 text-sm">
        <a href="{prev['slug']}.html" class="link">← {E(prev['title'])}</a>
        <a href="{nxt['slug']}.html" class="link">{E(nxt['title'])} →</a>
      </nav>
    </div>
  </article>
</main>
"""
        + footer(depth=1)
    )


def barra_menu(depth: int, atual: str = "portfolio") -> str:
    """Menu no topo, em barra escura, como a referência faz no rodapé.
    Kaz pediu no topo."""
    base = "../" if depth else ""
    itens = [("portfolio", "Portfólio", f"{base}index.html"),
             ("sobre", "Sobre", f"{base}sobre.html"),
             ("contato", "Contato", f"{base}contato.html")]
    links = "".join(
        f'<a href="{href}" class="menu-link"'
        f'{chr(32) + chr(97) + "ria-current=" + chr(34) + "page" + chr(34) if chave == atual else ""}>{E(rotulo)}</a>'
        for chave, rotulo, href in itens
    )
    return f"""<header class="bg-graphite">
  <nav aria-label="Principal" class="mx-auto flex max-w-[956px] flex-wrap items-center justify-center gap-x-8 gap-y-2 px-6 py-4">
    {links}
  </nav>
</header>
"""


def zap_flutuante() -> str:
    numero = SITE["whatsapp"].strip()
    if not numero:
        return ""
    url = f"https://wa.me/{numero}?text={quote(SITE['whatsapp_message'])}"
    return f"""<a href="{url}" class="zap" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp">
  <svg viewBox="0 0 24 24" class="size-7" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.97L2 22l5.25-1.38a9.87 9.87 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.13h-.01a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.17 8.17 0 0 1-1.26-4.36c0-4.54 3.7-8.24 8.25-8.24 2.2 0 4.27.86 5.83 2.42a8.19 8.19 0 0 1 2.41 5.83c0 4.54-3.7 8.21-8.24 8.21Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.78.97-.14.16-.29.18-.54.06-.25-.13-1.05-.39-2-1.23-.74-.66-1.24-1.47-1.38-1.72-.15-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.41.09-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.87.85-.87 2.07 0 1.22.89 2.4 1.02 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.08.15-1.18-.06-.11-.22-.17-.47-.29Z"/></svg>
</a>
"""


def index_page() -> str:
    pecas = []
    for case in CASES:
        legendas = dict(case["images"])
        for nome in case["vitrine"]:
            capa, alt = nome, legendas[nome]
            src = f"assets/img/{case['slug']}/{capa}"
            w, h = size_of(case["slug"], capa)
            pecas.append(f"""<a href="cases/{case['slug']}.html" class="group block focus-ring" aria-label="{E(case['title'])}">
  <img src="{src}@sm.webp" srcset="{src}@sm.webp 800w, {src}.webp 1600w"
       sizes="(min-width: 900px) 312px, (min-width: 640px) 46vw, 92vw" alt="{E(alt)}"
       width="{w}" height="{h}" loading="lazy" decoding="async"
       class="w-full transition-opacity duration-200 group-hover:opacity-85 motion-reduce:transition-none">
</a>""")

    return (
        head(f"{SITE['name']} — {SITE['role']}", SITE["lede"], "#2A2A2A", depth=0,
             body_class="bg-canvas text-graphite")
        + draft_banner(_pending())
        + barra_menu(depth=0)
        + f"""<main id="conteudo">
  <section class="mx-auto max-w-[956px] px-6 pt-16 pb-12 text-center">
    <h1 class="text-2xl font-bold uppercase tracking-[0.2em] md:text-[26px]">{E(SITE['name'])}</h1>
    <p class="mt-4 text-base font-light uppercase tracking-[0.18em] text-neutral-600 md:text-lg">Designer gráfica</p>
  </section>

  <section id="projetos" class="mx-auto max-w-[956px] px-6 pb-16">
    <h2 class="sr-only">Projetos</h2>
    <div class="vitrine">
      {"".join(pecas)}
    </div>
  </section>

</main>
"""
        + footer(depth=0)
    )


def sobre_page() -> str:
    """Segue o layout da página Sobre da referência: nome centralizado, retrato à
    esquerda, texto à direita, botão de currículo. O Contato repete a estrutura de
    duas colunas da página de contato do template. Lá o lado direito é um formulário,
    que num site estático não teria para onde enviar; no lugar vão os canais reais."""
    w, h = size_of("sobre", "retrato")
    tools = ("Photoshop, Illustrator, InDesign, Premiere e Dreamweaver, Figma, Canva, "
             "Trello, Miro e o pacote Office.")
    return (
        head(f"Sobre — {SITE['name']}", SITE["lede"], "#2A2A2A", depth=0,
             body_class="bg-canvas text-graphite")
        + draft_banner(_pending())
        + barra_menu(depth=0, atual="sobre")
        + f"""<main id="conteudo" class="mx-auto max-w-[956px] px-6 pb-24">
  <p class="pt-16 pb-14 text-center text-2xl font-bold uppercase tracking-[0.2em] md:text-[26px]">{E(SITE['name'])}</p>

  <section class="grid gap-10 md:grid-cols-[minmax(0,476px)_minmax(0,1fr)] md:gap-14">
    <img src="assets/img/sobre/retrato.webp" srcset="assets/img/sobre/retrato@sm.webp 600w, assets/img/sobre/retrato.webp 1200w"
         sizes="(min-width: 768px) 476px, 92vw" width="{w}" height="{h}"
         alt="Retrato de {E(SITE['name'])}" decoding="async" class="w-full">
    <div>
      <h1 class="text-base font-normal uppercase tracking-[0.2em]">Sobre</h1>
      <p class="mt-8 leading-relaxed">Bacharela em Comunicação Visual Design pela UFRJ, com sete anos de
      trabalho em identidade visual, design editorial e comunicação institucional. Passei por projetos de
      marca para clientes e por campanhas da Fundação Roberto Marinho, onde desdobrei identidade em peças
      institucionais para Aprendiz Legal, Futura, Telecurso e co.liga.</p>
      <p class="mt-5 leading-relaxed">Atendo como freelancer desde 2019. Trabalho com grid, tipografia e
      sistemas que precisam funcionar em formatos diferentes, e preparo arquivo para impressão e fechamento
      gráfico.</p>
      <p class="mt-5 text-sm text-neutral-600">{E(tools)}</p>
      <a href="assets/curriculo-rafaela-senceite.pdf" target="_blank" rel="noopener"
         class="mt-8 inline-flex min-h-11 items-center bg-graphite px-7 text-sm text-white transition-colors hover:bg-neutral-700 focus-ring">Currículo</a>
    </div>
  </section>

</main>
"""
        + footer(depth=0)
    )


def contato_page() -> str:
    """Duas colunas como a página de contato da referência. Lá a coluna direita é um
    formulário; num site estático ele não teria para onde enviar, então ficam os
    canais que funcionam de verdade."""
    return (
        head(f"Contato — {SITE['name']}", SITE["availability"], "#2A2A2A", depth=0,
             body_class="bg-canvas text-graphite")
        + draft_banner(_pending())
        + barra_menu(depth=0, atual="contato")
        + f"""<main id="conteudo" class="mx-auto max-w-[956px] px-6 pb-32">
  <p class="pt-16 pb-14 text-center text-2xl font-bold uppercase tracking-[0.2em] md:text-[26px]">{E(SITE['name'])}</p>

  <div class="grid gap-10 md:grid-cols-[minmax(0,476px)_minmax(0,1fr)] md:gap-14">
    <div>
      <h1 class="text-base font-normal uppercase tracking-[0.2em]">Contato</h1>
      <dl class="mt-8 leading-relaxed">
        <div><dt class="sr-only">E-mail</dt><dd><a href="mailto:{E(SITE['email'])}" class="underline underline-offset-4">{E(SITE['email'])}</a></dd></div>
        <div class="mt-1"><dt class="sr-only">Telefone</dt><dd>Tel: {E(SITE['phone'])}</dd></div>
      </dl>
    </div>
    <div>
      <p class="max-w-[520px] text-lg leading-relaxed">{E(SITE['availability'])}</p>
      <div class="mt-9">{whatsapp_cta('lg')}</div>
      <p class="mt-4 text-sm text-neutral-500">Respondo mais rápido pelo WhatsApp.</p>
    </div>
  </div>
</main>
"""
        + footer(depth=0)
    )


def main() -> None:
    (ROOT / "cases").mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(index_page(), encoding="utf-8")
    (ROOT / "sobre.html").write_text(sobre_page(), encoding="utf-8")
    (ROOT / "contato.html").write_text(contato_page(), encoding="utf-8")
    written = ["index.html", "sobre.html", "contato.html"]
    for i, case in enumerate(CASES):
        prev, nxt = CASES[i - 1], CASES[(i + 1) % len(CASES)]
        (ROOT / "cases" / f"{case['slug']}.html").write_text(case_page(case, prev, nxt), encoding="utf-8")
        written.append(f"cases/{case['slug']}.html")

    missing = [
        f"{case['slug']}/{name}"
        for case in CASES
        for name, _ in case["images"]
        if not (ROOT / "assets" / "img" / case["slug"] / f"{name}.webp").exists()
    ]
    for path in written:
        print(path)
    for name in missing:
        print(f"MISSING IMAGE\t{name}")
    assert not missing, "missing images break the build"


if __name__ == "__main__":
    main()
