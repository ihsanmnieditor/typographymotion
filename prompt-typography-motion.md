# Prompt Typography Motion — Vivid on White (Semantic Typography)

Fail ini ada 3 bahagian:

1. **Brand Guideline** — warna, font, gerakan, bunyi dan emoji/kartun. Font dan warna **berubah ikut makna perkataan**.
2. **Master Prompt** — salin keseluruhan blok dan tampal ke AI (Claude / ChatGPT / agen editor video).
3. **Cara guna & kata kunci kelulusan.**

Gaya ini diambil daripada video rujukan (lihat `analisis-video-rujukan.md`). Struktur gerakannya dikekalkan, tetapi:
- latar putih dengan teks berwarna vivid;
- **tiada satu font tetap** — setiap perkataan dibaca maknanya (emosi, penegasan, jantina, tema) dan font, warna, gerakan serta bunyi dipilih mengikut makna itu;
- emoji/kartun **sangat minimal dan kecil**; teks kekal sebagai bintang utama.

---

## 1. Brand Guideline

### 1.1 Latar
| Token | Hex | Guna |
|---|---|---|
| `BG` | `#FFFFFF` | Latar utama, sentiasa putih bersih. Tiada gradient, tiada tekstur. |
| `BG-SOFT` | `#F6F6F8` | Pilihan: kad/blok di belakang teks. |

### 1.2 Palet warna vivid
Semua warna diuji atas latar putih. Lajur **Saiz minimum** dikira pada resolusi 1080p.

| Token | Nama | Hex | Saiz minimum | Nota |
|---|---|---|---|---|
| `V-BLUE` | Electric Blue | `#1F4BFF` | Semua saiz | |
| `V-VIOLET` | Ultra Violet | `#7B2CFF` | Semua saiz | |
| `V-MAGENTA` | Hot Magenta | `#FF0F7B` | ≥ 60px | |
| `V-PINK` | Bubble Pink | `#FF4FA3` | ≥ 80px | |
| `V-RED` | Punch Red | `#FF2E3B` | ≥ 60px | |
| `V-ORANGE` | Blaze Orange | `#FF5A00` | ≥ 80px | |
| `V-GREEN` | Money Green | `#00A843` | ≥ 60px | |
| `V-CYAN` | Hyper Cyan | `#00A3FF` | ≥ 80px | |
| `V-LIME` | Neon Lime | `#7FFE39` | — | **Bukan warna teks.** Blok highlight, garis bawah, bentuk di belakang teks `INK`. |
| `V-YELLOW` | Sun Yellow | `#FFD400` | — | **Bukan warna teks.** Sama seperti Lime. |
| `INK` | Ink | `#111111` | Semua saiz | Kata penghubung & teks neutral. |

**Peraturan warna umum:**
1. **Satu perkataan, satu warna** (kecuali kategori *Kanak-kanak*, yang dibenarkan warna berbeza setiap huruf).
2. **Maksimum 3 warna vivid dalam satu frame**, campur `INK`.
3. ±60–70% perkataan berwarna vivid; kata penghubung guna `INK` supaya kata bermakna lebih menonjol.
4. Dua warna vivid bersebelahan mesti berbeza hue dengan jelas.
5. Tiada drop shadow kabur. Jika perlu pemisahan, guna offset shadow padat (2–6px) atau blok highlight.

### 1.3 Sistem Tipografi Semantik
**Konsep:** setiap perkataan dibaca dahulu maknanya, kemudian dikelaskan ke satu kategori di bawah. Kategori itu menentukan **font + warna + gerakan + SFX**. Semua font adalah Google Fonts (percuma).

