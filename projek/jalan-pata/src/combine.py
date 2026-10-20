"""Join the 3 parts of storyboard.json into one timeline (hard cut between parts, @handle only at the end).
Writes storyboard_gabung.json with a single part (id 0)."""
import copy, json, sys

d = sys.argv[1]
parts = json.load(open(f'{d}/storyboard.json'))
out = dict(id=0, title='Gabung (1+2+3)', mood=' → '.join(p['mood'] for p in parts), babak=[], offsets=[])
off = 0.0
for i, P in enumerate(parts):
    out['offsets'].append(off)
    for j, bb in enumerate(P['babak']):
        bb = copy.deepcopy(bb)
        bb['t0'] = round(bb['t0'] + off, 2); bb['t1'] = round(bb['t1'] + off, 2)
        if i and j == 0:
            bb['cam'] = 'M11 hard cut (sambung bahagian)'
        for line in bb['lines']:
            for b in line:
                b['t'] = round(b['t'] + off, 2)
        out['babak'].append(bb)
    if i < len(parts) - 1:
        off = round(off + P['cta'], 2)      # next part starts where the old @handle cut was
    else:
        out['cta'] = round(off + P['cta'], 2)
        out['dur'] = round(off + P['dur'], 2)
out['emoji'] = sum(p['emoji'] for p in parts)
json.dump([out], open(f'{d}/storyboard_gabung.json', 'w'), ensure_ascii=False, indent=1)
print('offsets', out['offsets'], 'cta', out['cta'], 'dur', out['dur'])
