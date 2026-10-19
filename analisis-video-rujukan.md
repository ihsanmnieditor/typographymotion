# Analisis Video Rujukan — "Typography in CapCut"

**Spesifikasi fail:** 1024×576 (16:9), 30 fps, ±10.5 saat, ada audio (muzik latar).
**Struktur masa:**

| Masa | Bahagian |
|---|---|
| 0.0 – 5.7s | Kinetic typography (isi utama) |
| 5.7 – 6.5s | Kad nama `@ECO` (hard cut) |
| 6.5 – 10.5s | End card TikTok (watermark platform — **abaikan**, bukan sebahagian gaya) |

## 1. Breakdown babak demi babak

| # | Masa (anggaran) | Teks | Teknik animasi |
|---|---|---|---|
| 1 | 0.5 – 1.2s | `TYPOGRAPHY` | **Typewriter** — huruf muncul satu-satu dari kiri ke kanan (T → TYPOGRA → TYPOGRAPHY). |
| 2 | 1.2 – 1.4s | `IN` | **Pop-in** perkataan italic, warna aksen hijau lime, letak di sebelah kanan baris. |
| 3 | 1.6 – 2.0s | `CapCut` | **Slide-up + fade** dari bawah (kelabu → hitam), baris baharu, rata kanan. |
| 4 | 2.0 – 2.3s | `can` | Italic ringan, masuk di bawah; **kamera pan ke atas** mengikut baris baharu (teks lama tolak keluar frame). |
| 5 | 2.3 – 2.6s | `be` | **Scale contrast** — saiz sangat besar & tebal berbanding perkataan lain; muncul huruf `b` dahulu. |
| 6 | 2.6 – 3.0s | `challenging` | **Slide-in dari kiri dengan motion blur / echo trail**, mendarat di bawah `be`. |
| 7 | 3.0 – 3.5s | `BUT` | **Fade-in** (lutsinar → penuh) warna hijau lime, saiz gergasi. Kata kunci titik pusing ayat. |
| 8 | 3.5 – 4.0s | (transisi) | **Rotate kamera 90°** — seluruh komposisi berpusing, teks lama jadi menegak di tepi kiri sebagai "dinding". |
| 9 | 4.0 – 4.3s | `it's` | Fade kelabu → hitam. |
| 10 | 4.3 – 4.6s | `NOT` | **Hard pop**, tukar ke font *condensed* tinggi — kontras typeface. |
| 11 | 4.6 – 5.2s | `✓` | **Stroke draw-on** — tanda semak dilukis, warna hijau. |
| 12 | 5.2 – 5.7s | (transisi) | Teks `@ECO` muncul bertindih (glitch overlap), kemudian **hard cut**. |
| 13 | 5.7 – 6.5s | `@ECO` | Handle/brand, font nipis, tengah skrin, statik. |

## 2. Prinsip reka bentuk yang dikesan

- **Satu idea, satu perkataan, satu gerakan.** Setiap perkataan dapat animasi sendiri; tiada dua perkataan masuk serentak.
- **Hierarki melalui saiz, bukan warna sahaja.** `be` dan `BUT` diperbesar 3–5× untuk penekanan.
- **Campuran typeface yang terkawal:** geometric sans tebal (Black/ExtraBold) sebagai asas, italic untuk kata penghubung (`IN`, `can`), condensed untuk kata tegas (`NOT`), light untuk handle.
- **Layout bertingkat (stacked)** — baris bertindih rapat, leading sangat ketat (≈ 0.85), rata kanan/kiri silih ganti.
- **Kamera maya bergerak** — pan ke atas, kemudian rotate 90°; teks lama kekal dalam frame sebagai tekstur.
- **Tempo laju:** purata 0.3–0.5s setiap perkataan, disegerakkan dengan beat muzik.
- **Easing:** keluar laju, mendarat perlahan (ease-out / expo-out), sedikit overshoot pada pop-in.

## 3. Palet warna rujukan (sampel piksel)

| Peranan | Hex |
|---|---|
| Latar | `#FCFCFC` (putih lembut) |
| Teks utama | `#000000` |
| Aksen | `#7FFE39` (hijau lime neon) |
| Tanda semak | hijau tepu ±`#1EC81E` |

**Perbezaan dengan gaya yang anda mahu:** video rujukan hampir monokrom (hitam + satu aksen). Gaya anda akan kekalkan struktur gerakan di atas, tetapi **teks majoriti berwarna vivid** atas latar putih — lihat `prompt-typography-motion.md`.
