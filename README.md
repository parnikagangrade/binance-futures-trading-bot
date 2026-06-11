# Binance Futures Trading Bot

## Overview

A Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Input validation
- Error handling
- Logging
- Binance Futures Testnet integration

## Setup

1. Clone repository

```bash
git clone <repository-url>
cd trading_bot
```

2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure API credentials

Create `.env`

```env
API_KEY=your_api_key
API_SECRET=your_secret_key
```

## MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

## Project Structure

trading_bot/
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
├── cli.py
├── README.md
├── requirements.txt
└── .env

## Assumptions

- Binance Futures Testnet account is configured.
- API credentials are valid.
- User has sufficient test funds.