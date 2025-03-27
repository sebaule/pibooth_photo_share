import pibooth
import requests
import logging

__version__ = "1.0.0"

# Configuration du logger
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger('pibooth-photo-share')
logger.setLevel(logging.DEBUG)

@pibooth.hookimpl
def state_processing_exit(app):
#def state_finish_exit(app):
    # Récupérer l'URL générée par Google Photo
    google_photo_url = app.previous_picture_url

    if google_photo_url:
        # Réduire l'URL avec is.gd
        try:
            url = google_photo_url
            api_url = f"https://is.gd/create.php?format=json&url={url}"
            response = requests.get(api_url)

            if response.status_code == 200:
                shortened_url = response.json()["shorturl"]
                app.previous_picture_url = shortened_url  # Remplacer l'URL originale par l'URL réduite
                logger.debug(f"URL réduite : {shortened_url}")
                print(f"URL réduite : {shortened_url}")
            else:
                logger.error(f"Erreur lors de la réduction de l'URL : {response.text}")
        except Exception as e:
            logger.error(f"Erreur lors de la réduction de l'URL : {e}")
    else:
        logger.info("Pas d'URL à réduire")
