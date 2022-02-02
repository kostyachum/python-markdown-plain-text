# python-markdown-plain-text
Plain Text Extension for Python Markdown


# Installation

using pip

```
pip install -e git+https://github.com/kostyachum/python-markdown-plain-text.git#egg=plain-text-markdown-extention
```


# Usage
Just use it as extenetion
```python
from markdown_plain_text.extention import PlainTextExtension
from markdown import Markdown

...
plain_text = Markdown(extentions=[PlainTextExtension()]).convert(mardown_text)
...

```


Or use shorcut method:
```python
from markdown_plain_text.extention import convert_to_plain_text

...
plain_text = convert_to_plain_text(mardown_text)
...

```


# Contribution

1. Fork and create a branch
2. pip install .
3. do the changes
4. python -m unittest
5. Create a Pull-Request