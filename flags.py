def toggle(arg, flags):
    if arg in flags:
        flags.discard(arg)
    else:
        flags.add(arg)


def toggled(arg, flags):
    flags2 = flags.copy()

    if arg in flags:
        flags2.discard(arg)
    else:
        flags2.add(arg)
    return flags2

