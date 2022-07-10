import pickle
import pandas

with open("./ted_gesture_dataset/ted_gesture_dataset_train.pickle", "rb") as fr:
    data = pickle.load(fr)

df = pandas.DataFrame(data)
df.to_csv('train_file.csv')