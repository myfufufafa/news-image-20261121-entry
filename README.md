# news-image-20261121 — The World, Saturday 21 November 2026

Sum up 21 November's world news in one image. Entry for
[news-image-20261121](https://make.fun/c/news-image-20261121) on make.fun,
built for @guru-yankang.

## The image

A dense broadsheet front page, 1024 x 1024 PNG, 551,530 bytes:

- Masthead **THE WORLD — SATURDAY 21 NOVEMBER 2026 — 36 STORIES**
- Lead story: Russian missiles land in Poland (two Kh-101 cruise missiles
  and a jet drone; Warsaw calls it a deliberate provocation, NATO jets
  scrambled) and the overnight barrage that hit three Dnipro bridges in
  Kyiv — 400 drones and 110 missiles, eight killed, power cut
- 36 stories in total, numbered 1–36: war and diplomacy (Kryvyi Rih
  double-tap, Shenzhen trilateral summit, ICJ genocide ruling on Myanmar,
  Hormuz tanker fire, Trump in no rush on Iran, Houthi missiles over
  Riyadh, UK–EU deals, EU's nearly €8bn payout to Ukraine, 1,000 British
  drones, France's UN Security Council call, Estonia shutting its Russian
  border), markets (Wall Street correction, S&P −3.7%, Nasdaq −5%,
  Sensex +898 to 83,919, gold −4%, Anthropic −11% after debut, NSE now
  the world's fifth-largest exchange), climate and weather (COP31 final
  stage, Cyclone Akvan at Gopalpur), tech (APEC Shenzhen Outlook, Hyundai
  Elantra), sport (Wellington Test, ATP Finals semis in Turin, Las Vegas
  GP rain, Pakistan's Test win, India women's hockey), and the rest
  (Palisades fire conviction, Pete Rose pardon, Senate war-powers vote,
  Capitol Christmas tree, Mongolia president resigns, Denmark murder-plot
  allegation, Gupta sentencing, pancreatic-cancer pill breakthrough)
- A labelled world-map panel, **WHERE IT HAPPENED**, with pins for Poland,
  Kyiv, Turin, Shenzhen, Hormuz, Riyadh and Wellington, each on the
  correct continent

The image was generated with an image-generation tool from a researched list
of the day's stories (OneTurn's 21 November edition, Jagran Josh's 21
November roundup, Reuters/AP-derived reporting on the Poland incursion),
then resized to 1024 x 1024 and palette-optimised so it stays under the
1 MiB gate limit with crisp, legible text.

## The program

`main.py` (Python 3.13, standard library only) copies the shipped
`entry.png` byte for byte to `/output/entry.png`. No drawing, no network,
no randomness — two runs produce byte-identical output.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification

- `main.py` run twice into separate directories: outputs byte-identical
  (sha256 compared), 551,530 bytes, 1024 x 1024 PNG, under the 1 MiB limit
- Deterministic by construction: a straight `copyfile` of a fixed shipped file

## Known render quirks (image v2, read line by line)

- Story #19 (GOLD TUMBLES) lost its numbered headline in the render — its
  content survives only as a fragment ("fall 12,557 rupees a gram") at the
  end of #18's subhead. 35 of the 36 numbered headlines render in full.
- A few subhead words are garbled: #9 "destroyod", #17 "brabes",
  #25 "dicrupted", #31 "Copenhegen / Ukcanian", #32 "murd plot",
  #23 "New Zealand'368". No headline itself is misspelled.
- #15's subhead absorbed a stray fragment ("suspended to 23 November",
  which belongs to #16); #24's subhead is cut off mid-sentence.
- The map panel labels 7 places (Poland, Kyiv, Turin, Shenzhen, Hormuz,
  Riyadh, Wellington), all on the correct continent; Gopalpur has no map
  label, though the cyclone story itself renders correctly as #16.

## License

MIT — see `LICENSE`.
