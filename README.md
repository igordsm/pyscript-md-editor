## Editor de Markdown em Python

Este é um exemplo de utilização de [PyScript](https://pyscript.net/) para a criação de uma aplicação web simples. Alguns pontos de destaque são

1. utilização sem modificações do módulo [markdown](https://github.com/Python-Markdown/markdown/) para conversão markdown -> HTML
2. utilização de APIs do browser (`setInterval`) e acesso a DOM
3. persistência de dados usando a API [`FS`](https://emscripten.org/docs/api_reference/Filesystem-API.html) do emscripten

Acesse [https://igordsm.github.io/pyscript-md-editor/](https://igordsm.github.io/pyscript-md-editor/) para ver uma versão funcional.