def apply_diff(target, diff):
    if 'add' in diff.keys():
        target.update(diff['add'])
    if 'remove' in diff.keys():
        target.difference_update(diff['remove'])
