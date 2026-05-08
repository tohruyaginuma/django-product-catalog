# Django Product Catalog

A Django project that models products, categories, and tags with search and filter functionality.

## Setup

**Requirements**: Python 3.10+

```bash
cp .env.example .env
make install
make migrate
make seed
make up
```

Open http://127.0.0.1:8000

## Commands

| Command | Description |
|---|---|
| `make install` | Create virtualenv and install dependencies |
| `make migrate` | Apply database migrations |
| `make seed` | Populate seed data |
| `make up` | Start development server |
| `make test` | Run tests |
| `make lint` | Run linter (ruff) |
| `make format` | Auto-format code (ruff) |
| `make manage cmd="<command>"` | Run any Django management command |

## Design Notes

**Model relationships**

- `Product` → `Category`: Many-to-one (ForeignKey). A product belongs to exactly one category. This reflects a common catalog design where a product has a single primary classification.
- `Product` ↔ `Tag`: Many-to-many (via `ProductTag`). Tags represent cross-cutting attributes (e.g. "Sale", "New") that can apply to any product regardless of category.

**Service layer**

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
