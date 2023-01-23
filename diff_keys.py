def diff_keys(old_dict, new_dict):
    res = {}

    res['kept'] = set(old_dict) & set(new_dict)
    res['added'] = set(old_dict) - set(new_dict)
    res['removed'] = set(old_dict) - set(new_dict)

    return res
