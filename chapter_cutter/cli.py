import argparse
import os
from chapter_cutter.core import split_file, merge_folder

def cmd_split(args):
    for path in args.paths:
        if not os.path.isfile(path):
            print(f"Skipping non-file: {path}")
            continue
        out_dir = args.out or None
        files = split_file(path, lang=args.lang, out_dir=out_dir)
        print(f"Wrote {len(files)} chapters to: {os.path.dirname(files[0]) if files else out_dir}")

def cmd_merge(args):
    input_folder = args.folder
    if not os.path.isdir(input_folder):
        print(f"Not a folder: {input_folder}")
        return
    out = merge_folder(input_folder, output_file=args.out)
    print(f"Merged into: {out}")

def main():
    parser = argparse.ArgumentParser(prog='chapter_cutter')
    sub = parser.add_subparsers(dest='cmd')

    p_split = sub.add_parser('split')
    p_split.add_argument('paths', nargs='+', help='Input txt file(s)')
    p_split.add_argument('--lang', default='Spanish', help='Target language (Spanish, English, French, German, Italian, Portuguese, Russian, Chinese, Japanese)')
    p_split.add_argument('--out', help='Output directory (optional)')
    p_split.set_defaults(func=cmd_split)

    p_merge = sub.add_parser('merge')
    p_merge.add_argument('folder', help='Folder with numbered chapter .txt files')
    p_merge.add_argument('--out', help='Output merged filename (optional)')
    p_merge.set_defaults(func=cmd_merge)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        return
    args.func(args)

if __name__ == '__main__':
    main()
