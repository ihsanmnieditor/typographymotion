"""Cartoon/fun music (120 BPM, C major) + SFX driven by storyboard.json.
usage: python3 audio.py <dir> <part> → <dir>/mix<part>.wav"""
import json, re, sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
BEAT = 0.5
rng = np.random.default_rng(11)


def t_(d): return np.arange(int(SR * d)) / SR
def hz(n): return 440 * 2 ** ((n - 69) / 12)
def lp(x, f): return sosfilt(butter(2, f, 'low', fs=SR, output='sos'), x)
def hp(x, f): return sosfilt(butter(2, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)
def noise(d): return rng.standard_normal(int(SR * d))
def sweep(f0, f1, d, curve='exp'):
    tt = t_(d)
    f = f0 * (f1 / f0) ** (tt / d) if curve == 'exp' else f0 + (f1 - f0) * tt / d
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def env(n, a=0.003, dec=0.3):
    e = np.exp(-np.arange(n) / SR / dec)
    k = int(a * SR)
    if k: e[:k] *= np.linspace(0, 1, k)
    return e


def add(buf, sig, at, db=0.0):
    i = int(round(at * SR))
    if i < 0: sig, i = sig[-i:], 0
    if i >= len(buf): return
    sig = sig[:len(buf) - i]
    buf[i:i + len(sig)] += sig * 10 ** (db / 20)


# ---------------- instruments ----------------
def marimba(n, d=0.5):
    tt = t_(max(d, 0.35)); f = hz(n)
    s = np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(2 * np.pi * f * 4 * tt) * np.exp(-tt / 0.03)
    return s * env(len(tt), 0.002, 0.22) * 0.5

def glock(n, d=0.8):
    tt = t_(d); f = hz(n)
    s = sum(a * np.sin(2 * np.pi * f * r * tt) for a, r in [(1, 1), (0.4, 2.76), (0.2, 5.4)])
    return s * env(len(tt), 0.001, 0.35) * 0.3

def tuba(n, d=0.3):
    tt = t_(d)
    s = np.tanh(1.8 * np.sin(2 * np.pi * hz(n) * tt))
    e = np.minimum(1, tt / 0.01) * np.exp(-tt / 0.18)
    return lp(s * e, 900) * 0.55

def stab(notes, d=0.16):
    tt = t_(d)
    s = sum(np.sin(2 * np.pi * hz(n) * tt) + 0.4 * np.sin(2 * np.pi * hz(n) * 2 * tt) for n in notes)
    return s * env(len(tt), 0.002, 0.07) * 0.12

def kick():
    tt = t_(0.3); f = 50 + 120 * np.exp(-tt * 35)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.001, 0.1) * 0.8

def snare():
    n = noise(0.18)
    tt = t_(0.18)
    return (bp(n, 1500, 6000) * 0.6 + np.sin(2 * np.pi * 190 * tt) * 0.5) * env(len(n), 0.001, 0.05) * 0.5

def shaker():
    n = noise(0.05); return hp(n, 6000) * env(len(n), 0.004, 0.012) * 0.25

def crash():
    n = noise(1.5); return hp(n, 4000) * env(len(n), 0.002, 0.45) * 0.3


MEL = [[(76, .5), (79, .5), (84, .5), (79, .5), (81, 1), (79, 1)],
       [(77, .5), (81, .5), (84, 1), (81, .5), (77, .5), (79, 1)],
       [(74, .5), (79, .5), (83, .5), (86, .5), (84, 1), (83, 1)],
       [(84, 1.5), (79, .5), (76, 1), (None, 1)],
       [(76, .5), (81, .5), (84, .5), (81, .5), (76, 1), (None, 1)],
       [(77, .5), (81, .5), (84, .5), (86, .5), (84, 1), (81, 1)],
       [(79, .5), (83, .5), (86, .5), (83, .5), (79, .5), (81, .5), (83, 1)],
       [(84, 2), (None, 2)]]
