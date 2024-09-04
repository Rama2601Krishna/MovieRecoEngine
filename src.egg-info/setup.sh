mkdir -p ~/.streamlit/

echo "\
[server]\n\
port=$PORT\n\
nableCORS=false\n\
headless=true\n\
\n\

" > ~/.streamlit/config.toml