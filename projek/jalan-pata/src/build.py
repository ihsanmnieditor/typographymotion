"""Storyboard data for 'Pesanan Jalan Pata' + timing calculator.
Writes storyboard.json (for layout/animation) and storyboard.md (tables for the Fasa 1 report)."""
import json, re, sys

BPM = 120
GRID = 60 / BPM / 2          # 1/8 beat = 0.25s
CAM = 0.5                    # camera move between babak
HOLD = 0.25                  # read-hold after last beat of a babak

# category -> (label, font, colour token, default motion, default sfx)
STY = {
  'asas':    ('Penghubung',          'Inter Medium',             'INK',        'M3 slide-up',               'soft swipe'),
  'asasI':   ('Penghubung',          'Inter Medium Italic',      'INK',        'M3 slide-up',               'soft swipe'),
  'info':    ('Maklumat',            'Inter Black',              None,         'M3 slide-up',               'swipe'),
  'tempat':  ('Tempat',              'Inter Black',              'V-BLUE',     'M2 pop',                    'pop'),
  'santai':  ('Santai / alam',       'Quicksand SemiBold',       'V-CYAN',     'Float naik',                'angin lembut'),
  'nombor':  ('Nombor',              'Bebas Neue',               'V-GREEN',    'M5 scale XL',               'bass hit'),
  'larangan':('Larangan',            'Anton',                    'V-RED',      'M2 pop + pangkah (M9)',     'buzz + pen'),
  'marah':   ('Marah / geram',       'Anton UPPERCASE',          'V-RED',      'Shake + glitch RGB',        'distorted hit'),
  'kunci':   ('Kata kunci',          'Anton UPPERCASE',          'V-VIOLET',   'M5 + blok V-LIME',          'bass hit'),
  'lucu':    ('Lucu',                'Bangers',                  'V-ORANGE',   'Wobble',                    'boing'),
  'soalan':  ('Soalan / sindiran',   'Inter Bold Italic',        'V-VIOLET',   'Condong masuk + ? melantun','bloop'),
  'positif': ('Positif / setuju',    'Inter Black',              'V-GREEN',    'M2 pop + ✓ dilukis',        'ding'),
  'cemas':   ('Cemas / bahaya',      'Special Elite',            'V-VIOLET',   'Jitter / flicker',          'heartbeat'),
  'tenang':  ('Tenang / istighfar',  'Quicksand SemiBold',       'V-CYAN',     'Float perlahan',            'airy chime + muzik low-pass'),
  'terkejut':('Terkejut / brek',     'Rubik Black',              'INK',        'Zoom punch-in + blok V-YELLOW','brek tayar (screech)'),
  'bisikan': ('Petikan / bisikan',   'Inter Light Italic',       'INK 60%',    'Typewriter perlahan',       'tick perlahan'),
}

def B(text, sty, size='S', **kw):
    return dict(text=text, sty=sty, size=size, **kw)

