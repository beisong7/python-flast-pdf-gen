from flask import jsonify, request
import base64
import time
import pdfkit
import os
import logging


class GenerateController:
    @staticmethod
    def generate():
        data = request.get_json()
        html = data.get("html")

        if html:
            # Decode base64-encoded HTML
            decoded_html = base64.b64decode(html).decode('utf-8')

            # Use an absolute path for the generated directory
            current_dir = os.path.abspath(os.path.dirname(__file__))
            root_dir = os.path.abspath(os.path.join(current_dir, '../'))
            generated_dir = os.path.join(root_dir, 'generated')
            os.makedirs(generated_dir, exist_ok=True)

            # Generate a unique name for the PDF file
            file_name = f"{int(time.time())}_file.pdf"
            file_path = os.path.join(generated_dir, file_name)

            logging.debug(file_path)
            logging.info(file_path)
            print("get path")
            print(file_path)
            print(file_name)

            try:
                # Generate PDF from HTML content
                pdfkit.from_string(decoded_html, file_path)

                # Serve the file URL
                
                file_url = f"{request.host_url}generated/{file_name}"
                return jsonify({"status": "success", "url": file_url, "file_path": file_path, "current_dir": current_dir, "root_dir": root_dir, "generated_dir": generated_dir}), 200

            except OSError as e:
                return jsonify({"error": f"Failed to generate PDF: {str(e)}"}), 500

        return jsonify({"error": "bad request"}), 400