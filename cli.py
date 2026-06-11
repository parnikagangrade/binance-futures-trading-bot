import argparse
import logging

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    if not validate_side(args.side):
        raise ValueError("Side must be BUY or SELL")

    if not validate_order_type(args.type):
        raise ValueError("Type must be MARKET or LIMIT")

    if not validate_quantity(float(args.quantity)):
        raise ValueError("Quantity must be positive")

    if args.type.upper() == "MARKET":

        response = place_market_order(
            args.symbol,
            args.side,
            float(args.quantity)
        )

    else:

        if not args.price:
            raise ValueError(
                "Price required for LIMIT order"
            )

        response = place_limit_order(
            args.symbol,
            args.side,
            float(args.quantity),
            args.price
        )

    print("\nORDER SUCCESSFUL\n")
    print(response)

    logging.info(response)

except Exception as e:

    logging.error(str(e))

    print("ERROR:", e)