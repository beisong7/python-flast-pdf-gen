from flask import jsonify, request, url_for
import base64
import time
import pdfkit
import os


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
            generated_dir = os.path.join(root_dir, '..', 'generated')
            os.makedirs(generated_dir, exist_ok=True)

            # Generate a unique name for the PDF file
            filename = f"{int(time.time())}_file.pdf"
            file_path = os.path.join(generated_dir, filename)

            try:
                # Generate PDF from HTML content
                pdfkit.from_string(decoded_html, file_path)

                # Serve the file URL
                file_url = url_for('generated', filename=f'{filename}', _external=True)
                return jsonify({"status": "success", "url": file_url}), 200

            except OSError as e:
                return jsonify({"error": f"Failed to generate PDF: {str(e)}"}), 500

        return jsonify({"error": "bad request"}), 400