# Phase 4 — Visualization

**Goal:** Communicate the Phase 3 findings **visually** using Matplotlib (Day 7) and Seaborn
(Day 8). The core discipline: **every chart answers one question — never decoration.**

## Run it

```bash
python phase4_visualization.py
```

The script uses Matplotlib's `Agg` backend, so it **saves 6 PNG files** into this folder even
on a machine with no display.

## The chart-selection table

| File | Chart type | Why chosen | What it reveals |
|------|-----------|-----------|-----------------|
| `chart_01_revenue_by_category.png` | Bar | Compare distinct categories | Top-earning category (Electronics) |
| `chart_02_revenue_by_city.png` | Bar | Compare distinct cities | Strongest market (Pune) |
| `chart_03_amount_distribution.png` | Histogram | Spread of one numeric variable | Most orders small; a few large ones drive revenue |
| `chart_04_amount_by_category_box.png` | Box plot | Spread + auto outlier flag | Electronics = highest, most variable amounts |
| `chart_05_quantity_vs_amount.png` | Scatter (hue=Category) | Relationship of two numerics | Two distinct buying patterns |
| `chart_06_correlation_heatmap.png` | Heatmap | Visualize correlation matrix | Quantifies the weak Amount↔Quantity link |

## The rule to remember

> **Match the chart to the question:**
> - Compare categories → **bar**
> - Distribution of one variable → **histogram / box plot**
> - Relationship between two variables → **scatter**
> - A correlation matrix → **heatmap**

Each chart here maps directly back to a Phase 3 finding and forward to a Phase 6 insight.
