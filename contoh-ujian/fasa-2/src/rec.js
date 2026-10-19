// usage: node rec.js <dir> <outdir> <scale> [times...]  (no times → all frames 30fps, 12.6s)
const { chromium } = require('playwright');
const path = require('path');
const [dir, out, scale, ...times] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: +scale });
  await p.goto('file://' + path.join(dir, 'anim.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  const list = times.length ? times.map(Number) : [...Array(378).keys()].map(i => i / 30);
  let i = 0;
  for (const t of list) {
    await p.evaluate(t => window.render(t), t);
    const name = times.length ? `t_${t.toFixed(2)}.png` : `f${String(i).padStart(4, '0')}.png`;
    await p.screenshot({ path: path.join(out, name), type: 'png' });
    i++;
  }
  await b.close();
})();
