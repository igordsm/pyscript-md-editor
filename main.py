import asyncio
import markdown
from js import document, window, console
from pyodide import to_js
import pyodide_js


def do_convert(source, target, converter):
    text = source.value
    target.innerHTML = converter.convert(text)

    with open('data/teste.txt', 'w') as f:
        f.write(text)
    
    pyodide_js.FS.syncfs(to_js(lambda e: console.log(e)))


def load_existing_data(source, target, converter, e):
    try:
        with open('data/teste.txt') as f:
            source.value = f.read()
            do_convert(source, target, converter)
    except:
        console.log('não existe!!!')


def init():
    converter = markdown.Markdown()

    source = document.getElementById('markdown-source')
    target = document.getElementById('markdown-target')
    window.setInterval(to_js(lambda: do_convert(source, target, converter)), 5000)

    pyodide_js.FS.mkdir('data')
    pyodide_js.FS.mount(pyodide_js.FS.filesystems.IDBFS, {}, '/home/pyodide/data/')

    pyodide_js.FS.syncfs(True, to_js(lambda e: load_existing_data(source, target, converter, e)))


init()