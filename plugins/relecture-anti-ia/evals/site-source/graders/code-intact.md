---
type: regex
pattern: 'export default function Hero\(\{ city \}\)[\s\S]*<section className="hero hero--dark" data-track="hero">[\s\S]*\{city\}[\s\S]*<img src="/team\.jpg" alt="[^"]*" />[\s\S]*<a href="/contact" className="btn">'
target: { source: file, path: src/Hero.jsx }
---
