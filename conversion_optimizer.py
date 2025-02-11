def optimize_conversion():
    user_behavior = analyze_user_behavior()
    if user_behavior['cart_abandonment'] > 50:
        display_discount_popup()
    print("Conversion optimization complete.")

def analyze_user_behavior():
    # Exemple d’analyse du comportement utilisateur
    return {'cart_abandonment': 60}

def display_discount_popup():
    print("Displaying a discount popup to reduce cart abandonment.")
