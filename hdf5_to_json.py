import h5py
import json
import io


filename = 'sensor_records.hdf5'
treePath = 'trajectory_0000/gps/position'

f = h5py.File(filename, 'r')


# Get the data
data = f[treePath]

data = data[()].tolist()

with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(str(str_))
