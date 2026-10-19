"""Synthesised music (100 BPM) + SFX for the Fasa 2 preview. Writes music.wav, sfx.wav, mix.wav."""
import sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
DUR = 12.6
N = int(SR * DUR)
BEAT = 0.6
rng = np.random.default_rng(7)


def t_(d):
    return np.arange(int(SR * d)) / SR


def add(buf, sig, at, gain_db=0.0):
    i = int(at * SR)
    if i >= len(buf):
        return
    sig = sig[: len(buf) - i]
    buf[i:i + len(sig)] += sig * 10 ** (gain_db / 20)


def lp(x, f):
    return sosfilt(butter(2, f, 'low', fs=SR, output='sos'), x)


def hp(x, f):
    return sosfilt(butter(2, f, 'high', fs=SR, output='sos'), x)


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)


def env(n, a=0.005, decay=1.0):
    tt = np.arange(n) / SR
    e = np.exp(-tt / decay)
    k = int(a * SR)
    if k:
        e[:k] *= np.linspace(0, 1, k)
    return e


def hz(note):  # midi -> Hz
    return 440 * 2 ** ((note - 69) / 12)


def piano(note, d=2.0, decay=0.9):
    tt = t_(d)
    f = hz(note)
    s = sum((0.6 ** h) * np.sin(2 * np.pi * f * (h + 1) * tt * (1 + 0.0004 * h)) for h in range(6))
    return s * env(len(tt), 0.004, decay) * 0.25


def pad(notes, d):
    tt = t_(d)
    s = sum(np.sin(2 * np.pi * hz(n) * tt) + 0.3 * np.sin(2 * np.pi * hz(n) * 2.003 * tt) for n in notes)
    e = np.minimum(1, tt / 0.3) * np.minimum(1, (d - tt) / 0.3)
    return lp(s * e, 1800) * 0.06


def kick():
    tt = t_(0.35)
    f = 50 + 110 * np.exp(-tt * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.001, 0.12) * 0.9


def clap():
    n = rng.standard_normal(int(SR * 0.2))
    return bp(n, 900, 4000) * env(len(n), 0.001, 0.05) * 0.5


def hat():
    n = rng.standard_normal(int(SR * 0.06))
    return hp(n, 7000) * env(len(n), 0.001, 0.015) * 0.25


def bass(note, d):
    tt = t_(d)
    s = np.tanh(2 * np.sin(2 * np.pi * hz(note) * tt))
    return lp(s, 600) * env(len(tt), 0.005, d * 0.8) * 0.35


def stab(notes, d=0.25):
    tt = t_(d)
    s = sum(np.sign(np.sin(2 * np.pi * hz(n) * tt)) * 0.5 + np.sin(2 * np.pi * hz(n) * tt) for n in notes)
    return lp(s, 2500) * env(len(tt), 0.003, 0.1) * 0.05


# ---------------- music ----------------
music = np.zeros(N)
Am, F, C, G = [57, 60, 64], [53, 57, 60], [55, 60, 64], [55, 59, 62]
# intro 0–5.33: sad piano, filtered
intro = np.zeros(N)
for at, ch in [(0.0, Am), (2.4, F)]:
    add(intro, pad(ch, 2.4), at)
    for k, n in enumerate(ch + [ch[0] + 12]):
        add(intro, piano(n, 2.0, 0.8), at + k * BEAT * 0.5, -4)
    add(intro, piano(ch[0] - 12, 2.4, 1.2), at, -2)
add(intro, pad(Am, 0.55), 4.8)
intro = lp(intro, 2200)
intro[int(5.333 * SR):] = 0  # 2-frame silence before drop
music += intro
# drop 5.4–11.4: upbeat
prog = [(C, 48), (G, 43), (Am, 45), (F, 41), (C, 48)]
for bar, (ch, root) in enumerate(prog):
    t0 = 5.4 + bar * 1.2
    add(music, pad([n + 12 for n in ch], 1.2), t0, -2)
    for b in range(2):
        tb = t0 + b * BEAT
        add(music, kick(), tb)
        add(music, bass(root, BEAT * 0.9), tb, -1)
        add(music, stab([n + 12 for n in ch]), tb + BEAT / 2)
        if b == 1:
            add(music, clap(), tb, -3)
        for h in range(4):
            add(music, hat(), tb + h * BEAT / 4, -2 if h % 2 else -6)
music[int(11.4 * SR):] = 0
# outro chord 11.5–12.6
add(music, pad([60, 64, 67, 72], 1.1), 11.5, 2)
add(music, piano(48, 1.1, 0.6), 11.5)

# ---------------- SFX ----------------
sfx = np.zeros(N)


def swipe(d=0.18, lo=1500, hi=5000):
    n = rng.standard_normal(int(SR * d))
    tt = np.arange(len(n)) / len(n)
    return bp(n, lo, hi) * np.sin(np.pi * tt) ** 2 * 0.25


def whoosh(d=0.45):
    n = rng.standard_normal(int(SR * d))
    tt = np.arange(len(n)) / len(n)
    out = np.zeros_like(n)
    for i, (lo, hi) in enumerate([(300, 900), (700, 2000), (1500, 4500), (700, 2000), (300, 900)]):
        seg = bp(n, lo, hi) * np.exp(-((tt - i / 4) ** 2) / 0.02)
        out += seg
    return out * np.sin(np.pi * tt) * 0.5


