import { execFileSync } from 'node:child_process';
import { readFileSync, existsSync } from 'node:fs';
import path from 'node:path';
const EXPECTED_VERSION='0.39.1', EXPECTED_RPC='https://studio.genlayer.com/api', EXPECTED_CHAIN='61999';
const bin=process.platform==='win32'?path.join('node_modules','.bin','genlayer.cmd'):path.join('node_modules','.bin','genlayer');
function fail(m){console.error('THROTTLE toolchain guard: '+m);process.exit(1)}
if(!existsSync(bin)) fail('local GenLayer CLI missing; run npm install');
const v=execFileSync(bin,['--version'],{encoding:'utf8',shell:process.platform==='win32'}).trim();
if(!v.includes(EXPECTED_VERSION)||/0\.40|rc2/i.test(v)) fail('expected local CLI '+EXPECTED_VERSION+'; got '+v);
const pkg=JSON.parse(readFileSync('package.json','utf8'));
if(pkg?.devDependencies?.genlayer!==EXPECTED_VERSION) fail('package.json must pin genlayer exactly to '+EXPECTED_VERSION);
const cfg=readFileSync('gltest.config.yaml','utf8');
if(!cfg.includes(EXPECTED_RPC)||!cfg.includes('studionet:')||/studio-dev|61997/i.test(cfg)) fail('active config must be stable Studionet only');
console.log('OK: local CLI '+EXPECTED_VERSION);
console.log('OK: Studionet RPC '+EXPECTED_RPC);
console.log('Expected deployment chain ID: '+EXPECTED_CHAIN);
