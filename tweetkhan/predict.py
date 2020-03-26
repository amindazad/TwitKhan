import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User
from .twitter import BASILICA

def predict_user(user1_name, user2_name, tweet_text):
    """Determine which use is more likely to tweet a given text"""
    user1 = User.query.filter(User.name == user1_name).one()
    user2 = User.query.filter(User.name == user2_name).one()
    user1_embeddings = np.array([tweet.embedding for tweet in user1.tweets])
    user2_embeddings = np.array([tweet.embedding for tweet in user2.tweets])
    embeddings = np.vstack([user1_embeddings, user2_embeddings])
    labels = np.concatenate([np.ones(len(user1.tweets)), np.zeros(len(user2.tweets))])
    log_reg = LogisticRegression().fit(embeddings, labels)
    tweet_embedding = BASILICA.embed_sentence(tweet_text, model='twiiter')
    return log_reg.predict(np.array(tweet_embedding).reshape(1, -1))