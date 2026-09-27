import { execFileSync } from 'node:child_process'; import { existsSync } from 'node:fs'; import path from 'node:path';
const V='0.39.1', RPC='https://studio.genlayer.com/api', CHAIN='61999';
const bin=process.platform==='win32'?path.join('node_modules','.bin','genlayer.cmd'):path.join('node_modules','.bin','genlayer');
const o={shell:process.platform==='win32'};
function fail(m){console.error('THROTTLE deploy guard: '+m);process.exit(1)}
if(!existsSync(bin)) fail('run npm install first');
const v=execFileSync(bin,['--version'],{encoding:'utf8',...o}).trim();
if(!v.includes(V)||/0\.40|rc2/i.test(v)) fail('refusing deployment with '+v);
execFileSync(bin,['network','set','studionet'],{stdio:'inherit',...o});
const info=execFileSync(bin,['network','info'],{encoding:'utf8',...o}); console.log(info);
if(!info.includes(CHAIN)||!info.includes('studio.genlayer.com')) fail('network info did not prove stable Studionet '+CHAIN);
execFileSync(bin,['deploy','--contract','contracts/throttle.py','--rpc',RPC],{stdio:'inherit',...o});
