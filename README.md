# Insify

A music streaming platform where you can share reels from insta and get the song directly.

A music streaming PWA built with a monorepo architecture. The project consists of a Next.js web frontend, a NestJS API backend, and a FastAPI fingerprinting service.

## Getting Started

### Prerequisites
- Node.js 20+
- Python 3.11+
- npm

### Installation

```bash
# Install all npm dependencies
npm install

# Install Python dependencies for fingerprint service
cd fingerprint && pip install -r requirements.txt
```

### Running Locally

Run each service in a separate terminal:

**Frontend (Next.js) - runs on http://localhost:3000**
```bash
npm run dev:frontend
```

**Backend (NestJS) - runs on http://localhost:3001**
```bash
npm run dev:backend
```

**Fingerprint (FastAPI) - runs on http://localhost:8000**
```bash
npm run dev:fingerprint
```

### Project Structure

```
insify/
├── frontend/           # Next.js PWA (TypeScript, App Router, Tailwind)
├── backend/            # NestJS API (TypeScript)
├── fingerprint/        # FastAPI service (Python)
├── packages/
│   └── shared-types/   # Shared TypeScript types
├── package.json        # Root workspace config
└── .env.example        # Environment variables template
```