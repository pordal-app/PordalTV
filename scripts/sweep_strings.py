"""Case-preserving Nuvio->Pordal sweep over res/values*/strings.xml.

Protected (never rewritten):
- name="..." attribute values (resource IDs referenced from code)
- the licenses_attributions_nuvio_title/body elements (GPL attribution must
  keep crediting the upstream NuvioTV project, in every locale)
"""
import re
import glob

REPLACEMENTS = [  # longest-first
    ("NuvioTV", "PordalTV"),
    ("Nuvio TV", "Pordal TV"),
    ("NUVIO", "PORDAL"),
    ("Nuvio", "Pordal"),
    ("nuvio", "pordal"),
]

PROTECT = [
    re.compile(r'name="[^"]*"'),
    re.compile(
        r'<string name="licenses_attributions_nuvio_(?:title|body)"[^>]*>.*?</string>',
        re.DOTALL,
    ),
]

def protected_ranges(text):
    spans = []
    for rx in PROTECT:
        spans.extend(m.span() for m in rx.finditer(text))
    return sorted(spans)

def in_protected(pos, spans):
    return any(s <= pos < e for s, e in spans)

def sweep(text):
    spans = protected_ranges(text)
    out = []
    i = 0
    while i < len(text):
        hit = None
        if not in_protected(i, spans):
            for old, new in REPLACEMENTS:
                if text.startswith(old, i):
                    hit = (old, new)
                    break
        if hit:
            out.append(hit[1])
            i += len(hit[0])
        else:
            out.append(text[i])
            i += 1
    return "".join(out)

changed = 0
for path in sorted(glob.glob("app/src/main/res/values*/strings.xml")):
    with open(path, encoding="utf-8") as f:
        original = f.read()
    swept = sweep(original)
    if swept != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(swept)
        changed += 1
        print(f"swept: {path}")
print(f"{changed} files changed")
