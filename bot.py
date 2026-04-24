"""
Pocket Option Bot with WebSocket 11.0 fix
"""

import asyncio
from BinaryOptionsToolsV2 import PocketOption

# Your SSID
SSID = '42["auth",{"session":"90dcda6b139fe52217664e80d6930ace","isDemo":1,"uid":88209425,"platform":2,"isFastHistory":true,"isOptimized":true}]'

async def main():
    print("=" * 50)
    print("🚀 Pocket Option Bot (WebSocket 11.0)")
    print("=" * 50)
    
    client = PocketOption(ssid=SSID)
    print("[1] Client created")
    
    await client.connect()
    print("[2] Connected!")
    
    balance = await client.get_balance()
    print(f"[3] Balance: ${balance}")
    
    candles = await client.get_candles("EURUSD_otc", 60, 10)
    print(f"[4] Got {len(candles)} candles")
    
    await client.close()
    print("[5] Done!")

if __name__ == "__main__":
    asyncio.run(main())
