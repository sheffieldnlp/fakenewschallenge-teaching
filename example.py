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

    #Test data will be provided in week 10
    for stance in test_data:
        print(stance)
        print(dataset.articles[stance['Body ID']])
        print("")
            
    #Example scorer - THIS WONT RUN UNTIL YOU HAVE MADE YOUR PREDICTIONS
    #predicted = ['unrelated','discuss',...] #these will come from labels you predict on the dev/test data
    #actual = [stance['Stance'] for stance in dev_data]
    
    #THIS WILL THROW AN ERROR IF THE NUMBER OF SAMPLES IN THE PREDICTED IS DIFFERENT FROM THE NUMBER OF SAMPLES IN THE ACTUAL
    #assert len(predicted)==len(actual), "Number of predictions should match the number of dev data"
    #report_score(actual, predicted)
