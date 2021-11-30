from pydotnet.clr import CLRApi


def format_row(row):
    return "{0}\t{1}\t{2}\t{3}\t{4:.2f}".format(row.Fund, row.Desk, row.Strategy, row.Key, row.Value)


clr = CLRApi(hostname='127.0.0.1')

obj = clr.new("DataAccessExport.RequestBuilder")

try:
    for i in range(2):
        "{0}\t{1}\t{2}\t{3}\t{4}".format("Fund", "Desk", "Strategy", "Key", "Value")
        for row_measure in obj.GetRowMeasures(r'C:\Users\dharr\OneDrive\Documents\GitHub\homework\BlueCrestRestApi\Data\testResult.json'):
            print(format_row(row_measure))
            print('========================')
            print(clr.callstatic("DataAccessExport.TestStatic", 'CanCallStatic', True))

    print('Done')
except OSError:
    pass
finally:
    clr.close()



