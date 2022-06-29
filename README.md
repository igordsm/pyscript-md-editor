## Markdown editor in PyScript

This is an example of using [PyScript](https://pyscript.net/) to create a simple webapp. Some highlights:

1. uses the [markdown](https://github.com/Python-Markdown/markdown/) module to convert markdown -> HTML
2. uses browser APIs (`setInterval`) and modifies the DOM
3. persists virtual filesystem data using emscripten's [`FS`](https://emscripten.org/docs/api_reference/Filesystem-API.html) API

Live demo at [https://igordsm.github.io/pyscript-md-editor/](https://igordsm.github.io/pyscript-md-editor/)