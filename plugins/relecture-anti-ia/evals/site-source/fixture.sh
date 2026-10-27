#!/bin/bash
set -e
mkdir -p src
cat > src/Hero.jsx <<'JSX'
export default function Hero({ city }) {
  return (
    <section className="hero hero--dark" data-track="hero">
      <h1>Votre partenaire au cœur de la transformation digitale</h1>
      <p>Basés à {city} depuis 2018, nous accompagnons 40 entreprises.</p>
      <img src="/team.jpg" alt="Image de notre équipe" />
      <a href="/contact" className="btn">N'hésitez pas à nous contacter</a>
    </section>
  );
}
JSX
git init -q && git add -A && git -c user.email=e@e -c user.name=e commit -qm init