def tick():
    n = rng.standard_normal(int(SR * 0.02))
    return hp(n, 3000) * env(len(n), 0.0005, 0.004) * 0.6


def clink(f=2600):
    tt = t_(0.3)
    return (np.sin(2 * np.pi * f * tt) + 0.6 * np.sin(2 * np.pi * f * 1.47 * tt)) * env(len(tt), 0.001, 0.06) * 0.25


def fall_tone():
    tt = t_(0.55)
    f = 700 * np.exp(-tt * 2.5)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.01, 0.3) * 0.25


def buzz():
    tt = t_(0.25)
    return lp(np.sign(np.sin(2 * np.pi * 110 * tt)), 1200) * env(len(tt), 0.003, 0.15) * 0.25


def scribble(d=0.4):
    n = rng.standard_normal(int(SR * d))
    tt = t_(d)
    am = 0.5 + 0.5 * np.abs(np.sin(2 * np.pi * 9 * tt))
    return bp(n, 2500, 6000) * am * np.sin(np.pi * tt / d) * 0.15


def riser(d=0.53):
    tt = t_(d)
    f = 200 * (6 ** (tt / d))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.15 + hp(rng.standard_normal(len(tt)), 2000) * 0.15
    return s * (tt / d) ** 2


def bass_hit():
    tt = t_(0.8)
    f = 40 + 90 * np.exp(-tt * 12)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.001, 0.35)
    click = hp(rng.standard_normal(len(tt)), 2000) * env(len(tt), 0.0005, 0.01) * 0.3
    return (s + click) * 0.9


def bell(f=1320, d=1.4):
    tt = t_(d)
    s = sum(a * np.sin(2 * np.pi * f * r * tt) for a, r in [(1, 1), (0.5, 2.0), (0.3, 2.76), (0.15, 5.4)])
    return s * env(len(tt), 0.002, 0.45) * 0.12


def bloop():
    tt = t_(0.16)
    f = 300 + 700 * (tt / 0.16)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * tt / 0.16) * 0.3


def chime():
    out = np.zeros(int(SR * 1.4))
    for k, n in enumerate([84, 88, 91, 96]):
        add(out, bell(hz(n), 1.0) * 0.8, k * 0.07)
    return lp(out, 9000)


def pop():
    tt = t_(0.08)
    f = 900 * np.exp(-tt * 30) + 200
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.001, 0.03) * 0.4


def thump():
    tt = t_(0.5)
    f = 45 + 50 * np.exp(-tt * 15)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.002, 0.2) * 0.6


add(sfx, piano(57, 1.5, 0.9), 0.30, -2)          # Dulu: nota piano
add(sfx, swipe(), 0.90, -15)                       # aku
add(sfx, piano(45, 2.0, 1.2), 1.50, 0)            # SEDIH: piano rendah
add(sfx, swipe(0.35, 800, 3000), 2.85, -12)        # pan
add(sfx, clink(2600), 3.30, -6); add(sfx, clink(3100), 3.36, -9)  # duit
add(sfx, fall_tone(), 3.60, -6)                     # habis
for k in range(3):
    add(sfx, clink(2200 - k * 300), 3.75 + k * 0.12, -12)
add(sfx, swipe(), 4.20, -15)                       # kerja
add(sfx, buzz(), 4.50, -10)                        # tak jadi
add(sfx, scribble(), 4.70, -8)                     # coretan
add(sfx, riser(), 4.80, -6)                        # riser
add(sfx, bass_hit(), 5.40, -2)                     # TAPI
add(sfx, whoosh(), 6.00, -6)                       # rotate 90°
add(sfx, swipe(0.3, 600, 2500), 6.60, -14)         # ibu
for k in range(3):
    add(sfx, tick(), 7.20 + k * 0.1, -14)          # titik ...
add(sfx, swipe(0.35, 800, 3000), 7.50, -14)        # pan
add(sfx, bell(1320), 7.80, -4)                      # sabar sayang
add(sfx, swipe(0.3, 1000, 5000), 8.70, -10)        # whip pan
add(sfx, bloop(), 9.20, -8)                         # ?
add(sfx, chime(), 9.60, -6)                         # Alhamdulillah
for k in range(12):
    add(sfx, tick(), 10.20 + k * 0.04, -16)         # count-up
add(sfx, bell(2093, 1.0), 10.70, -2)  # ka-ching
add(sfx, clink(4200), 10.72, -6)
add(sfx, pop(), 10.80, -8)                          # sebulan!
add(sfx, thump(), 11.50, -6)                        # CTA

# ducking -4 dB around big hits
duck = np.ones(N)
for at, d in [(5.40, 0.5), (6.00, 0.45)]:
    i, j = int(at * SR), int((at + d) * SR)
    duck[i:j] = 10 ** (-4 / 20)
duck = np.convolve(duck, np.ones(480) / 480, mode='same')
mix = music * duck + sfx
fade = np.ones(N); k = int(0.3 * SR); fade[-k:] = np.linspace(1, 0, k)
mix *= fade
mix /= np.max(np.abs(mix)) * 1.05

out = sys.argv[1]
for name, sig in [('music', music), ('sfx', sfx), ('mix', mix)]:
    s = sig / max(1e-9, np.max(np.abs(sig))) * 0.95 if name != 'mix' else sig
    st = np.stack([s, s], axis=1).astype(np.float32)
    wavfile.write(f'{out}/{name}.wav', SR, st)
print('ok')
