"""Number sections, equations and figures in src.md, generate the contents, build the .docx."""
import glob, re, subprocess, sys

HERE = sys.path[0]
src = '\n\n'.join(open(f, encoding='utf-8').read().strip('\n') for f in sorted(glob.glob(HERE + '/src/*.md'))) + '\n'
head_end = src.index('\n---', 4) + 4
meta, body = src[:head_end], src[head_end:]

parts, secs = [], []          # parts: (title, id); secs: (part index, n, title, label)
def part(m):
    parts.append(m.group(1))
    return '# %s {#part_%d}' % (m.group(1), len(parts))
body = re.sub(r'^# (Part .+?)\s*$', part, body, flags=re.M)

sec_no = {}
lines = body.split('\n')
for i, line in enumerate(lines):
    m = re.match(r'^# Part .* \{#part_(\d+)\}$', line)
    if m:
        cur = int(m.group(1))
    m = re.match(r'^## (.+) \{#(\w+)\}$', line)
    if m and m.group(2) != 'contents':
        n = len(secs) + 1
        sec_no[m.group(2)] = n
        secs.append((cur, n, m.group(1), m.group(2)))
        lines[i] = '## %d. %s {#sec_%d}' % (n, m.group(1), n)
body = '\n'.join(lines)

eq_no, fig_no = {}, {}
for lab in re.findall(r'\\quad\(\\#(\w+)\)', body):
    if lab in eq_no:
        sys.exit('duplicate equation label ' + lab)
    eq_no[lab] = len(eq_no) + 1
for lab in re.findall(r'!\[Figure \{fig:(\w+)\}', body):
    if lab in fig_no:
        sys.exit('duplicate figure label ' + lab)
    fig_no[lab] = len(fig_no) + 1

body = re.sub(r'\\quad\(\\#(\w+)\)', lambda m: r'\quad(%d)' % eq_no[m.group(1)], body)
missing = set()
def ref(table, kind):
    def f(m):
        if m.group(1) not in table:
            missing.add(kind + ':' + m.group(1)); return '??'
        return str(table[m.group(1)])
    return f
body = re.sub(r'\{eq:(\w+)\}', ref(eq_no, 'eq'), body)
body = re.sub(r'\{fig:(\w+)\}', ref(fig_no, 'fig'), body)
body = re.sub(r'\{sec:(\w+)\}', ref(sec_no, 'sec'), body)
if missing:
    sys.exit('unresolved: ' + ', '.join(sorted(missing)))

toc = ['```{=openxml}', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>', '```', '', '## Contents', '']
for k, title in enumerate(parts, 1):
    toc += ['::: {custom-style="Contents Part"}', '[%s](#part_%d)' % (title, k), ':::', '']
    for (p, n, t, _) in secs:
        if p == k:
            toc.append('%d.  [%s](#sec_%d)' % (n, t, n))
    toc.append('')
out = meta + '\n\n' + '\n'.join(toc) + body
open(HERE + '/build.md', 'w', encoding='utf-8').write(out)
r = subprocess.run(['pandoc', HERE + '/build.md', '-o', sys.argv[1], '--reference-doc=' + HERE + '/ref.docx',
                    '--resource-path=' + HERE], capture_output=True, text=True)
print(r.stderr.strip()[:2000])
print('sections %d, equations %d, figures %d' % (len(secs), len(eq_no), len(fig_no)))

# Declare the PNG content type, which the reference template lacks.
import zipfile, shutil, os
tmp = sys.argv[1] + '.tmp'
with zipfile.ZipFile(sys.argv[1]) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == '[Content_Types].xml' and b'Extension="png"' not in data:
            data = data.replace(b'<Default Extension="rels"', b'<Default Extension="png" ContentType="image/png"/><Default Extension="rels"', 1)
        zout.writestr(item, data)
shutil.move(tmp, sys.argv[1])

# Every part and section heading must survive as a heading, and every box must stand alone.
with zipfile.ZipFile(sys.argv[1]) as z:
    doc = z.read('word/document.xml').decode('utf-8')
h1, h2 = doc.count('<w:pStyle w:val="Heading1"'), doc.count('<w:pStyle w:val="Heading2"')
boxes = len(re.findall(r'(DEFINITIONS|ASSUMPTIONS)\.', body))
built = doc.count('DEFINITIONS.') + doc.count('ASSUMPTIONS.')
starts = 0
for para in re.findall(r'<w:p>.*?</w:p>', doc, flags=re.S):
    texts = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', para)
    labels = sum(t.count('DEFINITIONS.') + t.count('ASSUMPTIONS.') for t in texts)
    if labels == 0:
        continue
    if labels == 1 and 'w:val="BlockText"' in para and texts[0].strip() in ('DEFINITIONS.', 'ASSUMPTIONS.'):
        starts += 1
    else:
        print('merged or misplaced box:', ''.join(texts)[:120])
print('part headings %d/%d, section headings %d/%d, boxes %d/%d starting their own box' % (h1, len(parts), h2, len(secs) + 2, starts, boxes))
if h1 != len(parts) or h2 != len(secs) + 2 or starts != boxes or built != boxes:
    sys.exit('STRUCTURE CHECK FAILED')
