"""
Pocket Option Bot - Synchronous Version (No asyncio)
"""

from BinaryOptionsToolsV2 import PocketOption
import time

# Your SSID
SSID = '42["auth",{"session":"90dcda6b139fe52217664e80d6930ace","isDemo":1,"uid":88209425,"platform":2,"isFastHistory":true,"isOptimized":true}]'

print("=" * 50)
print("🚀 Pocket Option Bot (Synchronous)")
print("=" * 50)

try:
    print("\n[1] Creating client...")
    client = PocketOption(ssid=SSID)
    print("   ✅ Client created")
    
    print("\n[2] Connecting...")
    client.connect()
    print("   ✅ Connected!")
    
    print("\n[3] Getting balance...")
    balance = client.balance()
    print(f"   ✅ Balance: ${balance}")
    
    print("\n[4] Getting candles...")
    candles = client.get_candles("EURUSD_otc", 60, 10)
    print(f"   ✅ Got {len(candles)} candles")
    
    if candles:
        print(f"   Latest candle: {candles[-1]}")
    
    print("\n[5] Keeping connection alive...")
    print("   Press Ctrl+C to stop")
    
    while True:
        time.sleep(30)
        print("   💓 Heartbeat - Bot alive")
        
except KeyboardInterrupt:
    print("\n   Stopping...")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    try:
        client.close()
        print("   ✅ Disconnected")
    except:
        pass
