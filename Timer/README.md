# Timer (mkw-recomp mod)

The Switch `timer.zip` mod, ported to mkw-recomp for MKW 1.8.0: import the `Timer/` folder from the
start screen's Mods page (zip or folder — this folder is the mod).

| Part | What it does |
|---|---|
| `romfs/` | The mod's blink animation for the race timer (`RaceInfo_1...blarc.zs`) |
| `exefs/` | The original Switch IPS (build-id matched at import; kept for Switch/emulator use) |
| `mod.json` | The port: `switches` with `TIMER`, the compiled-in patch span (`recomp/patches-mkw-180.txt`: `main+0x48E728`, 22 words skipped while the switch is on) |

Enabling the mod in the menu sets `MKW_TIMER=1` for the next start; the generated code then skips the
timer-hide block exactly as the mod's branch does. Disabling restores the stock timer.
