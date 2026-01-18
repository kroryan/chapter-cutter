import os
import re
from .patterns import get_patterns

def find_chapter_line_indices(lines, patterns):
    indices = []
    for i, line in enumerate(lines):
        for pat in patterns:
            if pat.search(line):
                indices.append(i)
                break
    return indices

def split_text_into_chapters(text, patterns):
    lines = text.splitlines()
    starts = find_chapter_line_indices(lines, patterns)
    if not starts:
        # fallback: try English 'chapter' or split into fixed-size chunks (not ideal)
        return [text]

    chapters = []
    starts.append(len(lines))
    for a, b in zip(starts, starts[1:]):
        chunk = '\n'.join(lines[a:b]).strip()
        if chunk:
            chapters.append(chunk)
    return chapters

def split_file(path, lang=None, out_dir=None):
    base = os.path.basename(path)
    name, _ = os.path.splitext(base)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    patterns = get_patterns(lang)
    chapters = split_text_into_chapters(text, patterns)

    if not out_dir:
        out_dir = os.path.join(os.path.dirname(path), name)
    os.makedirs(out_dir, exist_ok=True)

    width = max(2, len(str(len(chapters))))
    out_files = []
    for idx, ch in enumerate(chapters, start=1):
        fname = f"{idx:0{width}d}.txt"
        out_path = os.path.join(out_dir, fname)
        with open(out_path, 'w', encoding='utf-8') as wf:
            wf.write(ch + '\n')
        out_files.append(out_path)

    return out_files

def merge_folder(folder_path, output_file=None):
    txts = [p for p in os.listdir(folder_path) if p.lower().endswith('.txt')]
    # sort by numeric prefix if possible
    def sort_key(n):
        try:
            return int(os.path.splitext(n)[0])
        except Exception:
            return n

    txts.sort(key=sort_key)
    if not output_file:
        output_file = os.path.join(os.path.dirname(folder_path), os.path.basename(folder_path) + '_merged.txt')

    with open(output_file, 'w', encoding='utf-8') as wf:
        for i, name in enumerate(txts):
            p = os.path.join(folder_path, name)
            with open(p, 'r', encoding='utf-8', errors='ignore') as rf:
                data = rf.read().rstrip()
            wf.write(data)
            if i != len(txts) - 1:
                wf.write('\n\n')

    return output_file
