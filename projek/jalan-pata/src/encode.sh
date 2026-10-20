#!/bin/bash
# encode.sh <dir> <part> <out.mp4> : two-pass loudnorm (-14 LUFS, TP -2 before AAC) + H.264 mux
set -e
D=$1; N=$2; OUT=$3
ffmpeg -v error -y -i "$D/mix$N.wav" -af "alimiter=limit=0.22:attack=3:release=60:level=false" "$D/lim$N.wav"
J=$(ffmpeg -hide_banner -i "$D/lim$N.wav" -af loudnorm=I=-14:TP=-2.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
get(){ echo "$J" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -v error -y -i "$D/lim$N.wav" -af "loudnorm=I=-14:TP=-2.5:LRA=11:measured_I=$(get input_i):measured_TP=$(get input_tp):measured_LRA=$(get input_lra):measured_thresh=$(get input_thresh):offset=$(get target_offset):linear=true,aresample=48000" "$D/norm$N.wav"
ffmpeg -v error -y -framerate 30 -i "$D/seq$N/f%05d.png" -i "$D/norm$N.wav" -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium -c:a aac -b:a 320k -ar 48000 -shortest -movflags +faststart "$OUT"
ffmpeg -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak):" | tr -s ' ' | tr '\n' ' '; echo
