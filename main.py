import asyncio

import octobot_commons.symbols as symbols
import octobot_commons.os_util as os_util

import triangular_arbitrage.detector as detector

if __name__ == "__main__":
    if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 
    
    
        import time

        s = time.perf_counter()

   
    print("Scanning...")
    exchange_name = "bybit"  

    best_opportunities, best_profit = asyncio.run(detector.run_detection(exchange_name))
