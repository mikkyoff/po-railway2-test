"""
Eagle Lenz - Pocket Option Bot for Railway (Python 3.11)
"""

import asyncio
import nest_asyncio
from BinaryOptionsToolsV2 import PocketOption

# Apply nest_asyncio to allow nested event loops
try:
    nest_asyncio.apply()
except ImportError:
    pass

SSID = '42["auth",{"session":"90dcda6b139fe52217664e80d6930ace","isDemo":1,"uid":88209425,"platform":2,"isFastHistory":true,"isOptimized":true}]'

def run_bot():
    print("🚀 Railway Bot Starting...")
    
    # Use synchronous client (no asyncio issues)
    client = PocketOption(ssid=SSID)
    print("   ✅ Client created")
    
    client.connect()
    print("   ✅ Connected to Pocket Option!")
    
    balance = client.balance()
    print(f"   ✅ Balance: ${balance}")
    
    candles = client.get_candles("EURUSD_otc", 60, 5)
    print(f"   ✅ Got {len(candles)} candles")
    
    print("   ✅ Bot is running...")
    
    # Keep the bot alive
    import time
    while True:
        time.sleep(60)
        print("   Heartbeat - Bot still running")

if __name__ == "__main__":
    run_bot()
