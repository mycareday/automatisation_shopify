import facebook
import google.ads

def manage_ads():
    create_facebook_ad_campaign()
    create_google_ad_campaign()

def create_facebook_ad_campaign():
    # Création de la campagne Facebook Ads
    campaign = facebook.create_campaign("Nom de la campagne")
    print(f"Facebook Campaign {campaign.id} created.")

def create_google_ad_campaign():
    # Création de la campagne Google Ads
    campaign = google.ads.create_campaign("Nom de la campagne")
    print(f"Google Ads Campaign {campaign.id} created.")
