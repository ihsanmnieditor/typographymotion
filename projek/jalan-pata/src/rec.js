// node rec.js <dir> <part 1-3> <outdir> <scale> [times...]   no times → every frame @30fps
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [dir, partId, out, scale, ...times] = process.argv.slice(2);
const part = JSON.parse(fs.readFileSync(path.join(dir, process.env.SB || 'storyboard.json'), 'utf8')).find(p => p.id == partId);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: +scale });
  await p.goto('file://' + path.join(dir, 'anim.html'));
  await p.evaluate(part => window.build(part), part);
  // warm every font (layout is measured after they load)
  await p.evaluate(() => { document.querySelectorAll('.b').forEach(e => e.style.opacity = 1); });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  await p.evaluate(() => window.fit());
  const list = times.length ? times.map(Number) : [...Array(Math.round(part.dur * 30)).keys()].map(i => i / 30);
  let i = 0;
  for (const t of list) {
    await p.evaluate(t => window.render(t), t);
    const name = times.length ? `t_${String(t.toFixed(2)).padStart(6, '0')}.png` : `f${String(i).padStart(5, '0')}.png`;
    await p.screenshot({ path: path.join(out, name) });
    i++;
  }
  await b.close();
})();
