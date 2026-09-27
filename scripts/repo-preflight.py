from pathlib import Path
import ast,json
R=Path(__file__).resolve().parents[1]
s=(R/'contracts/throttle.py').read_text()
ast.parse(s)
p=json.loads((R/'package.json').read_text())
assert p['devDependencies']['genlayer']=='0.39.1'
c=(R/'gltest.config.yaml').read_text()
assert 'https://studio.genlayer.com/api' in c and 'studio-dev' not in c.lower() and '61997' not in c
for x in ('run_nondet_unsafe','SAME_CLASS','DIFFERENT_CLASS','AMBIGUOUS','class Throttle(gl.Contract)','authorize_operation'):
 assert x in s,x
print('THROTTLE offline preflight: OK')
print('Pinned CLI: 0.39.1')
print('Target network: stable Studionet / 61999')