# extras: color, stretch=True (M12), strike, arrow ('L'/'R'), lanes, check, emoji, motion, sfx, upper
PARTS = [
 dict(id=1, title='Bahagian 1/3 — Lane kiri, lane kanan', mood='Nasihat santai → geram', babak=[
  dict(id='1.1', cam='Mula (statik)', lines=[
    [B('Sdkit pesanan', 'info', 'M', color='V-BLUE', motion='M1 typewriter', sfx='tick setiap huruf')],
    [B('untuk', 'asas'), B('kwn²', 'info', 'M', color='V-ORANGE')],
    [B('atau', 'asas'), B('kenalan.', 'info', 'M', color='V-MAGENTA')]]),
  dict(id='1.2', cam='M7 pan ke atas', lines=[
    [B('jln pata', 'tempat', 'M')],
    [B('seb takir', 'tempat', 'M'), B('tuuu,', 'asas', stretch=True)],
    [B('ye', 'asas'), B('2', 'nombor', 'XL', lanes=True, sfx='bass hit + 2 garisan lorong dilukis')],
    [B('lorong', 'nombor', 'M'), B('yee.', 'asas', stretch=True)]]),
  dict(id='1.3', cam='M7 pan ke atas', lines=[
    [B('klau rasa nk', 'asas')],
    [B('santai²', 'santai', 'M')],
    [B('layan', 'asas'), B('angin pata,', 'santai', 'M', emoji='🌊')],
    [B('layan', 'asas'), B('view,', 'santai', 'M')]]),
  dict(id='1.4', cam='M7 pan ke atas', lines=[
    [B('duk je', 'asas')],
    [B('LANE KIRI !!!', 'kunci', 'XL', arrow='L', sfx='bass hit + anak panah ← dilukis')]]),
  dict(id='1.5', cam='M4 whip pan ke KANAN (tukar lorong)', lines=[
    [B('DK SOH', 'larangan', 'M', strike=True)],
    [B('BENG GALOK', 'lucu', 'M')],
    [B('GATAL GELENYAAA', 'lucu', 'M', stretch=True)],
    [B('LAAA NYAAAA', 'info', 'S', color='INK', stretch=True)]]),
  dict(id='1.6', cam='M7 pan ke atas', lines=[
    [B('NK DUK', 'asas')],
    [B('LANE KANAN', 'marah', 'XL', arrow='R')],
    [B('!!!!!!', 'marah', 'M', motion='Pop satu-satu')]]),
  dict(id='1.7', cam='M7 pan ke atas', lines=[
    [B('dk sume org', 'asas'), B('yg lalu situ', 'asas')],
    [B('sbb nk layan', 'asas')],
    [B('angin pata', 'santai', 'M')],
    [B('mcm ge mu !!', 'lucu', 'M', motion='Wobble + kenyit')]]),
  dict(id='1.8', cam='M7 pan ke atas (laju)', lines=[
    [B('ada lgi yg lalu situ', 'asas')],
    [B('sbb nk gi', 'asas'), B('keje,', 'info', 'M', color='V-BLUE')],
    [B('nk gi', 'asas'), B('settle urusan', 'info', 'M', color='V-ORANGE')],
    [B('bandor nung,', 'tempat', 'M')],
    [B('dan sbgainyaaa !!!', 'info', 'S', color='INK', stretch=True)]]),
  dict(id='1.9', cam='M8 rotate 90° (klimaks)', lines=[
    [B('EEEEEEEEEEE', 'marah', 'M', stretch=True, sfx='riser + jeritan sintetik naik')],
    [B('GERAM', 'marah', 'XL', sfx='distorted hit + ducking')],
    [B('LAAAAAA', 'marah', 'M', stretch=True)],
    [B('HAKUUUUUU !!!', 'marah', 'M', stretch=True, sfx='impact + hard cut M11')]]),
 ]),
 dict(id=2, title='Bahagian 2/3 — Guna otok skit', mood='Merayu → marah → serius (nyawa)', babak=[
  dict(id='2.1', cam='Mula (statik)', lines=[
    [B('Pstuuuu', 'info', 'M', color='INK', stretch=True)],
    [B('yg nk', 'asas'), B('ambk gmbr', 'info', 'M', color='V-BLUE', emoji='📸')],
    [B('kt', 'asas'), B('tepi', 'info', 'M', color='V-ORANGE'), B('ke,', 'asas')],
    [B('tgh jalan', 'info', 'M', color='V-ORANGE'), B('ke', 'asas')],
    [B('apa sume tu.', 'asas')]]),
  dict(id='2.2', cam='M7 pan ke atas', lines=[
    [B('MITOKKK', 'marah', 'M', stretch=True, motion='Stretch (M12), tanpa shake')],
    [B('TLG SANGAT', 'info', 'S', color='INK')],
    [B('GUNA OTOK', 'kunci', 'XL')],
    [B('SKIT', 'info', 'M', color='V-VIOLET', emoji='🤏🏻')]]),
  dict(id='2.3', cam='M7 pan ke atas', lines=[
    [B('jgn', 'larangan', 'M', strike=True), B('wk mcm', 'asas')],
    [B('sume', 'asas'), B('kete motor', 'info', 'M', color='V-BLUE')],
    [B('akn', 'asas'), B('brhnti', 'info', 'M', color='V-ORANGE')],
    [B('ke kita untuk tnggu', 'asas')],
    [B('deme sume', 'asas'), B('ambk gmbr !!', 'info', 'M', color='V-BLUE')]]),
  dict(id='2.4', cam='M7 pan ke atas', lines=[
    [B('EHH TLG LAAA !!', 'marah', 'M')],
    [B('ku turun motor,', 'asas')],
    [B('ku debikkkkk', 'lucu', 'M', stretch=True, sfx='boing + "pow" kartun')],
    [B('kang haaa !!', 'lucu', 'M')]]),
  dict(id='2.5', cam='M7 pan ke atas', lines=[
    [B('EEEE', 'marah', 'M', stretch=True)],
    [B('BYK KALI SNGT', 'marah', 'M')],
    [B('EYHHH', 'info', 'S', color='INK', stretch=True)],
    [B('JUPE HK PESENG GNI !!', 'marah', 'M')]]),
  dict(id='2.6', cam='M7 pan ke atas (lebih perlahan)', lines=[
    [B('dk maroh pn', 'positif', 'M')],
    [B('nk', 'asas'), B('ambk gmbr,', 'info', 'M', color='V-BLUE')],
    [B('ambk laaaa.', 'positif', 'M', check=True, stretch=True)]]),
  dict(id='2.7', cam='M7 pan ke atas', lines=[
    [B('tpi', 'kunci', 'M')],
    [B('mntk tlg sngt !!', 'info', 'S', color='INK')],
    [B('syg ke nyawa tek !!', 'soalan', 'M')]]),
  dict(id='2.8', cam='M8 rotate 90° (klimaks)', lines=[
    [B('NYAWAAAAA', 'kunci', 'XL', stretch=True, sfx='riser → bass hit')],
    [B('ORG LAIN', 'kunci', 'M')],
    [B('LAAAA !!', 'marah', 'M', stretch=True)]]),
  dict(id='2.9', cam='M7 pan perlahan; muzik berhenti', lines=[
    [B('sbb klau', 'asas'), B('kena', 'cemas', 'M')],
    [B('tuuu,', 'asas', stretch=True)],
    [B('bkn mu sorang', 'info', 'M', color='V-BLUE')],
    [B('hk', 'asas'), B('boleh sakit !!', 'cemas', 'M', sfx='heartbeat ×2 → senyap')]]),
 ]),
 dict(id=3, title='Bahagian 3/3 — Parking tgh² jalan', mood='Terkejut → istighfar (ironi) → sindir → meletup', babak=[
  dict(id='3.1', cam='Mula (statik)', lines=[
    [B('Pstu', 'asas'), B('orkkk', 'info', 'S', color='INK', stretch=True), B('hk peseng', 'asas')],
    [B('brahi brhnti', 'terkejut', 'M')],
    [B('tghhh jalan !!', 'info', 'M', color='V-ORANGE', stretch=True)]]),
  dict(id='3.2', cam='M7 pan ke atas', lines=[
    [B('lgi²', 'asas'), B('kt', 'asas')],
    [B('kg cina', 'tempat', 'M'), B('nuh.', 'asas')]]),
  dict(id='3.3', cam='M7 pan perlahan; muzik low-pass', lines=[
    [B('ASTAGHFIRULLAH', 'tenang', 'M')]]),
  dict(id='3.4', cam='M7 pan ke atas', lines=[
    [B('supoh kata', 'asas'), B('klau lalu situ', 'asas')],
    [B('mmg boleh', 'asas'), B('pahala', 'positif', 'M')],
    [B('istighfar,', 'tenang', 'M')],
    [B('zikir aje', 'tenang', 'M', emoji='😭')]]),
  dict(id='3.5', cam='M7 pan ke atas; muzik masuk semula', lines=[
    [B('demi', 'asas'), B('gmbr', 'info', 'M', color='V-BLUE'), B('org kata,', 'asas')],
    [B('mu boleh orkk', 'asas')],
    [B('PARKING', 'kunci', 'XL')],
    [B('TGH² JALAN !!', 'kunci', 'M')]]),
  dict(id='3.6', cam='M7 pan ke atas', lines=[
    [B('mu napok dkkk', 'soalan', 'M', stretch=True)],
    [B('jalan tu', 'asas'), B('sempit', 'info', 'M', color='V-ORANGE', motion='Huruf dihimpit (squeeze)', sfx='squeak')],
    [B('stare mana !!', 'soalan', 'M')]]),
  dict(id='3.7', cam='M7 pan ke atas', lines=[
    [B('org sini plok', 'asas')],
    [B('kete bapok²', 'info', 'M', color='V-BLUE')],
    [B('gong blake !!', 'info', 'XL', color='V-ORANGE', motion='Membesar (scale 0.5→1.15→1)', sfx='thump besar')]]),
  dict(id='3.8', cam='M7 pan ke atas', lines=[
    [B('ALLAHUUU,', 'tenang', 'M', stretch=True)],
    [B('rasa nk gi', 'asas'), B('jek', 'lucu', 'M', sfx='hentakan kaki (stomp)')],
    [B('atas tekok', 'lucu', 'M')],
    [B('sorang².', 'asas')]]),
  dict(id='3.9', cam='M7 pan ke atas', lines=[
    [B('phtu bila org', 'asas'), B('tegur,', 'info', 'M', color='V-BLUE')],
    [B('“jp eyhh jp eyh”.', 'bisikan', 'M')]]),
  dict(id='3.10', cam='M7 pan ke atas', lines=[
    [B('eeee rasa nk', 'asas', stretch=True)],
    [B('jek skali !!', 'lucu', 'M', sfx='stomp ×2')],
    [B('kita plok nk kne', 'asas')],
    [B('tunggu ye !!', 'info', 'M', color='V-MAGENTA', motion='Huruf muncul sangat perlahan (menunggu)', sfx='jam berdetik')]]),
  dict(id='3.11', cam='M7 pan ke atas', lines=[
    [B('pstu hk jenis napok', 'asas')],
    [B('port ambk gmbr', 'info', 'M', color='V-BLUE'), B('skit,', 'asas')],
    [B('papppp', 'terkejut', 'M', stretch=True)],
    [B('berhenti !!', 'terkejut', 'M')]]),
  dict(id='3.12', cam='M7 pan ke atas (laju, 3 soalan)', lines=[
    [B('signal', 'info', 'M', color='V-ORANGE', motion='Berkelip macam lampu signal ×2', sfx='tik-tok signal')],
    [B('kete mu', 'asas'), B('haus ke ?', 'soalan', 'M')],
    [B('side mirror', 'info', 'M', color='V-BLUE', motion='Terbalik cermin → normal (flip)', sfx='swish')],
    [B('mu', 'asas'), B('patoh ke ?', 'soalan', 'M')],
    [B('pah dk napok', 'asas'), B('org alik lakang', 'info', 'S', color='V-BLUE', motion='Muncul dari belakang (scale 0.3→1)')],
    [B('ni ada ke dk ?', 'soalan', 'M')]]),
  dict(id='3.13', cam='M8 rotate 90° (klimaks akhir)', lines=[
    [B('EEE', 'marah', 'M', stretch=True)],
    [B('JEK SKALI', 'marah', 'XL', sfx='stomp + distorted hit')],
    [B('BRU TAU !!', 'marah', 'M', sfx='impact + hard cut M11')]]),
 ]),
]

