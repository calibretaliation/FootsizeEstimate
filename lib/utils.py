import wget

def download_images(url, save_dir):
    return wget.download(url, out = save_dir)

def create_dataset():
    #Need images, labels from metadata
    #TODO
    pass