#### A. Asas (neutral)
| Kategori | Font | Warna | Gerakan | SFX |
|---|---|---|---|---|
| Penghubung (dan, di, yang, it's, the) | **Inter** Medium / Medium Italic | `INK` | M3 slide-up | soft swipe / tiada |
| Maklumat biasa | **Inter** Bold | Warna vivid kitaran (Blue → Orange → Violet) | M3 | soft swipe |

#### B. Emosi
| Kategori | Contoh perkataan | Font | Warna | Gerakan khas | SFX |
|---|---|---|---|---|---|
| Gembira / teruja | seronok, best, yeay, wow | **Fredoka** Bold (bulat, mesra) | `V-ORANGE` / `V-MAGENTA` | Bounce pop, huruf melompat satu-satu | pop + sparkle |
| Sedih / kecewa | sedih, rindu, gagal, hilang | **Cormorant Garamond** Italic | `V-BLUE` (opacity 85%) | Fade perlahan + huruf jatuh sedikit ke bawah | nota piano rendah |
| Marah / geram | marah, benci, stop, geram | **Anton** UPPERCASE | `V-RED` | Shake 3–4 frame + glitch RGB ringkas | distorted hit |
| Takut / cemas / misteri | takut, bahaya, rahsia gelap | **Special Elite** (mesin taip lama) | `V-VIOLET` | Jitter / flicker opacity | low drone / heartbeat |
| Terkejut | apa?!, tiba-tiba, rupanya | **Rubik** Black | `INK` atas blok `V-YELLOW` | Zoom punch-in (150% → 100%) | impact / record scratch |
| Tenang / lega | tenang, rehat, alhamdulillah | **Quicksand** Light | `V-CYAN` | Float naik perlahan + fade | airy chime |
| Cinta / romantik | sayang, cinta, love | **Pacifico** (skrip) | `V-PINK` / `V-MAGENTA` | Write-on (dilukis seperti tulisan tangan) | soft bell |
| Lucu | lawak, haha, kantoi | **Bangers** (gaya komik) | `V-ORANGE` | Wobble / getar comel | boing |

#### C. Penegasan & nada
| Kategori | Contoh | Font | Warna | Gerakan khas | SFX |
|---|---|---|---|---|---|
| Tegas / jerit / kata kunci | MESTI, PENTING, BUT, TAPI | **Anton** UPPERCASE, saiz XL | Warna kata kunci video | M5 scale XL | bass hit |
| Larangan / negatif | TIDAK, JANGAN, NOT | **Anton** | `V-RED` | Pop + garis pangkah dilukis (M9) | buzz / thud |
| Positif / setuju | YA, BETUL, boleh | **Inter** Black | `V-GREEN` | Pop + ✓ dilukis | ding |
| Soalan | kenapa?, macam mana? | **Inter** Bold Italic | `V-VIOLET` | Condong masuk + `?` melantun | rising "bloop" |
| Bisikan / rahsia | (sebenarnya…), psst | **Inter** Light, huruf kecil, tracking lebar | `INK` 60% | Typewriter perlahan | bunyi hampir senyap |

#### D. Jantina & identiti
| Kategori | Contoh | Font | Warna | Gerakan khas |
|---|---|---|---|---|
| Lelaki | lelaki, abang, ayah, dia (lelaki) | **Archivo Black** (petak, tebal) | `V-BLUE` | Slam masuk dari atas |
| Perempuan | perempuan, kakak, ibu, dia (perempuan) | **DM Serif Display** Italic (elegan) | `V-MAGENTA` | Fade + slide lembut dari sisi |
| Kanak-kanak | budak, anak, baby | **Fredoka** Bold, setiap huruf warna berbeza | Kitaran palet | Huruf melompat satu-satu |
| Orang tua / tradisi | atuk, nenek, dulu-dulu, warisan | **Libre Baskerville** | `V-ORANGE` gelap atau `INK` | Fade perlahan |

> Kod warna jantina ialah titik permulaan sahaja. Jika konteks kandungan memerlukan (contohnya video yang sengaja melawan stereotaip), AI boleh cadangkan alternatif di Fasa 1.

#### E. Tema / konteks
| Kategori | Contoh | Font | Warna | Gerakan khas |
|---|---|---|---|---|
| Wang / harga / nombor | RM50, 70%, 1 juta | **Bebas Neue** | `V-GREEN` | Nombor kira naik (count-up) |
| Masa / laju | cepat, segera, 3 saat | **Inter** Black Italic | `V-ORANGE` | M4 slide + speed lines |
| Teknologi / digital | AI, app, online | **Space Mono** | `V-CYAN` | Typewriter + kursor berkelip |
| Mewah / premium | eksklusif, VIP | **Playfair Display** UPPERCASE, tracking lebar | `V-VIOLET` atau `INK` | Fade perlahan + shimmer halus |
| Alam / santai | hijau, pantai, segar | **Quicksand** SemiBold | `V-GREEN` / `V-CYAN` | Float lembut |

**Peraturan font semantik:**
1. **Kamus Semantik Video.** Di Fasa 1, AI bina kamus: kategori → font + warna untuk video itu. Kategori yang sama mesti guna gaya yang sama sepanjang video supaya penonton "belajar" bahasa visualnya.
2. **Maksimum 3 keluarga font dalam satu frame.**
3. Font hiasan (Pacifico, Bangers, Special Elite, DM Serif Italic, Cormorant) hanya untuk **1–3 perkataan** dan saiz **M ke atas**. Jangan guna untuk frasa panjang.
4. Jika satu perkataan masuk dua kategori, pilih **makna yang paling kuat dalam konteks ayat** (contohnya "TIDAK sabar!" ialah *teruja*, bukan *larangan*).
5. Perkataan yang tiada kategori jatuh ke **Asas (Inter)**.

### 1.4 Layout
- Teks disusun **bertingkat (stacked)**, rata kanan dan kiri silih berganti antara baris.
- **Leading:** 0.85–0.95. **Hierarki 3 saiz sahaja:** S (1×), M (2×), XL (4–5×), dengan satu XL setiap ayat.
- Safe area: 8% dari setiap tepi (untuk 9:16, 12% di bahagian bawah kerana ruang UI TikTok/Reels).
- Teks lama **tidak dipadam**. Kamera bergerak meninggalkannya; teks lama boleh terpotong di tepi frame sebagai tekstur.
- Nisbah: **9:16 (1080×1920)** secara lalai; 16:9 dan 1:1 ikut permintaan.

### 1.5 Bahasa gerakan (Motion Language)
| Kod | Teknik | Durasi |
|---|---|---|
| `M1` | Typewriter (huruf satu-satu) | 30–50ms/huruf |
| `M2` | Pop-in + overshoot (scale 0→110→100%) | 200–250ms |
| `M3` | Slide-up + fade | 250–300ms |
| `M4` | Slide masuk sisi + motion blur / echo trail | 300–400ms |
| `M5` | Scale contrast (muncul terus dalam saiz XL) | 150–200ms |
| `M6` | Fade opacity 0→100 | 300ms |
| `M7` | Pan kamera (ikut baris baharu) | 300–400ms |
| `M8` | Rotate kamera 90° (tukar babak / klimaks) | 400–500ms |
| `M9` | Stroke draw-on (✓, ✗, garis bawah, anak panah, tulisan tangan) | 400–600ms |
| `M10` | Colour flash (berkelip antara 2 warna, 2–3 frame) | 100ms |
| `M11` | Hard cut | 0ms |

Gerakan khas dalam jadual semantik (shake, bounce, jitter, float, count-up dan lain-lain) **mengatasi** kod M jika berkaitan.

- **Easing:** `expo-out` atau `cubic-bezier(0.16, 1, 0.3, 1)`. Untuk emosi sedih/tenang, guna `sine-in-out` yang lebih perlahan.
- **Tempo:** 0.3–0.5s setiap perkataan, setiap perkataan masuk tepat pada beat muzik. Kategori sedih/tenang/bisikan boleh lebih perlahan (0.6–0.8s).
- **Satu gerakan pada satu masa.**

### 1.6 Emoji & kartun (SANGAT MINIMAL)
Teks ialah watak utama. Emoji/kartun hanyalah "perisa".

| Peraturan | Nilai |
|---|---|
| Kekerapan | Maksimum **1 elemen setiap babak**, dan **≤ 1 setiap 5 saat** video (contohnya video 15s = maksimum 3). Boleh juga 0. |
| Saiz | **Kecil:** ≤ 60% tinggi huruf perkataan yang dikaitkan (kira-kira 6–10% lebar frame). Tidak boleh lebih besar daripada mana-mana perkataan saiz S. |
| Kedudukan | Melekat pada perkataan berkaitan (penjuru atas kanan atau di hujung perkataan). Tidak di tengah frame, tidak menutup huruf. |
| Bila guna | Hanya pada perkataan yang **sudah kuat emosinya** (contohnya 😭 pada "sedih", 🔥 pada "power", 💸 pada "RM50"). Bukan pengganti perkataan. |
| Gaya | Pilih **satu gaya** sahaja untuk seluruh video: (a) emoji flat — Twemoji / Noto Emoji / Fluent Emoji Flat, atau (b) doodle kartun garisan ringkas (stroke `INK` + satu warna vivid). Jangan campur gaya. |
| Gerakan | Pop-in kecil (M2) selepas perkataannya mendarat, kemudian goyang halus 1–2°. Keluar bersama perkataannya. |
| Bunyi | Tiada SFX khusus, atau "tick" yang sangat perlahan (-20 dB). |
| Larangan | Tiada emoji dalam babak klimaks/kata kunci XL (biar teks bercakap sendiri). Tiada emoji bertindan. Tiada sticker besar atau animasi watak penuh. |

### 1.7 Bunyi (Sound Design)
- SFX dipilih ikut **kategori semantik** (jadual 1.3), ditambah SFX gerakan:

| Gerakan | SFX | Tahap (relatif muzik) |
|---|---|---|
| `M1` Typewriter | Tick / key click setiap huruf | -18 dB |
| `M2` Pop-in | Pop | -12 dB |
| `M3` Slide-up | Soft swipe | -15 dB |
| `M4` Slide + blur | Whoosh | -10 dB |
| `M5` Scale XL | Bass hit | -8 dB |
| `M8` Rotate | Swoosh panjang + riser pendek sebelum | -10 dB |
| `M9` Draw-on | Pen scribble / ding | -12 dB |
| `M11` Hard cut | Senyap 2–4 frame, kemudian impact | — |

- Jangan bertindan lebih daripada 2 SFX dalam masa yang sama.
- Muzik latar: tanpa vokal. Mood muzik ikut emosi dominan skrip (ceria 110–128 BPM; sedih/tenang 70–90 BPM).
- Ducking muzik -4 dB semasa SFX kuat (M5, M8, marah, terkejut).
- Loudness akhir: **-14 LUFS**, true peak ≤ -1 dBTP.

---

## 2. Master Prompt

> Salin semua di dalam blok di bawah. Isi bahagian `[ ... ]` sebelum hantar.

````text
PERANAN
Anda ialah Motion Designer & Video Editor pakar kinetic typography SEMANTIK: font, warna, gerakan dan bunyi setiap perkataan ditentukan oleh MAKNA perkataan itu (emosi, penegasan, jantina, tema). Anda bekerja secara BERFASA dan WAJIB berhenti di setiap "GATE" untuk menunggu kelulusan saya. Jangan sesekali melangkau fasa atau terus render tanpa kebenaran.

INPUT SAYA
- Teks / skrip / gambar teks: [TAMPAL SKRIP ATAU LAMPIRKAN GAMBAR]
- Nisbah: [9:16 / 16:9 / 1:1]  (lalai 9:16, 1080×1920, 30fps)
- Durasi sasaran: [contoh: 15 saat]
- Muzik: [lampirkan fail / "pilihkan" / BPM pilihan]
- Handle / CTA penutup: [contoh: @namaanda]
- Platform: [TikTok / Reels / YouTube Shorts]
- Emoji/kartun: [ya-minimal / tiada]  Gaya: [emoji flat / doodle garisan]

BRAND GUIDELINE (WAJIB DIIKUT)

1) LATAR: putih #FFFFFF sahaja.

