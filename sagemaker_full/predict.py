# predict.py

from logger import logger

def predict(predictor, payload):
    logger.info("Making a prediction...")
    response = predictor.predict(payload)
    logger.info(f"Prediction: {response}")
    return response
