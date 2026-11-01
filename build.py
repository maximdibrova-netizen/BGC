"""Собирает index.html (версия для сайта, с онлайном) из src/ui.html и src/core.js.
Запуск: python3 build.py"""
import os
here = os.path.dirname(os.path.abspath(__file__))
ui = open(os.path.join(here, 'src', 'ui.html'), encoding='utf-8').read()
core = open(os.path.join(here, 'src', 'core.js'), encoding='utf-8').read()
page = ui.replace('/*CORE*/', core)
head = ('<!doctype html>\n<html lang="ru"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>'
        '<script>window.BGC_ONLINE=true;</script></head><body>\n')
open(os.path.join(here, 'index.html'), 'w', encoding='utf-8').write(head + page + '\n</body></html>\n')
print('index.html собран')
