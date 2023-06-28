def checkSrc(conf_file, src_addr):
    """
    Checks source ip against allowed ip table.
    Returns True if passed check, False otherwise.
    """
    with open(conf_file) as file:
        ip_table = file.read()
    return src_addr in ip_table
