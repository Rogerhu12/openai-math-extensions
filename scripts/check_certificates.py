"""Run the collected finite certificates and compare their recorded outputs."""
import argparse
from pathlib import Path
import subprocess
import sys
import json

ROOT = Path(__file__).resolve().parents[1]
JOBS = [
    ('029-artin-primitive-roots', 'hecke_double_sparse_endpoint_certificate.py', 'hecke_double_sparse_endpoint_certificate_results.txt'),
]

def normalize(value):
    return '\n'.join(line.rstrip() for line in value.splitlines()).strip()

def check(job):
    family, name, expected_name = job
    directory = ROOT / 'papers' / family / 'certificates'
    result = subprocess.run([sys.executable, '-X', 'utf8', name], cwd=directory, capture_output=True, text=True, encoding='utf-8', timeout=900)
    target = ROOT / 'build' / 'certificates' / name.replace('.py', '.txt')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(result.stdout + result.stderr, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(name + ' failed; see ' + str(target))
    expected = (directory / expected_name).read_text(encoding='utf-8')
    same = normalize(expected) == normalize(result.stdout)
    print(('PASS ' if same else 'OUTPUT DIFF ') + name, flush=True)
    return {'script': (directory / name).relative_to(ROOT).as_posix(), 'assertions_passed': True, 'recorded_output_matches': same}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--family', choices=['029'])
    args = parser.parse_args()
    jobs = [j for j in JOBS if args.family is None or j[0].startswith(args.family)]
    results = [check(job) for job in jobs]
    (ROOT / 'build/certificate-summary.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    if not all(r['recorded_output_matches'] for r in results):
        raise SystemExit('Assertions passed, but recorded output differences require review.')

if __name__ == '__main__':
    main()
