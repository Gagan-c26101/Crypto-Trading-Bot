import asyncio

import octobot_commons.symbols as symbols
import octobot_commons.os_util as os_util

import triangular_arbitrage.detector as detector

if __name__ == "__main__":
    if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    benchmark = os_util.parse_boolean_environment_var("IS_BENCHMARKING", "False")
    if benchmark:
        import time

        s = time.perf_counter()

   
    print("Scanning...")
    exchange_name = "bybit"  

    best_opportunities, best_profit = asyncio.run(detector.run_detection(exchange_name))

    def opportunity_symbol(opportunity):
        return symbols.parse_symbol(str(opportunity.symbol))


    def get_order_side(opportunity: detector.ShortTicker):
        return 'buy' if opportunity.reversed else 'sell'


    if best_opportunities is not None:
        print("-------------------------------------------")
        total_profit_percentage = round((best_profit - 1) * 100, 5)
        print(f"New {total_profit_percentage}% {exchange_name} opportunity:")
        for i, opportunity in enumerate(best_opportunities):
             base_currency = opportunity.symbol.base
             quote_currency = opportunity.symbol.quote
             order_side = get_order_side(opportunity)
        print(
                f"{i + 1}. {order_side} {base_currency} "
                f"{'with' if order_side == 'buy' else 'for'} "
                f"{quote_currency} at {opportunity.last_price:.5f}")
        print("-------------------------------------------")
    else:
        print("No opportunity detected")

    if benchmark:
        elapsed = time.perf_counter() - s
        print(f"{__file__} executed in {elapsed:0.2f} seconds.")