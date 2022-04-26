
def model_list_to_json(lis, cls=None):
    return list(map(lambda u: u.to_json(), lis))
