from flask import jsonify, request
import logging

class HomeController:
    @staticmethod
    def home():
        logging.info("Some Information")
        logging.debug("some debug")
        print("wahala")
        return jsonify({"app": "Flask Api Running", "Version": "0"})