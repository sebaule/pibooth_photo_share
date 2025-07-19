# pibooth_photo_share

Ce plugin, à destination de PiBooth, permet de réduire les liens générés par le plugin pibooth-google-photo.
En effet lorsqu'on envoie au plugin pibooth-qrcode le lien google de la photo uploadé, celui-ci est énorme et il est impossible de le scanner...

Mon plugin permet donc de réduite cette url et d'afficher un QRCode scannable.

Pour l'intégrer, faire un copier/coller du fichier pibooth_photo-share.py sur votre serveur PiBooth.
Par exemple dans :
- ~/pibooth_plugins/pibooth_photo_share.py

Modifier le fichier de configuration
- ~/.config/pibooth/piboof.cfg
Ajouter la déclaration du plugin :
- plugins = ~/pibooth_plugins/pibooth_photo-share.py

Pour que celui-ci puisse fonctionner et être appelé, il faudra modifier le code du plugin pibooth-google-photo pour qu'il s'applique en premier :
- Editer le fichier pibooth_google_photo.py
  o Ajouter **(tryfirst=True)** dans l'event state_processing_exit

Vouc devriez obtenir ceci :
  @pibooth.hookimpl(tryfirst=True)
  def state_processing_exit(cfg, app):

En faisant cela, les **enchainements des plugins** sur l'événement **sate_processing_exit** sera le suivant :
1. pibooth-google-photo
2. pibooth_photo_share
3. pibooth-qrcode





