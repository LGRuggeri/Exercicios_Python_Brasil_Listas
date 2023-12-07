def byte_megabyte(byte):
    converter= round((byte/1048576),2)
    return converter

def percentagem_megabyte(megabyte,soma):
    percentagem= round((megabyte/sum(soma)*100),2)
    return percentagem