# Django Product Catalog

A Django project that models products, categories, and tags with search and filter functionality.

## Setup

**Requirements**: Python 3.10+

```bash
cp .env.example .env
make install
make setup
make up
```

Open http://127.0.0.1:8000

## Commands

| Command | Description |
|---|---|
| `make install` | Create virtualenv and install dependencies |
| `make setup` | Apply migrations and populate sample data |
| `make migrate` | Apply database migrations only |
| `make up` | Start development server |
| `make test` | Run tests |

## Design Notes

Services are split by responsibility:
- `category_service`, `tag_service`: single aggregate operations
- `product_query_service`: cross-aggregate query (Product + Category + Tag)

## AI Usage

This project was developed with Claude Code assistance. All code has been reviewed and understood by the author. AI was used for:
- Discussing design decisions:
  - Service layer structure
  - Error handling
  - Model explicitness
  - Frontend design
- Creating Makefile and README
