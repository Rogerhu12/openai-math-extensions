"""Compile paper sources into the build directory."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    '030': ['papers/030-modularity/modularity_cm_totally_real.tex'],
    '159': ['papers/159-szemeredi-exponents/math159_single_exponential.tex'],
    '029': [
        'papers/029-artin-primitive-roots/hecke_zero_free_strip.tex',
        'papers/029-artin-primitive-roots/artin_positive_density.tex',
        'papers/029-artin-primitive-roots/hecke_seven_eighths_all_characters.tex',
    ],
    '172': ['papers/172-euclidean-ramsey/algebraic_spherical_configurations.tex'],
}

def build(relative):
    source = ROOT / relative
    output = ROOT / 'build' / source.parent.name / source.stem
    output.mkdir(parents=True, exist_ok=True)
    for run in range(1, 4):
        result = subprocess.run(['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory', str(output), source.name], cwd=source.parent, capture_output=True)
        (output / ('pass-' + str(run) + '.log')).write_bytes(result.stdout + result.stderr)
        if result.returncode:
            raise RuntimeError('Compilation failed: ' + relative + '; see ' + str(output))
    final_log = (output / (source.stem + '.log')).read_text(encoding='utf-8', errors='replace')
    for error in ['There were undefined references', 'There were multiply-defined labels']:
        if error in final_log:
            raise RuntimeError(error + ': ' + relative)
    print('BUILT ' + str((output / (source.stem + '.pdf')).relative_to(ROOT)), flush=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('families', nargs='*', help='Family numbers; omit for all available sources.')
    args = parser.parse_args()
    if not shutil.which('pdflatex'):
        parser.error('pdflatex is required (TeX Live or MiKTeX).')
    selected = args.families or list(TARGETS)
    if any(f not in TARGETS for f in selected):
        parser.error('Available source families: ' + ', '.join(TARGETS) + '.')
    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(build, [p for f in selected for p in TARGETS[f]]))

if __name__ == '__main__':
    main()
