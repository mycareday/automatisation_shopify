import shopify

def handle_orders():
    orders = shopify.Order.find(fulfilled=False)  # Trouve les commandes non remplies
    for order in orders:
        process_order(order)

def process_order(order):
    # Processus de validation de commande
    order.fulfill()
    print(f"Order {order.id} processed.")
    track_shipping(order)
    
def track_shipping(order):
    # Ajouter un suivi pour les livraisons
    tracking_url = "http://trackingexample.com/" + str(order.id)
    print(f"Order {order.id} shipping: {tracking_url}")
