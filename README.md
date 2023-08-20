# building-ai-products-with-openai

Running and deploying backend

```modal run ./podcast_backend.py --url https://anchor.fm/s/5e09c654/podcast/rss --path ./podcasts/```

```modal deploy podcast_backend.py ```

Running frontend locally (deploy = push to github)

```streamlit run podcast_frontend.py```

Testing local function
```python podcast_backend.py get_podcast_summary "hello"```

Colab notebook
https://colab.research.google.com/drive/16nmbXW_5RaRZYP4GTpfE_e21rx8rh4YK#scrollTo=pUnIxoJUXHbE