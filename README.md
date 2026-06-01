# CyberMesh Labs

![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![Chart.js](https://img.shields.io/badge/Chart.js-4-FF6384?logo=chartdotjs)
![Tailwind](https://img.shields.io/badge/Tailwind-3-06B6D4?logo=tailwindcss)
![License](https://img.shields.io/badge/License-MIT-blue)

**Autonomous Security Operations Center (SOC) Dashboard** — a real-time cyber threat simulation with live telemetry, threat vector radar analysis, and system integrity monitoring.

> [Live Demo](https://raphasha27.github.io/CyberMesh-Labs/)

## Features

- **Live Threat Telemetry** — Simulated real-time log feed of security events (DDoS, SQLi, Malware, Port Scans, Unauthorized Auth) with IP addresses and severity levels
- **Threat Vector Radar** — Interactive Chart.js radar chart visualizing global threat vector activity across 6 categories, updating every 3 seconds
- **System Metrics** — Packets inspected (1.42B), payloads blocked (84,932), system integrity status
- **Defcon Status Indicator** — Visual DEFCON level badge
- **Cyberpunk Aesthetic** — Dark theme, neon green (#00ffcc) accents, CRT scanline overlay, glassmorphism panels, monospace font

## Tech Stack

- **React 18** via CDN (UMD production build)
- **Tailwind CSS 3** via CDN
- **Chart.js 4** via CDN
- **Babel Standalone** — JSX transpilation in the browser

No build step required — this is a single `index.html` that can be opened directly or served via GitHub Pages.

## Usage

```bash
# Open directly in browser
open index.html

# Or serve locally
npx serve .
```

## Project Structure

```
CyberMesh-Labs/
├── index.html          # Single-page SOC Dashboard
├── .env.example
├── .github/
│   ├── workflows/      # CI, pages deployment, security scanning
│   └── dependabot.yml
└── README.md
```

## License

MIT — see [LICENSE](./LICENSE).
