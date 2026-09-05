const qualityGates = [
  'Snapshot analítico versionado',
  'Testes automatizados',
  'Build de produção',
  'Revisão por Pull Request',
];

export default function HomePage() {
  return (
    <main className="shell">
      <header className="hero">
        <p className="eyebrow">DADOS PÚBLICOS · METODOLOGIA AUDITÁVEL</p>
        <h1>Análise Eleitoral 2026</h1>
        <p className="lede">
          Nova camada web para explorar métricas eleitorais com rastreabilidade,
          neutralidade e gates explícitos de qualidade.
        </p>
      </header>

      <section aria-labelledby="quality-title" className="panel">
        <h2 id="quality-title">Qualidade da entrega</h2>
        <ul>
          {qualityGates.map((gate) => (
            <li key={gate}>{gate}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}