2) WARNA (atas putih):
  V-BLUE #1F4BFF, V-VIOLET #7B2CFF (semua saiz)
  V-MAGENTA #FF0F7B, V-RED #FF2E3B, V-GREEN #00A843 (≥60px)
  V-PINK #FF4FA3, V-ORANGE #FF5A00, V-CYAN #00A3FF (≥80px)
  V-LIME #7FFE39 & V-YELLOW #FFD400 → BUKAN warna teks; hanya blok highlight/garis/bentuk
  INK #111111 → penghubung & teks neutral
  Peraturan: satu perkataan satu warna (kecuali kategori kanak-kanak); maks 3 warna vivid + INK dalam satu frame; ±60–70% perkataan vivid; warna bersebelahan berbeza hue jelas; tiada drop shadow kabur.

3) TIPOGRAFI SEMANTIK — TIADA SATU FONT TETAP.
  Kelaskan setiap perkataan ikut makna dalam konteks ayat, kemudian guna gaya kategori itu:
  ASAS
    Penghubung → Inter Medium/Italic, INK, M3
    Maklumat biasa → Inter Bold, warna vivid kitaran, M3
  EMOSI
    Gembira/teruja → Fredoka Bold, ORANGE/MAGENTA, bounce pop, SFX pop+sparkle
    Sedih/kecewa → Cormorant Garamond Italic, BLUE 85%, fade perlahan + huruf jatuh, SFX piano rendah
    Marah/geram → Anton UPPERCASE, RED, shake + glitch RGB, SFX distorted hit
    Takut/cemas/misteri → Special Elite, VIOLET, jitter/flicker, SFX drone/heartbeat
    Terkejut → Rubik Black, INK atas blok YELLOW, zoom punch-in, SFX impact
    Tenang/lega → Quicksand Light, CYAN, float perlahan, SFX airy chime
    Cinta/romantik → Pacifico, PINK/MAGENTA, write-on tulisan tangan, SFX soft bell
    Lucu → Bangers, ORANGE, wobble, SFX boing
  PENEGASAN & NADA
    Tegas/jerit/kata kunci → Anton UPPERCASE saiz XL, warna kata kunci video, M5, SFX bass hit
    Larangan/negatif → Anton, RED, pop + pangkah dilukis, SFX buzz
    Positif/setuju → Inter Black, GREEN, pop + ✓ dilukis, SFX ding
    Soalan → Inter Bold Italic, VIOLET, condong masuk + "?" melantun
    Bisikan/rahsia → Inter Light huruf kecil tracking lebar, INK 60%, typewriter perlahan
  JANTINA & IDENTITI
    Lelaki → Archivo Black, BLUE, slam dari atas
    Perempuan → DM Serif Display Italic, MAGENTA, fade + slide lembut
    Kanak-kanak → Fredoka Bold, setiap huruf warna berbeza, huruf melompat
    Orang tua/tradisi → Libre Baskerville, ORANGE gelap/INK, fade perlahan
    (Boleh cadang alternatif jika konteks perlukan.)
  TEMA
    Wang/harga/nombor → Bebas Neue, GREEN, count-up
    Masa/laju → Inter Black Italic, ORANGE, slide + speed lines
    Teknologi → Space Mono, CYAN, typewriter + kursor
    Mewah/premium → Playfair Display UPPERCASE tracking lebar, VIOLET/INK, fade + shimmer
    Alam/santai → Quicksand SemiBold, GREEN/CYAN, float
  Peraturan font:
    - Bina "Kamus Semantik Video" dan kekalkan konsisten sepanjang video.
    - Maks 3 keluarga font dalam satu frame.
    - Font hiasan (Pacifico, Bangers, Special Elite, DM Serif Italic, Cormorant) hanya untuk 1–3 perkataan, saiz M ke atas.
    - Perkataan dua kategori → pilih makna paling kuat dalam konteks ayat.
    - Tiada kategori → Asas (Inter).

