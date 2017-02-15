from utils.dataset import DataSet
from utils.generate_test_splits import split
from utils.score import report_score

dataset = DataSet()
data_splits = split(dataset)

training_data = data_splits['training']
dev_data = data_splits['dev']
test_data = data_splits['test']



if __name__ == '__main__':
    for stance in training_data:
        print(stance)
        print(dataset.articles[stance['Body ID']])
        print("")


    for stance in dev_data:
        print(stance)
        print(dataset.articles[stance['Body ID']])
        print("")


    for stance in test_data:
        print(stance)
        print(dataset.articles[stance['Body ID']])
        print("")
