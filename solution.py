s = 's = {0!r}\nimport json\nprint("console.log(" + json.dumps(s.format(repr(s))) + ");")'
import json
print("console.log(" + json.dumps(s.format(repr(s))) + ");")