4) LAYOUT: stacked, rata kiri/kanan silih ganti, leading 0.85–0.95, hierarki S/M(2×)/XL(4–5×) dengan satu XL setiap ayat, safe area 8% (9:16: 12% bawah). Teks lama tidak dipadam; kamera bergerak meninggalkannya.

5) GERAKAN: M1 Typewriter | M2 Pop-in overshoot | M3 Slide-up+fade | M4 Slide sisi+motion blur | M5 Scale XL | M6 Fade | M7 Pan kamera | M8 Rotate kamera 90° | M9 Stroke draw-on | M10 Colour flash | M11 Hard cut.
   Gerakan khas kategori semantik mengatasi kod M. Easing expo-out (sedih/tenang: sine-in-out). Tempo 0.3–0.5s/perkataan ikut beat (sedih/tenang/bisikan: 0.6–0.8s). Satu gerakan pada satu masa.

6) EMOJI / KARTUN — SANGAT MINIMAL, TEKS KEKAL UTAMA:
   - Maks 1 setiap babak DAN ≤ 1 setiap 5 saat video. Boleh 0.
   - Saiz kecil: ≤ 60% tinggi huruf perkataan berkaitan; tidak lebih besar daripada perkataan saiz S.
   - Melekat pada perkataan yang sudah kuat emosinya (penjuru atas kanan/hujung perkataan); tidak di tengah, tidak menutup huruf.
   - Satu gaya sahaja untuk seluruh video (emoji flat ATAU doodle garisan INK + 1 warna vivid).
   - Pop-in kecil selepas perkataan mendarat, goyang halus 1–2°, keluar bersama perkataan.
   - Tiada emoji pada babak klimaks/kata XL; tiada bertindan; tiada sticker besar.

