import h5py
import json
import io

filename = 'sensor_records.hdf5'
treePath = 'trajectory_0000/imu/gyroscope'

f = h5py.File(filename, 'r')

# Get the data
data = f[treePath]

data = data[()].tolist()

with io.open('gyroscope_data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(str(str_))