CH = [([60, 64, 67], 48), ([60, 65, 69], 41), ([59, 62, 67], 43), ([60, 64, 67], 48),
      ([57, 60, 64], 45), ([60, 65, 69], 41), ([59, 62, 67], 43), ([60, 64, 67], 48)]


def music(dur, climax_ts):
    out = np.zeros(int(SR * dur))
    bar = 4 * BEAT
    nb = int(np.ceil(dur / bar))
    for i in range(nb):
        t0 = i * bar
        ch, root = CH[i % 8]
        for b in range(4):
            tb = t0 + b * BEAT
            if b % 2 == 0:
                add(out, tuba(root if b == 0 else root - 5), tb, -2)
                add(out, kick(), tb, -4)
            else:
                add(out, stab(ch), tb, -2)
                add(out, snare(), tb, -12)
            for h in range(2):
                add(out, shaker(), tb + h * BEAT / 2, -8 if h else -12)
        tm = t0
        for n, d in MEL[i % 8]:
            if n: add(out, marimba(n, d * BEAT), tm, -5)
            tm += d * BEAT
        if i % 4 == 3:  # sparkle at phrase end
            for k, n in enumerate([84, 88, 91]):
                add(out, glock(n), t0 + 3 * BEAT + k * 0.12, -16)
    for tc in climax_ts:  # drum fill + crash into each climax
        for k in range(8):
            add(out, snare(), tc - 1.0 + k * 0.125, -14 + k)
        add(out, crash(), tc, -4)
        add(out, kick(), tc, 0)
    return out


# ---------------- SFX ----------------
def swipe(d=.18, lo=1500, hi=5000):
    n = noise(d); x = np.linspace(0, 1, len(n))
    return bp(n, lo, hi) * np.sin(np.pi * x) ** 2 * 0.3

def whoosh(d=.5):
    n = noise(d); x = np.linspace(0, 1, len(n)); out = np.zeros_like(n)
    for i, (lo, hi) in enumerate([(300, 900), (700, 2000), (1500, 4500), (700, 2000)]):
        out += bp(n, lo, hi) * np.exp(-((x - i / 3) ** 2) / 0.03)
    return out * np.sin(np.pi * x) * 0.6

def tick(): n = noise(.02); return hp(n, 3000) * env(len(n), .0005, .004) * .6
def tock(): tt = t_(.05); return np.sin(2 * np.pi * 900 * tt) * env(len(tt), .0005, .01) * .4
def pop(): tt = t_(.08); return sweep(900, 250, .08) * env(len(tt), .001, .03) * .5
def bloop(): tt = t_(.16); return sweep(300, 1000, .16) * np.sin(np.pi * tt / .16) * .35
def ding(): return glock(96, 1.0) * 1.6
def chime():
    o = np.zeros(int(SR * 1.5))
    for k, n in enumerate([84, 88, 91, 96]): add(o, glock(n, 1.2), k * .08)
    return o
def wind(d=.9):
    n = noise(d); x = np.linspace(0, 1, len(n)); return bp(n, 400, 1500) * np.sin(np.pi * x) * .35
def buzz(): tt = t_(.25); return lp(np.sign(np.sin(2 * np.pi * 110 * tt)), 1500) * env(len(tt), .003, .15) * .3
def scribble(d=.35):
    n = noise(d); tt = t_(d); return bp(n, 2500, 6000) * (.5 + .5 * np.abs(np.sin(2 * np.pi * 9 * tt))) * np.sin(np.pi * tt / d) * .2
def bass_hit():
    tt = t_(.8); f = 40 + 90 * np.exp(-tt * 12)
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), .001, .35) + hp(noise(.8), 2000) * env(len(tt), .0005, .01) * .3) * .9
def dist_hit():
    return np.tanh(3 * (bass_hit() + hp(noise(.8), 1000) * env(int(SR * .8), .001, .08) * .5)) * .6
def boing(d=.45):
    tt = t_(d); f = 220 * (1 + .35 * np.sin(2 * np.pi * 14 * tt) * np.exp(-tt * 5)) * (1 + tt)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), .002, .2) * .5