def letters(s):
    return len(re.sub(r'[^A-Za-z0-9²]', '', s))

def snap(x):
    return round(x / GRID) * GRID

def dur(b):
    n = letters(b['text'])
    d = 0.2 + 0.035 * n
    if b['sty'] in ('tenang', 'bisikan'): d = max(d * 1.4, 0.75)
    if b['sty'] == 'cemas': d = max(d, 0.5)
    if b.get('stretch'): d += 0.25
    if b['size'] == 'XL': d = max(d, 0.75)
    if b['sty'] == 'asas': d = min(d, 0.5)
    return max(GRID, min(1.25, snap(d)))

def build():
    out = []
    for P in PARTS:
        t = 0.25
        emo = 0
        for bb in P['babak']:
            bb['t0'] = round(t, 2)
            for line in bb['lines']:
                for b in line:
                    lab, font, col, mot, sfx = STY[b['sty']]
                    b['t'] = round(t, 2)
                    b['d'] = dur(b)
                    b['cat'] = lab
                    b['font'] = font
                    b['col'] = b.get('color') or col
                    b['motion'] = b.get('motion') or (mot + (' + Stretch M12' if b.get('stretch') else ''))
                    b['sfx'] = b.get('sfx') or sfx
                    if b.get('emoji'): emo += 1
                    t += b['d']
            t += HOLD
            bb['t1'] = round(t, 2)
            t += CAM
        P['dur'] = round(t - CAM + 0.7, 2)   # + end card / hard cut tail
        P['emoji'] = emo
        out.append(P)
    return out

