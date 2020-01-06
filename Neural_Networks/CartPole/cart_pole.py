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
    def __init__(self, num_states, num_actions, batch_size):
        self.num_states = num_states
        self.num_actions = num_actions
        self.batch_size = batch_size

        defModel()

    def defModel(self):
        input = keras.layers.Input(shape=(num_states))
        d1 = keras.layers.Dense(10, activation='relu')(input)
        d2 = keras.layers.Dense(2)(d1)
        self.model = keras.model.Model(inputs=input, outputs = self.logits)


    def train_batch(self, train_x, train_y):
        dataset = tf.data.Dataset.from_tensor_slices((train_x, train_y)
        ).shuffle(self.batch_size).repeat()

        self.model.compile(optimizer='Adam', loss='mse')

        self.model.fit(dataseet, steps_per_epoch=1, verbose=0)

    def predict(self, state):
        return self.model.predict(state.reshape(1, self.num_states))

    def predict_batch(self, states):
        return self.model.predict_on_batch(states)

    @property
    def num_states(self):
        return self.num_states

    @property
    def num_actions(self):
        return self.num_actions

    @property
    def batch_size(self):
        return self.batch_size

class Memory:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = list()

    def add_sample(self, sample):
        self.data.append(sample)
        if len(self.data) > self.max_size:
            self.data.pop(0)

    def get_samples(self, num_samples):
        if len(self.data) > num_samples:
            return random.sample(self.data, len(self.data))
        else:
            return random.sample(self.data, num_samples)

class GameRunner:
    def __init__(self, model, env, memory, max_eps, min_eps, eps_decay_fac, render=True):
        self.env = env
        self.model = model
        self.memory = memory
        self.min_eps = min_eps
        self.max_eps = max_eps
        self.eps_decay_fac = eps_decay_fac
        self.eps = self.max_eps
        self.render = render

    def run(self):
        state = env.reset()

        while(True):
            if self.render:
                self.env.render()

            action = self.choose_action(state)
            new_state, reward, done, info = self.env.step(action)

            # increase reward for keeping the cart in the center
            if abs(new_state[0]) < .5:
                reward += 4
            elif abs(new_state[0] < 1):
                reward += 2
            elif abs(new_state[0] < 1.5):
                reward +=1

            # increase reward for keeping the pole strait
            if abs(new_state[2] < 3):
                reward += 4
            elif abs(new_state[2] < 6):
                reward += 2

            if done:
                new_state = None

            self.memory.add_sample((state, action, reward, new_state))
            self.train()

            self._eps = MIN_EPSILON + (MAX_EPSILON - MIN_EPSILON) \
                                      * math.exp(-LAMBDA * self._steps)

            state = new_state

            if done:
                break

    def train(self):
        batch = self.memory.get_samples(self.model.batch_size)
        states = np.array([i[0] for i in batch])
        new_states = np.array([(np.zeros(self._model.num_states)
                                 if val[3] is None else val[3]) for val in batch])

        q_old = self.model.predict_batch(states)
        q_new = self.model.predict_batch(new_states)

        x = np.zeros((self.model.batch_size, self.model.num_states))
        y = np.zeros((self.model.batch_size, self.model.num_actions))

        for i, b in enumerate(batch):
            state, action, reward, new_state = b[0], b[1], b[2], b[3]

            q = q_old[i]

            if new_state is None:
                q[action] = reward
            else:
                q[action] = reward + GAMMA * np.amax(q_new[i])

            x[i] = state
            y[i] = q
        self.model.train_batch(x, y)

    def choose_action(self, state):
        if random.random() < self.eps:
            return random.randint(0,1)
        else:
            return np.argmax(self.model.predict(state))

if __name__ == "__main__":
    env = gym.make("CartPole-v1")

    num_states = env.env.observation_space.shape[0]
    num_actions = env.env.action_space.n

    model = Model(num_states, num_actions, BATCH_SIZE)
    memory = Memory(50000)

    runner = GameRunner(model, env, memory, MAX_EPS, MIN_EPS, LAMBDA)

    num_games = 300

    for i in range(num_games):
        runner.run()
