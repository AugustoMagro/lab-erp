from pathlib import Path
import requests
import os

BOOTSTRAP_STATIC_FILES = {
    "bootstrap.min.css":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
}

class DownloadStatic:
    def __init__(self):
        print("Downloading")

        BASE_DIR = Path(__file__).resolve().parent
        
        BASE_DIR_STATICFILES = BASE_DIR / "static"

        out_path_css = BASE_DIR_STATICFILES / "staticBootstrap.css"
        out_path_js1 = BASE_DIR_STATICFILES / "staticBootstrap1.js"
        out_path_js2 = BASE_DIR_STATICFILES / "staticBootstrap2.js"

        url1 = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        url2 = "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
        url3 = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
        
        DownloadStatic.download_to_local(url1, out_path_css)
        DownloadStatic.download_to_local(url2, out_path_js1)
        DownloadStatic.download_to_local(url3, out_path_js2)

    def download_to_local(url:str, out_path:Path, parent_mkfir:bool=True):
        if not isinstance(out_path, Path):
            raise ValueError(f"{out_path} must be a valid pathlib")
        if parent_mkfir:
            out_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            response = requests.get(url)
            response.raise_for_status()
            out_path.write_bytes(response.content)
            print("Downloaded")
            return True
        except requests.RequestException as e:
            print(f'Failed to download {url}: {e}')
            return False
        
if __name__ == "__main__":
    DownloadStatic()