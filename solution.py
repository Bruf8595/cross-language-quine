py = """py = {0!r}
js = "const py = {0!r};\\nconsole.log(py);"
print(js.format(py))
"""
js = "const py = {0!r};\nconsole.log(py);"
print(js.format(py))
