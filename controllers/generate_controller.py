from flask import jsonify, request, url_for
import base64
import time
import pdfkit


class GenerateController:
    @staticmethod
    def generate():
        data = request.get_json()
        html = data.get("html")

        if html:
            # Decode base64-encoded HTML
            decoded_html = base64.b64decode(html).decode('utf-8')

            # Generate a unique name for the PDF file
            filename = f"generated/{int(time.time())}_file.pdf"

            pdfkit.from_string(decoded_html, filename)

            # Return the PDF file URL
            file_url = url_for('static', filename=filename, _external=True)
            return jsonify({"status": "success", "url": file_url}), 200

        return jsonify({"error": "bad request"}), 400