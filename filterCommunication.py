def checkSrc(conf_file, src_addr):
    """
    Checks source ip against allowed ip table.
    Returns True if passed check, False otherwise.
    """
    with open(confFile) as conf_file:
        ip_table = conf_file.read()
    return src_addr in ip_table
