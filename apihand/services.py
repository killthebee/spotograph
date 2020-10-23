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
