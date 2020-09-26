from run import db


def add_to_db(objects):
    """
    Safely adds objects to the Documents Database, rolls back if it encounters any error

    :param objects: array of objects to be added to the database
    """
    for obj in objects:
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as ex:
            print(ex)
            db.session.rollback()

    return objects


def remove_from_db(objects):
    """
    Safely removes objects from the Documents Database, rolls back if it encounters any error

    :param objects: array of objects to be removed from the database
    """
    for obj in objects:
        try:
            db.session.delete(obj)
            db.session.commit()
        except Exception as ex:
            print(ex)
            db.session.rollback()
