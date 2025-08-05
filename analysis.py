"""Stub script for agentic financial modelling and stock analysis.

This script demonstrates the overall structure of an agentic financial
modelling workflow.  It includes functions for data retrieval,
preprocessing, model prediction and summarisation.  At present each
function logs its actions and returns dummy results; replace the
placeholder logic with real code to build a working system.
"""

import argparse
import logging
from dataclasses import dataclass
from typing import List, Tuple

logger = logging.getLogger(__name__)


def fetch_market_data(symbol: str, start: str = "2020-01-01", end: str = "2025-01-01") -> List[Tuple[str, float]]:
    """Fetch historical price data for a stock symbol.

    Parameters
    ----------
    symbol : str
        Ticker symbol (e.g. "AAPL").
    start : str
        Start date in YYYY-MM-DD format.
    end : str
        End date in YYYY-MM-DD format.

    Returns
    -------
    list of (date, price)
        A list of tuples with ISO date strings and closing prices.
    """
    logger.info("Fetching market data for %s from %s to %s", symbol, start, end)
    # TODO: integrate with a real data provider (e.g. yfinance, Alpha Vantage)
    # Return dummy data: a simple upward trend
    return [(f"2020-01-{day:02d}", 100 + day) for day in range(1, 31)]


def preprocess_data(data: List[Tuple[str, float]]) -> List[float]:
    """Preprocess raw market data into a sequence suitable for modelling.

    Currently this stub simply extracts the price values.

    Parameters
    ----------
    data : list of (date, price)
        Raw market data.

    Returns
    -------
    list of float
        Preprocessed price series.
    """
    logger.info("Preprocessing %d data points", len(data))
    return [price for _, price in data]


def predict_next_price(series: List[float]) -> float:
    """Predict the next price in the series.

    This stub returns the last observed value.  Replace it with a
    meaningful model such as an ARIMA, LSTM or transformer model.

    Parameters
    ----------
    series : list of float
        Historical price series.

    Returns
    -------
    float
        Predicted next price.
    """
    logger.info("Predicting next price from series of length %d", len(series))
    return series[-1] if series else 0.0


def generate_report(symbol: str, prediction: float) -> str:
    """Generate a narrative summary of the analysis.

    Parameters
    ----------
    symbol : str
        The stock symbol analysed.
    prediction : float
        The predicted next price.

    Returns
    -------
    str
        A report summarising the analysis.
    """
    report = (
        f"Analysis for {symbol}:\n"
        f"The forecasted next closing price is approximately ${prediction:.2f}.\n"
        "This is a placeholder report; integrate real models for actionable insights."
    )
    logger.debug("Generated report: %s", report)
    return report


def run_pipeline(symbol: str) -> str:
    data = fetch_market_data(symbol)
    series = preprocess_data(data)
    prediction = predict_next_price(series)
    report = generate_report(symbol, prediction)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Agentic financial modelling stub")
    parser.add_argument("--symbol", required=True, help="Stock symbol to analyse")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    report = run_pipeline(args.symbol)
    print(report)


if __name__ == "__main__":
    main()