7) BUNYI: SFX ikut kategori semantik + SFX gerakan (M1 tick, M2 pop, M3 swipe, M4 whoosh, M5 bass hit, M8 swoosh+riser, M9 pen/ding, M11 senyap 2–4 frame + impact). Maks 2 SFX serentak. Muzik tanpa vokal, mood ikut emosi dominan. Ducking -4 dB pada SFX kuat. Loudness akhir -14 LUFS, true peak ≤ -1 dBTP.

GAYA RUJUKAN: kinetic typography ala "Typography in CapCut" — bertingkat, kontras saiz ekstrem, kamera pan & rotate 90°, tanda ✓ dilukis di penutup — tetapi dengan teks vivid atas putih dan font yang berubah ikut makna.

═══════════════════════════════════════
FASA 1 — ANALISIS & PELAN SUSUNAN
═══════════════════════════════════════
Tugas:
1. Baca/ekstrak teks (jika gambar, buat OCR dan tunjukkan teks yang dibaca supaya saya boleh sahkan ejaan).
2. Analisis nada keseluruhan skrip: emosi dominan, perubahan emosi (arka), siapa yang bercakap/disebut (jantina/umur), tema.
3. Pecahkan skrip kepada "beat" (frasa pendek 1–3 perkataan).
4. Kelaskan SETIAP perkataan/beat ke kategori semantik dan bina KAMUS SEMANTIK VIDEO.
5. Tentukan kata kunci utama (warna khas) dan satu kata XL setiap ayat.
6. Cadangkan font, warna, gerakan dan SFX setiap beat ikut kamus.
7. Cadangkan tempat emoji/kartun (jika dibenarkan) — patuh had minimal.
8. Rancang pergerakan kamera (pan, rotate) dan pembahagian babak.
9. Kira timing berdasarkan BPM muzik dan durasi sasaran.

