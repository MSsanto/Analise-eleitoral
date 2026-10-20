import { render, screen } from '@testing-library/react';

import HomePage from '../app/page';

describe('HomePage', () => {
  it('renders the analytical product identity and quality gates', () => {
    render(<HomePage />);

    expect(
      screen.getByRole('heading', { level: 1, name: 'Análise Eleitoral 2026' }),
    ).toBeInTheDocument();
    expect(screen.getByText('Testes automatizados')).toBeInTheDocument();
    expect(screen.getByText('Revisão por Pull Request')).toBeInTheDocument();
  });
});
