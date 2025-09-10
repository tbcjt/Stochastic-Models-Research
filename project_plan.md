# Project Plan

## Hypothesis
Certain statistical and machine learning models can generate excess returns when applied to liquid equity markets with realistic transaction costs.

## Research questions
- How well do parametric models (GBM, GARCH, OU) describe real asset returns compared to ML methods?
- Can volatility modelling improve portfolio risk-adjusted returns?
- What robustness checks are needed to validate strategy performance?

## Metrics
- Primary: Out-of-sample Sharpe ratio > 1.0
- Secondary: Max drawdown < 20%, turnover < 2x monthly

## Focus
- Top 100 US equities (daily data from Yahoo Finance via `yfinance`)
- Frequency: Daily close prices

## Deliverables
- Jupyter notebooks (analysis, backtests)
- Research paper (8–10 pages)
- Final strategy implementation with backtests and robustness checks

