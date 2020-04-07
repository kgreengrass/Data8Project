from files_to_dataframe import FileToDF


def phonenoformat(bucket, folder, col):
    file = FileToDF(bucket,folder)
    df = file.dataframecsv()
    df[col]=df[col].astype(str)
    chars = ' ()-'
    for c in chars:
        df[col] = df[col].str.replace(c,'')
    return df
