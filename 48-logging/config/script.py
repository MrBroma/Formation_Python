import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="48-logging/config/app.log", # ou le chemin complet
                    filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")

