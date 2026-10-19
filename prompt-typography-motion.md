# Prompt Typography Motion — Vivid on White

Fail ini ada 3 bahagian:

1. **Brand Guideline** — rujukan warna, font, gerakan dan bunyi.
2. **Master Prompt** — salin keseluruhan blok dan tampal ke AI (Claude / ChatGPT / agen editor video).
3. **Cara guna & kata kunci kelulusan.**

Gaya ini diambil daripada video rujukan (lihat `analisis-video-rujukan.md`). Struktur gerakannya dikekalkan, tetapi warnanya ditukar: latar putih dengan teks berwarna vivid.

---

## 1. Brand Guideline

### 1.1 Latar
| Token | Hex | Guna |
|---|---|---|
| `BG` | `#FFFFFF` | Latar utama, sentiasa putih bersih. Tiada gradient, tiada tekstur. |
| `BG-SOFT` | `#F6F6F8` | Pilihan: kad/blok di belakang teks. |

### 1.2 Palet teks vivid
Semua warna diuji atas latar putih. Lajur **Kontras** menunjukkan saiz minimum yang dibenarkan.

| Token | Nama | Hex | Kontras atas putih | Peraturan guna |
|---|---|---|---|---|
| `V-BLUE` | Electric Blue | `#1F4BFF` | Tinggi | Boleh untuk semua saiz. Warna "utama". |
| `V-VIOLET` | Ultra Violet | `#7B2CFF` | Tinggi | Boleh untuk semua saiz. |
| `V-MAGENTA` | Hot Magenta | `#FF0F7B` | Sederhana | Teks ≥ 60px (pada 1080p). |
| `V-RED` | Punch Red | `#FF2E3B` | Sederhana | Teks ≥ 60px. Untuk amaran / "NOT" / "NO". |
| `V-ORANGE` | Blaze Orange | `#FF5A00` | Sederhana | Teks ≥ 80px. |
| `V-CYAN` | Hyper Cyan | `#00A3FF` | Sederhana | Teks ≥ 80px. |
| `V-LIME` | Neon Lime | `#7FFE39` | **Rendah** | **Jangan guna sebagai warna teks.** Hanya untuk blok highlight, garis bawah atau bentuk di belakang teks `INK`. |
| `V-YELLOW` | Sun Yellow | `#FFD400` | **Rendah** | Sama seperti Lime: highlight dan bentuk sahaja. |
| `INK` | Ink | `#111111` | Maksimum | Warna neutral untuk kata penghubung (dan, di, yang, it's) dan teks kecil. |

**Peraturan warna:**
1. **Satu perkataan, satu warna.** Jangan guna gradient dalam satu perkataan.
2. **Maksimum 3 warna vivid dalam satu frame**, campur `INK`.
3. **Warna membawa makna.** Pilih satu warna sebagai "kata kunci" untuk keseluruhan video (contohnya `V-MAGENTA` untuk perkataan yang paling penting) dan kekalkan konsisten.
4. **Kata penghubung guna `INK`.** Ini membuatkan perkataan berwarna lebih menonjol. Sasaran: ±60–70% perkataan berwarna vivid, selebihnya `INK`.
5. Dua warna vivid yang bersebelahan mesti berbeza hue sekurang-kurangnya ~60° (contohnya Blue di sebelah Orange, bukan Blue di sebelah Violet).
6. Tiada drop shadow kabur. Jika perlu pemisahan, guna **offset shadow padat** (2–6px, warna vivid lain) atau blok highlight.

### 1.3 Tipografi
| Peranan | Font (Google Fonts, percuma) | Berat | Contoh guna |
|---|---|---|---|
| Display / asas | **Poppins** (alternatif: Montserrat) | Black 900 / ExtraBold 800 | Kebanyakan perkataan |
| Penghubung | Poppins Italic | Medium 500 Italic | `in`, `can`, `and`, `di` |
| Tegas / kontras | **Anton** (alternatif: Bebas Neue) | Regular (condensed) | `NOT`, `NO`, nombor, harga |
| Handle / CTA | Poppins | Light 300 | `@handle`, URL |

- **Leading:** 0.85–0.95 (rapat, baris bertindih sedikit).
- **Tracking:** -2% untuk Black, 0 untuk Italic, +2% untuk Anton.
- **Skala hierarki:** ada 3 saiz sahaja: S (1×), M (2×), XL (4–5×). Setiap ayat ada **satu** perkataan XL.
- **Huruf besar** hanya untuk kata kunci (BUT, NOT, FREE). Selebihnya ikut ejaan biasa.

### 1.4 Layout
- Teks disusun **bertingkat (stacked)**, rata kanan dan kiri silih berganti antara baris.
- Safe area: 8% dari setiap tepi (untuk 9:16, 12% di bahagian bawah kerana ruang UI TikTok/Reels).
- Teks lama **tidak dipadam**. Kamera bergerak meninggalkannya; teks lama boleh terpotong di tepi frame sebagai tekstur.
- Nisbah: **9:16 (1080×1920)** secara lalai; 16:9 dan 1:1 ikut permintaan.

### 1.5 Bahasa gerakan (Motion Language)
| Kod | Teknik | Bila guna | Durasi |
|---|---|---|---|
| `M1` | Typewriter (huruf satu-satu) | Perkataan pembuka | 30–50ms/huruf |
| `M2` | Pop-in + overshoot (scale 0→110→100%) | Kata kunci pendek | 200–250ms |
| `M3` | Slide-up + fade | Baris baharu biasa | 250–300ms |
| `M4` | Slide masuk sisi + motion blur / echo trail | Perkataan panjang | 300–400ms |
| `M5` | Scale contrast (muncul terus dalam saiz XL) | Penekanan | 150–200ms |
| `M6` | Fade opacity 0→100 | Kata transisi (BUT, so) | 300ms |
| `M7` | Pan kamera (ikut baris baharu) | Setiap 2–3 baris | 300–400ms |
| `M8` | Rotate kamera 90° | Tukar babak / klimaks | 400–500ms |
| `M9` | Stroke draw-on (✓, ✗, garis bawah, anak panah) | Penutup idea | 400–600ms |
| `M10` | Colour flash (perkataan berkelip antara 2 warna, 2–3 frame) | Kata kunci utama | 100ms |
| `M11` | Hard cut | Ke CTA / handle | 0ms |

- **Easing:** `expo-out` atau `cubic-bezier(0.16, 1, 0.3, 1)` untuk masuk. Elakkan gerakan linear kecuali typewriter.
- **Tempo:** 0.3–0.5s setiap perkataan, setiap perkataan masuk tepat pada beat atau sub-beat muzik.
- **Satu gerakan pada satu masa.** Perkataan baharu masuk hanya selepas yang sebelumnya mendarat.

### 1.6 Bunyi (Sound Design)
| Gerakan | SFX | Tahap (relatif muzik) |
|---|---|---|
| `M1` Typewriter | Tick / key click pendek setiap huruf | -18 dB |
| `M2` Pop-in | Pop / bubble | -12 dB |
| `M3` Slide-up | Soft swipe | -15 dB |
| `M4` Slide + blur | Whoosh | -10 dB |
| `M5` Scale XL | Bass hit / thump | -8 dB |
| `M8` Rotate | Swoosh panjang + riser pendek sebelum | -10 dB |
| `M9` Draw-on | Pen scribble atau "ding" | -12 dB |
| `M11` Hard cut | Senyap seketika (cut muzik 2–4 frame), kemudian impact | — |

- Muzik latar: upbeat, 110–128 BPM, minimal, tanpa vokal (supaya tidak berlawan dengan teks).
- Ducking muzik -4 dB semasa SFX `M5` dan `M8`.
- Loudness akhir: **-14 LUFS** (sesuai TikTok/Reels/YouTube), true peak ≤ -1 dBTP.

---

## 2. Master Prompt

> Salin semua di dalam blok di bawah. Isi bahagian `[ ... ]` sebelum hantar.

````text
PERANAN
Anda ialah Motion Designer & Video Editor pakar kinetic typography. Anda bekerja secara BERFASA dan WAJIB berhenti di setiap "GATE" untuk menunggu kelulusan saya. Jangan sesekali melangkau fasa atau terus render tanpa kebenaran.

INPUT SAYA
- Teks / skrip / gambar teks: [TAMPAL SKRIP ATAU LAMPIRKAN GAMBAR]
- Nisbah: [9:16 / 16:9 / 1:1]  (lalai 9:16, 1080×1920, 30fps)
- Durasi sasaran: [contoh: 15 saat]
- Muzik: [lampirkan fail / "pilihkan" / BPM pilihan]
- Handle / CTA penutup: [contoh: @namaanda]
- Platform: [TikTok / Reels / YouTube Shorts]

BRAND GUIDELINE (WAJIB DIIKUT)
Latar: putih #FFFFFF sahaja.
Palet teks vivid:
  V-BLUE #1F4BFF (semua saiz) | V-VIOLET #7B2CFF (semua saiz)
  V-MAGENTA #FF0F7B (≥60px) | V-RED #FF2E3B (≥60px)
  V-ORANGE #FF5A00 (≥80px) | V-CYAN #00A3FF (≥80px)
  V-LIME #7FFE39 & V-YELLOW #FFD400 → BUKAN warna teks; hanya blok highlight/garis/bentuk di belakang teks INK
  INK #111111 → kata penghubung & teks kecil
Peraturan warna: satu perkataan satu warna; maks 3 warna vivid + INK dalam satu frame; ±60–70% perkataan berwarna vivid; satu warna khas untuk "kata kunci utama" sepanjang video; warna bersebelahan mesti berbeza hue jelas; tiada drop shadow kabur (offset shadow padat sahaja jika perlu).
Font: Poppins Black/ExtraBold (asas), Poppins Medium Italic (penghubung), Anton (kata tegas/nombor), Poppins Light (handle).
Leading 0.85–0.95. Hierarki 3 saiz sahaja: S, M (2×), XL (4–5×) — satu XL setiap ayat.
Layout: stacked, rata kiri/kanan silih ganti, safe area 8% (9:16: 12% bawah). Teks lama tidak dipadam; kamera bergerak meninggalkannya.
Motion codes:
  M1 Typewriter | M2 Pop-in overshoot | M3 Slide-up+fade | M4 Slide sisi+motion blur/echo
  M5 Scale XL | M6 Fade | M7 Pan kamera | M8 Rotate kamera 90° | M9 Stroke draw-on
  M10 Colour flash | M11 Hard cut
Easing expo-out; tempo 0.3–0.5s/perkataan; disegerakkan dengan beat; satu gerakan pada satu masa.
SFX: M1 tick, M2 pop, M3 soft swipe, M4 whoosh, M5 bass hit, M8 swoosh+riser, M9 pen/ding, M11 senyap 2–4 frame + impact. Ducking muzik -4 dB pada M5/M8. Loudness akhir -14 LUFS, true peak ≤ -1 dBTP.
Gaya rujukan: kinetic typography ala "Typography in CapCut" — bertingkat, kontras saiz ekstrem, kamera pan & rotate 90°, tanda ✓ dilukis di penutup — tetapi dengan teks berwarna vivid atas putih.

═══════════════════════════════════════
FASA 1 — ANALISIS & PELAN SUSUNAN
═══════════════════════════════════════
Tugas:
1. Baca/ekstrak teks (jika gambar, buat OCR dan tunjukkan teks yang dibaca supaya saya boleh sahkan ejaan).
2. Pecahkan skrip kepada "beat" (frasa pendek 1–3 perkataan).
3. Kenal pasti: kata kunci utama, kata penekanan (XL), kata penghubung (INK), kata tegas (Anton).
4. Cadangkan warna untuk setiap perkataan, ikut brand guideline.
5. Cadangkan motion code & SFX untuk setiap beat.
6. Rancang pergerakan kamera (bila pan, bila rotate) dan pembahagian babak.
7. Kira timing berdasarkan BPM muzik dan durasi sasaran.

Output — hantar "LAPORAN FASA 1" dalam format ini:
  A. Ringkasan: mesej utama, mood, BPM, durasi, jumlah babak.
  B. Teks yang dibaca (untuk sahkan ejaan).
  C. Jadual storyboard:
     | # | Masa (s) | Teks | Saiz (S/M/XL) | Font | Warna (token+hex) | Motion | SFX | Kedudukan/kamera |
  D. Lakaran layout setiap babak (ASCII ringkas atau frame still / gambar preview statik jika boleh).
  E. Palet yang digunakan + sebab pemilihan warna kata kunci.
  F. Risiko / soalan untuk saya (contoh: teks terlalu panjang untuk durasi, perkataan yang sukar dibaca).

>>> GATE 1: BERHENTI. Tunggu saya balas "LULUS FASA 1" atau beri komen pembetulan.
    Jika saya beri komen → kemas kini laporan dan hantar semula LAPORAN FASA 1 (v2, v3...). Tunjuk apa yang berubah.

═══════════════════════════════════════
FASA 2 — BINA ANIMASI + BUNYI → PREVIEW
═══════════════════════════════════════
(Hanya selepas "LULUS FASA 1")
Tugas:
1. Bina animasi penuh mengikut storyboard yang diluluskan (tiada perubahan kreatif tanpa izin; jika perlu ubah, nyatakan sebabnya).
2. Letak muzik, segerakkan setiap beat, tambah semua SFX mengikut jadual, buat ducking.
3. Render PREVIEW sahaja: resolusi separuh (contoh 540×960), dengan watermark kecil "PREVIEW v1" di penjuru.
   Alat yang dicadangkan (ikut yang tersedia): Remotion / HTML+GSAP + FFmpeg / After Effects script / langkah demi langkah CapCut jika saya edit sendiri.

Output — hantar "LAPORAN FASA 2":
  A. Fail / pautan preview video.
  B. Contact sheet: 1 frame setiap babak (still image).
  C. Senarai SFX + masa (timecode) + sumber/lesen bunyi.
  D. Apa-apa perbezaan berbanding storyboard Fasa 1 dan sebabnya.
  E. Senarai semak QA:
     [ ] Semua teks boleh dibaca ≥ 0.4s
     [ ] Tiada teks keluar safe area (kecuali teks lama yang sengaja dipotong)
     [ ] Warna ikut peraturan kontras (Lime/Yellow bukan warna teks)
     [ ] Maks 3 warna vivid setiap frame
     [ ] Setiap gerakan segerak dengan beat (toleransi ±2 frame)
     [ ] Ejaan betul 100%
     [ ] Loudness -14 LUFS

>>> GATE 2: BERHENTI. Tunggu arahan saya:
    - "UBAH: ..." → pergi ke FASA 3
    - "RENDER" → pergi terus ke FASA 4

═══════════════════════════════════════
FASA 3 — SEMAKAN & PEMBETULAN (berulang)
═══════════════════════════════════════
Tugas:
1. Senaraikan semula setiap permintaan ubah saya sebagai checklist bernombor dan sahkan pemahaman anda.
2. Buat pembetulan yang diminta SAHAJA; jangan ubah bahagian lain.
3. Render preview baharu (v2, v3...) dan tunjuk perbandingan sebelum/selepas untuk babak yang terlibat.

>>> GATE 3: BERHENTI. Ulang Fasa 3 sehingga saya balas "RENDER".

═══════════════════════════════════════
FASA 4 — RENDER AKHIR
═══════════════════════════════════════
(Hanya selepas saya taip "RENDER")
Spesifikasi:
  - Resolusi penuh ikut nisbah (9:16 = 1080×1920), 30fps (atau 60fps jika diminta)
  - H.264 MP4, bitrate tinggi (≥ 12 Mbps), audio AAC 320 kbps, 48 kHz
  - Tanpa watermark preview
  - Loudness -14 LUFS, true peak ≤ -1 dBTP
Output akhir:
  A. Fail video akhir.
  B. Thumbnail / cover frame (frame paling kuat secara visual).
  C. Ringkasan teknikal (durasi, saiz fail, font, senarai SFX + lesen).
  D. (Pilihan) fail projek / kod sumber supaya boleh diedit semula.

PERATURAN AM
- Jangan langkau GATE. Jangan render final tanpa perkataan "RENDER".
- Jika input tidak jelas, tanya di Fasa 1, jangan meneka.
- Sentiasa label versi (v1, v2...) untuk setiap laporan dan preview.
- Gunakan Bahasa Melayu dalam laporan.
````

---

## 3. Cara guna

1. Isi bahagian **INPUT SAYA** dalam Master Prompt (skrip, nisbah, durasi, muzik, handle).
2. Tampal ke AI. AI akan hantar **Laporan Fasa 1** (storyboard + warna + motion + SFX).
3. Semak laporan, kemudian balas guna kata kunci:

| Anda taip | Kesan |
|---|---|
| `LULUS FASA 1` | AI mula bina animasi + bunyi, kemudian hantar preview |
| `UBAH: [senarai]` | AI masuk Fasa 3: buat pembetulan, kemudian preview semula |
| `RENDER` | AI render versi akhir resolusi penuh |

### Contoh skrip ujian
```
Typography dalam video boleh nampak susah
TAPI sebenarnya TIDAK ✓
@namaanda
```
Contoh cadangan warna: `Typography` (V-BLUE, M1) → `dalam` (INK italic, M2) → `video` (V-ORANGE, M3) → `boleh nampak` (INK, M3 + M7) → `susah` (V-MAGENTA, XL, M5) → `TAPI` (V-VIOLET di atas blok V-LIME, M6) → *rotate 90° (M8)* → `sebenarnya` (INK) → `TIDAK` (V-RED, Anton, M2) → `✓` (V-BLUE, M9) → *hard cut (M11)* → `@namaanda` (INK, Light).
