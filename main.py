import MetaTrader5 as mt5
import time
import pandas as pd

# --- إعدادات الحساب ---
ACCOUNT_ID = 12345678  # رقم حسابك
PASSWORD = "YourPassword"
SERVER = "Exness-MT5-Real"
MAGIC = 123456

def initialize_mt5():
    if not mt5.initialize():
        print("فشل الاتصال بـ MT5")
        return False
    
    authorized = mt5.login(ACCOUNT_ID, password=PASSWORD, server=SERVER)
    if authorized:
        print("تم تسجيل الدخول بنجاح")
    else:
        print(f"فشل الدخول، الخطأ: {mt5.last_error()}")
    return authorized

def get_signal():
    # هنا يتم وضع منطق المتوسطات و RSI كما في كود MQL5
    # نقوم بجلب البيانات التاريخية وتحليلها
    rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M15, 0, 100)
    df = pd.DataFrame(rates)
    
    # حساب المتوسطات (مثال مبسط)
    fast_ma = df['close'].rolling(window=10).mean().iloc[-1]
    slow_ma = df['close'].rolling(window=30).mean().iloc[-1]
    
    if fast_ma > slow_ma:
        return "BUY"
    elif fast_ma < slow_ma:
        return "SELL"
    return None

def run_bot():
    if not initialize_mt5(): return
    
    while True:
        signal = get_signal()
        print(f"الإشارة الحالية: {signal}")
        # هنا تضع أوامر تنفيذ الصفقات mt5.order_send()
        time.sleep(60) # فحص كل دقيقة

if __name__ == "__main__":
    run_bot()
