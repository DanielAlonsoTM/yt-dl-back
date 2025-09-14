import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from yt_dlp import YoutubeDL

app = Flask(__name__)
CORS(app, resources={r"/*":{"origin":"http://localhost:3000"}})

@app.route('/ping', methods=['GET'])
def get_tasks():
    app.logger.info('Consulting for service enable')
    return jsonify('pong')

@app.route('/download', methods=['POST'])
def download_link():
    app.logger.info('Consulting for download url`s')

    data = request.json
    app.logger.info(f'Input data: {str(data)}')

    if not data:
        return jsonify({ "error" : "Request was not provided" }), 400

    # Validate and extrac data
    urls = data.get('urls')
    app.logger.info(f'Data url: {str(urls)}')


    if not urls or not isinstance(urls, list):
        return jsonify({ "error" : "'urls' must be a list" }), 400

    try:
        return yt_download(urls), 200

    except Exception as error:
        app.logger.error(f'Error: {str(error)}')
        return jsonify({"error": "Error proccessing request"}), 400

def yt_download(urls: list):
    # Result values
    response_ytdl = []

    # Creation of output folder if doesn't exists
    os.makedirs("downloads", exist_ok=True)

    # Settings for each download
    ydl_opts = {
        'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
        }],
    }

    app.logger.info(f'Settings for yt-dl: {str(ydl_opts)}')

    # Iteration for each url
    for index, url in enumerate(urls):
        app.logger.info(f'[{index}] Downloading url: {url}')

        try:
            # Default result object
            result_element = {
                'url': url,
                'title': '',
                'uploader': '',
                'duration_seconds': '',
                'file_path': '',
                'status': 'error'
            }

            # Call to yt-dl API to download from the url
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url=url, download=True)

                # Extract metada
                title = info_dict.get('title')
                uploader = info_dict.get('uploader')
                duration = info_dict.get('duration')
                filePath = ydl.prepare_filename(info_dict)

                # Generate info about result
                result_element.update({
                    'title': title,
                    'uploader': uploader,
                    'duration_seconds': duration,
                    'file_path': filePath,
                    'status': 'downloaded'
                })
                app.logger.info(f'[{index}] Result: {result_element}')

        except Exception as error:
           app.logger.error(f'Error executing API yt-dl, details: {error}')

        # Added result to the response list
        response_ytdl.append(result_element)

    return response_ytdl

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
