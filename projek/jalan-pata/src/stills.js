// node stills.js <dir> <outdir>  → one PNG per babak (540×960) from storyboard.json
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [dir, out] = process.argv.slice(2);
const parts = JSON.parse(fs.readFileSync(path.join(dir, 'storyboard.json'), 'utf8'));
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 0.5 });
  await p.goto('file://' + path.join(dir, 'layout.html'));
  await p.evaluate(() => document.fonts.ready);
  for (const P of parts) for (const bb of P.babak) {
    await p.evaluate(([bb, tag]) => window.show(bb, tag), [bb, `${bb.id} · ${bb.t0.toFixed(1)}s`]);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(100);
    const r = await p.evaluate(([bb, tag]) => window.show(bb, tag), [bb, `${bb.id} · ${bb.t0.toFixed(1)}s`]);
    await p.waitForTimeout(150);
    await p.locator('#stage').screenshot({ path: path.join(out, `b${bb.id.split('.')[0]}_${bb.id.split('.')[1].padStart(2, '0')}.png`) });
    if (r.over) console.log('TINGGI', bb.id, r.h);
  }
  await b.close();
})();