def md(parts):
    o = []
    for P in parts:
        o.append(f"### {P['title']}  ·  {P['dur']:.1f}s  ·  emoji: {P['emoji']}\n")
        o.append('| Babak | Masa (s) | Teks | Kategori | Saiz | Font | Warna | Motion | SFX | Emoji |')
        o.append('|---|---|---|---|---|---|---|---|---|---|')
        for bb in P['babak']:
            o.append(f"| **{bb['id']}** | {bb['t0']:.2f} | — | — | — | — | — | *Kamera: {bb['cam']}* | — | — |")
            for line in bb['lines']:
                for b in line:
                    if b['sty'] == 'asas':
                        o.append(f"| | {b['t']:.2f} | {b['text']} | Penghubung | S | Inter | INK | M3 | — | — |")
                        continue
                    extra = []
                    if b.get('strike'): extra.append('pangkah')
                    if b.get('arrow'): extra.append('anak panah ' + ('←' if b['arrow'] == 'L' else '→'))
                    if b.get('lanes'): extra.append('2 garisan lorong')
                    if b.get('check'): extra.append('✓')
                    mot = b['motion'] + (' · ' + ', '.join(extra) if extra else '')
                    o.append(f"| | {b['t']:.2f} | {b['text']} | {b['cat']} | {b['size']} | {b['font']} | {b['col']} | {mot} | {b['sfx']} | {b.get('emoji','—')} |")
        o.append('')
    return '\n'.join(o)

if __name__ == '__main__':
    parts = build()
    d = sys.argv[1]
    json.dump(parts, open(f'{d}/storyboard.json', 'w'), ensure_ascii=False, indent=1)
    open(f'{d}/storyboard.md', 'w').write(md(parts))
    for P in parts:
        print(P['id'], P['dur'], 'emoji', P['emoji'], 'babak', len(P['babak']))
