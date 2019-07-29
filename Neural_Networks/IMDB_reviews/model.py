import keras
import os

data_path_train_pos = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\\train\pos"
data_path_train_neg = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\\train\\neg"
data_path_test_pos = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\\test\pos"
data_path_test_neg = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\\test\\neg"

print(os.listdir(data_path_train_pos)[:5])
