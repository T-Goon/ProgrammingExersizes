import tensorflow as tf
from tensorflow import keras
import numpy as np
import gym
import random
import math

GAMMA = .99
BATCH_SIZE = 50
LAMBDA = .0001
MAX_EPS = 1
MIN_EPS = .01

class Model:
    # num_states: number of items that make up the state in the envirnment
    # num_actions: number of actions that are possible in the game
    def __init__(self, num_states, num_actions, batch_size):
        self._num_states = num_states
        self._num_actions = num_actions
        self._batch_size = batch_size

        self.defModel()

    def defModel(self):
        # NN with 2 dense layers
        input = keras.layers.Input(shape=(self._num_states,))
        d1 = keras.layers.Dense(50, activation='relu')(input)
        d2 = keras.layers.Dense(20, activation='relu')(d1)
        d3 = keras.layers.Dense(self._num_actions)(d2)

        self.model = keras.Model(inputs=input, outputs=d3)
        self.model.compile(optimizer='Adam', loss='mse')

    def train_batch(self, train_x, train_y):
        self.model.fit(train_x, train_y, batch_size=self._batch_size, verbose=0)

    def predict(self, state):
        return self.model.predict(state.reshape(1, self.num_states))

    def predict_batch(self, states):
        return self.model.predict_on_batch(states)

    @property
    def num_states(self):
        return self._num_states

    @property
    def num_actions(self):
        return self._num_actions

    @property
    def batch_size(self):
        return self._batch_size

# Storage for previos states in the game
# Used to train model
class Memory:
    # Init with a max number of samples that it can store
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = list()

    def add_sample(self, sample):
        self.data.append(sample)
        # Removes the oldest item if memory is at capacity
        if len(self.data) > self.max_size:
            self.data.pop(0)

    def get_samples(self, num_samples):
        # Return num_samples number of random sample from memory
        # if there are not enough samples in memory return what it has
        if len(self.data) < num_samples:
            return random.sample(self.data, len(self.data))
        else:
            return random.sample(self.data, num_samples)

class GameRunner:
    def __init__(self, model, env, memory, max_eps, min_eps, eps_decay_fac, render=True):
        # Game envirnment, model, and memory classes
        self._env = env
        self._model = model
        self._memory = memory

        # Variables for epsilon greedy policy
        self._min_eps = min_eps
        self._max_eps = max_eps
        self._eps_decay_fac = eps_decay_fac
        self._eps = self._max_eps

        self._render = render
        self._steps = 0
        self._best_run = 0

    def run(self):
        state = self._env.reset()
        steps = 0

        # Game loop
        while(True):
            steps+=1

            if self._render:
                self._env.render()

            # Have the agent take an action in the game
            action = self.choose_action(state)
            new_state, reward, done, info = self._env.step(action)

            # increase reward for keeping the pole strait
            if abs(new_state[2]) < .05:
                reward += 10
            elif abs(new_state[2]) < .1:
                reward += 5
            elif abs(new_state[2]) < 1.5:
                reward += 1

            if done or steps == 200:
                new_state = None

            # After each action add it to memory and train the model
            self._memory.add_sample((state, action, reward, new_state))
            self.train()

            # Exponentially decay the epsilon factor
            self._steps += 1
            self._eps = MIN_EPS + (MAX_EPS - MIN_EPS) \
                                      * math.exp(-LAMBDA * self._steps)

            state = new_state

            if(steps > self._best_run):
                self._best_run = steps

            if done or steps == 200:
                break

        return steps

    # Train the model with a batch of data
    def train(self):
        # Get data from memory
        batch = self._memory.get_samples(self._model.batch_size)

        # Seperate out the state and new states from data
        states = np.array([i[0] for i in batch])
        new_states = np.array([(np.zeros(self._model.num_states)
                                 if val[3] is None else val[3]) for val in batch])

        # From the states get the Q values
        q_old = self._model.predict_batch(states)
        q_new = self._model.predict_batch(new_states)

        # np array to hold the training data
        x = np.zeros((self._model.batch_size, self._model.num_states))
        y = np.zeros((self._model.batch_size, self._model.num_actions))

        for i, b in enumerate(batch):
            state, action, reward, new_state = b[0], b[1], b[2], b[3]

            # Q value for each data sample
            q = q_old[i]

            # Update Q value of the action taken based on future rewards
            # if the game is over don't
            if new_state is None:
                q[action] = reward
            else:
                q[action] = reward + GAMMA * np.amax(q_new[i])

            # add values to training data
            x[i] = state
            y[i] = q

        self._model.train_batch(x, y)

    def choose_action(self, state):
        # Choose random action on a chance based on epsilon
        if random.random() < self._eps:
            return random.randint(0,1)
        # Have the model choose the action
        else:
            return np.argmax(self._model.predict(state))

    # Show the model playing the game
    def playGame(self):
        steps = 0
        while(True):
            state = self._env.reset()
            steps +=1
            self._env.render()
            action = self.choose_action(state)
            state, reward, done, info = self._env.step(action)

            if done or steps == 200:
                break

    @property
    def best_run(self):
        return self._best_run

if __name__ == "__main__":
    env = gym.make("CartPole-v1")

    # Get number of states and actions from envirnment
    num_states = env.env.observation_space.shape[0]
    num_actions = env.env.action_space.n

    model = Model(num_states, num_actions, BATCH_SIZE)
    memory = Memory(50000)

    runner = GameRunner(model, env, memory, MAX_EPS, MIN_EPS, LAMBDA, render=False)

    num_games = 300
    completed = 0
    for i in range(num_games):
        steps = runner.run()

        if steps == 200:
            completed +=1
        # Display number of games that reach max length every 50 games
        if (i+1)%50 == 0:
            print('Games {} - {}, {} games completed.'.format(i-48, i+1, completed))
            completed = 0

    print('Best Run: {}'.format(runner.best_run))
