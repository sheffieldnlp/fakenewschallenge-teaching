from utils.dataset import DataSet
from utils.generate_test_splits import split

d = DataSet()
data_splits = split(d)

training = data_splits['training']
dev = data_splits['dev']
test = data_splits['test']

for stance in training:
    print(stance)
    print(d.articles[stance['Body ID']])
    print("")


for stance in dev:
    print(stance)
    print(d.articles[stance['Body ID']])
    print("")


for stance in test:
    print(stance)
    print(d.articles[stance['Body ID']])
    print("")