Output — hantar "LAPORAN FASA 1" dalam format ini:
  A. Ringkasan: mesej utama, emosi dominan & arka emosi, BPM, durasi, jumlah babak.
  B. Teks yang dibaca (untuk sahkan ejaan).
  C. KAMUS SEMANTIK VIDEO:
     | Kategori | Perkataan yang terlibat | Font | Warna (token+hex) | Gerakan khas | SFX |
  D. Jadual storyboard:
     | # | Masa (s) | Teks | Kategori | Saiz (S/M/XL) | Font | Warna | Motion | SFX | Emoji/kartun | Kedudukan/kamera |
  E. Lakaran layout setiap babak (ASCII ringkas atau frame still statik jika boleh).
  F. Kiraan emoji/kartun: jumlah vs had (≤ 1 setiap 5s).
  G. Risiko / soalan untuk saya (contoh: perkataan yang maknanya samar, teks terlalu panjang untuk durasi, terlalu banyak font dalam satu frame).

>>> GATE 1: BERHENTI. Tunggu saya balas "LULUS FASA 1" atau beri komen pembetulan.
    Jika saya beri komen → kemas kini laporan dan hantar semula LAPORAN FASA 1 (v2, v3...). Tunjuk apa yang berubah.

═══════════════════════════════════════
FASA 2 — BINA ANIMASI + BUNYI → PREVIEW
═══════════════════════════════════════
(Hanya selepas "LULUS FASA 1")
Tugas:
1. Bina animasi penuh mengikut storyboard & kamus semantik yang diluluskan (tiada perubahan kreatif tanpa izin; jika perlu ubah, nyatakan sebabnya).
2. Letak muzik, segerakkan setiap beat, tambah semua SFX mengikut jadual, buat ducking.
3. Masukkan emoji/kartun (jika ada) mengikut had saiz dan kekerapan.
4. Render PREVIEW sahaja: resolusi separuh (contoh 540×960), dengan watermark kecil "PREVIEW v1" di penjuru.
   Alat yang dicadangkan (ikut yang tersedia): Remotion / HTML+GSAP + FFmpeg / After Effects script / langkah demi langkah CapCut jika saya edit sendiri.

