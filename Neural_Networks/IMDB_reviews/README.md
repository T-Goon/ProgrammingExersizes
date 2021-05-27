# IMDB Reviews

Trains a neural netork model on the IMDB Reviews data set to predict whether movie reviews are positive or negative. Positive is defined as having a rating of > 5 and 
negative is defined as having a rating of <= 5.

## Model

1. The first layer is an embedding of the dictionary of words used in the reviews data set.
2. LSTM (Long Short Term Memory) layer of length equal to the review with the largest number of words.
3. Dense layer of length 1.

Output: 1 if the review is positive. 0 if the review is negative.

## File Structure

- Data for the positive training samples should be stored in: "aclImdb/train/pos/"
- Data for the negative training samples should be stored in: "aclImdb/train/neg/"
- Data for the positive testing samples should be stored in: "aclImdb/test/pos/"
- Data for the negative testing samples should be stored in: "aclImdb/test/neg/"

![image](https://user-images.githubusercontent.com/32044950/119889968-3c291880-bf05-11eb-902c-c470a23b175b.png)