def pow_():
    return (hp(noise(.25), 800) * env(int(SR * .25), .001, .04) * .6 + bass_hit()[:int(SR * .25)] * .7)
def stomp():
    tt = t_(.35); f = 45 + 70 * np.exp(-tt * 25)
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), .001, .12) + lp(noise(.35), 400) * env(len(tt), .001, .04)) * .9
def heartbeat():
    o = np.zeros(int(SR * .7))
    for at, g in [(0, 1), (.22, .7)]:
        tt = t_(.25); add(o, np.sin(2 * np.pi * 55 * tt) * env(len(tt), .005, .07) * g, at)
    return o * 1.2
def screech(d=.7):
    tt = t_(d); f = 2400 + 200 * np.sin(2 * np.pi * 30 * tt) - 600 * tt / d
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * .25 + bp(noise(d), 2000, 5000) * .3
    return s * np.minimum(1, tt / .02) * np.exp(-tt / (d * .6))
def squeak(): tt = t_(.18); return sweep(1200, 2600, .18) * np.sin(np.pi * tt / .18) * .25
def big_thump(): return stomp() * 1.2
def swish(): return swipe(.25, 2000, 7000)
def slide_whistle(d, up=True):
    tt = t_(d); f0, f1 = (500, 1600) if up else (1600, 500)
    f = f0 + (f1 - f0) * (tt / d) ** .8
    return np.sin(2 * np.pi * np.cumsum(f * (1 + .01 * np.sin(2 * np.pi * 6 * tt))) / SR) * np.minimum(1, tt / .03) * np.minimum(1, (d - tt) / .05) * .22
def riser(d=.5):
    tt = t_(d); return (sweep(200, 1400, d) * .15 + hp(noise(d), 2000) * .15) * (tt / d) ** 2
def impact(): return dist_hit()
def tada():
    o = np.zeros(int(SR * 1.6))
    for k, n in enumerate([72, 76, 79, 84]): add(o, marimba(n, .3), k * .07, -2)
    add(o, stab([72, 76, 79, 84], .5) * 2.5, .3)
    add(o, glock(96, 1.2), .3, -4)
    return o


def beat_sfx(sfx, b, buf, duck):
    t, d, s = b['t'], b['d'], b['sfx']
    def A(sig, at, db=0): add(buf, sig, at, db)
    if b['sty'] == 'asas' and not b.get('stretch'): return
    if 'tick setiap huruf' in s:
        n = len(b['text']); [A(tick(), t + i * d * .85 / n, -12) for i in range(n)]
    elif b['sty'] == 'bisikan':
        n = len(b['text']); [A(tick(), t + i * d * .85 / n, -20) for i in range(0, n, 2)]
    if 'riser' in s: A(riser(.5), t - .5, -6)
    if 'jeritan' in s: A(slide_whistle(max(d, .5)), t, -4)
    if 'bass hit' in s: A(bass_hit(), t, -2); duck.append((t, .5))
    if 'garisan lorong' in s: A(scribble(.4), t + .15, -10)
    if 'buzz' in s: A(buzz(), t, -10)
    if 'pen' in s: A(scribble(), t + .25, -8)
    if 'distorted' in s or 'impact' in s: A(dist_hit(), t, -3); duck.append((t, .5))
    if 'boing' in s: A(boing(), t, -6)
    if 'pow' in s: A(pow_(), t + .2, -6)
    if s == 'bloop': A(bloop(), t + .2, -8)
    if s == 'ding': A(ding(), t + .2, -6); A(scribble(.25), t + .15, -14)
    if 'heartbeat' in s: A(heartbeat(), t, 0); A(heartbeat(), t + .8, -2) if '×2' in s else None
    if 'airy chime' in s: A(chime(), t, -6)
    if 'angin' in s: A(wind(), t, -10)
    if 'brek' in s: A(screech(), t, -6)
    if s == 'pop': A(pop(), t, -8)
    if s in ('swipe', 'soft swipe'): A(swipe(), t, -16)
    if 'stomp' in s:
        A(stomp(), t, -2)
        if '×2' in s: A(stomp(), t + .25, -4)
    if 'squeak' in s: A(squeak(), t + .1, -8)
    if 'thump besar' in s: A(big_thump(), t, -2)
    if 'tik-tok' in s: [A(tock() if i % 2 else tick(), t + i * .12, -8) for i in range(4)]
    if 'swish' in s: A(swish(), t, -10)
    if 'jam berdetik' in s: [A(tock() if i % 2 else tick(), t + i * .25, -10) for i in range(int(d / .25) + 2)]
    if b.get('stretch') and 'jeritan' not in s: A(slide_whistle(max(min(d, .8), .3)), t, -12)