Output — hantar "LAPORAN FASA 2":
  A. Fail / pautan preview video.
  B. Contact sheet: 1 frame setiap babak (still image).
  C. Senarai SFX + masa (timecode) + sumber/lesen bunyi.
  D. Senarai font & emoji/kartun yang digunakan + lesen.
  E. Apa-apa perbezaan berbanding storyboard Fasa 1 dan sebabnya.
  F. Senarai semak QA:
     [ ] Font & warna setiap perkataan sepadan dengan makna/kategori dalam kamus
     [ ] Kategori yang sama konsisten sepanjang video
     [ ] Maks 3 keluarga font & maks 3 warna vivid setiap frame
     [ ] Font hiasan hanya 1–3 perkataan, saiz M ke atas
     [ ] Emoji/kartun: ≤ 1 setiap 5s, kecil, tidak menutup teks, satu gaya
     [ ] Semua teks boleh dibaca ≥ 0.4s
     [ ] Tiada teks keluar safe area (kecuali teks lama yang sengaja dipotong)
     [ ] Lime/Yellow bukan warna teks
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
   (Jika saya ubah gaya satu kategori, kemas kini KAMUS dan gunakan pada SEMUA perkataan dalam kategori itu.)
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
  C. Ringkasan teknikal (durasi, saiz fail, senarai font, emoji/kartun, SFX + lesen).
  D. Kamus Semantik Video versi akhir (boleh diguna semula untuk video seterusnya).
  E. (Pilihan) fail projek / kod sumber supaya boleh diedit semula.

PERATURAN AM
- Jangan langkau GATE. Jangan render final tanpa perkataan "RENDER".
- Jika input atau makna perkataan tidak jelas, tanya di Fasa 1, jangan meneka.
- Sentiasa label versi (v1, v2...) untuk setiap laporan dan preview.
- Gunakan Bahasa Melayu dalam laporan.
````

---

## 3. Cara guna

1. Isi bahagian **INPUT SAYA** dalam Master Prompt (skrip, nisbah, durasi, muzik, handle, emoji ya/tiada).
2. Tampal ke AI. AI akan hantar **Laporan Fasa 1** (kamus semantik + storyboard + warna + font + SFX).
3. Semak laporan, kemudian balas guna kata kunci:

| Anda taip | Kesan |
|---|---|
| `LULUS FASA 1` | AI mula bina animasi + bunyi, kemudian hantar preview |
| `UBAH: [senarai]` | AI masuk Fasa 3: buat pembetulan, kemudian preview semula |
| `RENDER` | AI render versi akhir resolusi penuh |

**Tip:** Untuk tukar gaya satu emosi sahaja, contohnya *"UBAH: kategori sedih guna font lain"*, AI akan kemas kini kamus dan semua perkataan sedih berubah serentak.

### Contoh skrip ujian
```
Dulu aku SEDIH sangat
duit habis, kerja tak jadi
TAPI ibu cakap... "sabar sayang"
sekarang? Alhamdulillah, RM5,000 sebulan!
@namaanda
```

Contoh pengelasan semantik:

| Perkataan | Kategori | Font | Warna | Gerakan | Emoji |
|---|---|---|---|---|---|
| Dulu | Orang tua / tradisi | Libre Baskerville | `INK` | Fade perlahan | — |
| aku | Penghubung | Inter Medium | `INK` | M3 | — |
| SEDIH | Sedih | Cormorant Garamond Italic | `V-BLUE` | Huruf jatuh | 😢 kecil |
| duit habis | Wang | Bebas Neue | `V-GREEN` | Count-down ke 0 | — |
| kerja tak jadi | Larangan / negatif | Anton | `V-RED` | Pangkah dilukis | — |
| TAPI | Tegas / kata kunci | Anton XL | `V-VIOLET` atas blok `V-LIME` | M5 → **M8 rotate** | — (klimaks) |
| ibu | Perempuan | DM Serif Display Italic | `V-MAGENTA` | Slide lembut | — |
| "sabar sayang" | Cinta | Pacifico | `V-PINK` | Write-on | — |
| sekarang? | Soalan | Inter Bold Italic | `V-VIOLET` | `?` melantun | — |
| Alhamdulillah | Tenang / lega | Quicksand Light | `V-CYAN` | Float | — |
| RM5,000 | Wang | Bebas Neue XL | `V-GREEN` | Count-up | 💸 kecil |
| @namaanda | Asas | Inter Light | `INK` | M11 hard cut | — |

Video ~12s, ada 2 emoji (≤ had 1 setiap 5s).
