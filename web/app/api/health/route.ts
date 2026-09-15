import { NextResponse } from 'next/server';

export function GET() {
  return NextResponse.json({
    status: 'ok',
    service: 'analise-eleitoral-web',
    version: '0.1.0',
  });
}
