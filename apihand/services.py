from django.core.files.base import ContentFile
from urllib import request as rq

def valid_coord(coord):
    """
    validate coord
    :param coord: int or string
    :return: bool
    """
    try:
        if coord >= -90 and coord <= 90:
            return True
    except TypeError:
        return False
    return False


def fetch_imgs_files(main_img_data_uri, secondary_imgs_data_uri):
    main_image = None
    if main_img_data_uri:
        try:
            with rq.urlopen(main_img_data_uri) as response:
                data = response.read()
                main_image = ContentFile(data)
        except:
            pass
    secondary_imgs = []
    for data_uri in secondary_imgs_data_uri:
        try:
            with rq.urlopen(main_img_data_uri) as response:
                data = response.read()
                secondary_imgs.append(ContentFile(data))
        except:
            pass
    return main_image, secondary_imgs
