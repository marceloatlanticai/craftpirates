# feita de pontos — sala de criação

Oito mentes feitas de pontos de luz que trabalham briefs e ideias com
profissionais criativos: a alquimista, a semióloga, o estrategista,
a provocadora, o poeta, o brincante, o explorador e o cético.

## Estrutura do repositório

```
├── app.py            # wrapper Streamlit (injeta a chave e serve o index)
├── index.html        # a experiência completa (arquivo único, autossuficiente)
├── requirements.txt
└── .streamlit/
    └── secrets.toml  # NUNCA comitar — ver .gitignore
```

## Rodando localmente

1. `pip install -r requirements.txt`
2. Crie `.streamlit/secrets.toml` com:
   ```toml
   GEMINI_API_KEY = "sua-chave-aqui"
   ```
   (gere a chave em https://aistudio.google.com/apikey)
3. `streamlit run app.py`

Sem chave configurada, a experiência roda com respostas de reserva
(as provocações curadas de cada mente) — útil para testar o visual.

## Publicando (Streamlit Community Cloud)

1. Suba `app.py`, `index.html` e `requirements.txt` para um repositório
   no GitHub. **Adicione `.streamlit/` ao `.gitignore`.**
2. Em https://share.streamlit.io, conecte o repositório.
3. Em *App settings → Secrets*, cole `GEMINI_API_KEY = "sua-chave"`.

## Segurança da chave — leia isto

O Streamlit injeta a chave no HTML que roda no navegador do visitante.
Isso significa que **um visitante técnico consegue vê-la**. Para uso
pessoal, demonstrações e portfólio, é um risco aceitável DESDE QUE você:

1. **Restrinja a chave por referenciador HTTP** no Google Cloud Console
   (APIs & Services → Credentials → sua chave → Application restrictions
   → HTTP referrers → adicione `https://SEU-APP.streamlit.app/*`).
2. **Defina cotas baixas** para a API Generative Language no mesmo console.

Para um lançamento público sério, o caminho certo é um proxy mínimo
(Cloud Function / Cloud Run) que guarda a chave no servidor — quando
chegar essa hora, o `llm()` do index.html troca a URL em uma linha.

## Como funciona por dentro

- `index.html` detecta a chave: com Gemini configurado, usa
  `gemini-2.5-flash` **com Google Search (grounding)** — as mentes
  citam campanhas e movimentos reais e recentes das marcas.
- O roteador de elenco decide qual mente responde a cada fala; quando
  outra mente tem a técnica mais valiosa, ela pede a palavra e o rosto
  se metamorfoseia.
- **✦ sintetizar sessão** entrega a sessão ao Estrategista: territórios,
  tensão central e próximo passo.
