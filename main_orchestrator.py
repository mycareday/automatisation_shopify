import time
from scraper_tiktok import scrape_tiktok_trends
from product_manager import manage_products
from order_handler import handle_orders
from ads_manager import manage_ads
from conversion_optimizer import optimize_conversion
from security_proxy import secure_connection
from dashboard import start_dashboard

def main():
    while True:
        try:
            scrape_tiktok_trends()
            manage_products()
            handle_orders()
            manage_ads()
            optimize_conversion()
            secure_connection()
            start_dashboard()
            time.sleep(60)  # Pause before next cycle
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(60)  # Retry after waiting

if __name__ == "__main__":
    main()