def build(part, final=True):
    dur = part['dur']; N = int(SR * dur)
    climaxes = [bb['t0'] for bb in part['babak'] if 'M8' in bb['cam']]
    mus = music(dur, climaxes)
    # low-pass regions (istighfar) and silence (music stops)
    lpm = np.zeros(N); mute = np.ones(N)
    bks = part['babak']
    for i, bb in enumerate(bks):
        if 'low-pass' in bb['cam']:
            end = next((x['t0'] - .5 for x in bks[i + 1:] if 'masuk semula' in x['cam']), bb['t1'])
            lpm[int((bb['t0'] - .5) * SR):int(end * SR)] = 1
        if 'berhenti' in bb['cam']:
            mute[int((bb['t0'] - .5) * SR):] = 0
        for line in bb['lines']:
            for b in line:
                if b['sty'] == 'tenang': lpm[int(b['t'] * SR):int((b['t'] + b['d'] + .3) * SR)] = 1
    sm = np.ones(2400) / 2400
    lpm = np.convolve(lpm, sm, 'same'); mute = np.convolve(mute, sm, 'same')
    mus = (mus * (1 - lpm) + lp(mus, 500) * lpm * .6) * mute
    cta = part['cta']
    mus[int((cta - .1) * SR):] = 0           # hard cut silence
    sfx = np.zeros(N); duck = []
    for i, bb in enumerate(bks):
        if i:
            ct = bb['t0'] - .5
            ty = 'rot' if 'M8' in bb['cam'] else 'h' if 'KANAN' in bb['cam'] else 'v'
            add(sfx, whoosh() if ty != 'v' else swipe(.35, 800, 3000), ct, -6 if ty != 'v' else -16)
        for line in bb['lines']:
            for b in line:
                beat_sfx(sfx, b, sfx, duck)
    if final:
        add(sfx, tada() if 'berhenti' not in ''.join(x['cam'] for x in bks) else glock(84, 1.4), cta + .1, -2)
    dk = np.ones(N)
    for t, d in duck: dk[int(t * SR):int((t + d) * SR)] = 10 ** (-4 / 20)
    dk = np.convolve(dk, sm, 'same')
    mix = mus * dk * 0.8 + sfx
    f = np.ones(N); k = int(.25 * SR); f[-k:] = np.linspace(1, 0, k)
    if final: mix *= f
    return mix


if __name__ == '__main__':
    d, pid = sys.argv[1], int(sys.argv[2])
    parts = json.load(open(f'{d}/storyboard.json'))
    if pid == 0:   # gabung: each part at its offset, hard cut between, @handle sting only at the end
        G = json.load(open(f'{d}/storyboard_gabung.json'))[0]
        m = np.zeros(int(SR * G['dur']))
        for i, (P, off) in enumerate(zip(parts, G['offsets'])):
            add(m, build(P, final=(i == len(parts) - 1)), off)
    else:
        m = build(next(p for p in parts if p['id'] == pid))
    m = m / (np.max(np.abs(m)) * 1.05)
    wavfile.write(f'{d}/mix{pid}.wav', SR, np.stack([m, m], 1).astype(np.float32))
    print('ok', pid, len(m) / SR)
