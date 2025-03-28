import random

common_words = [
    "have", "that", "with", "this", "from", "they", "will", "there", "their", "what", "about", "which", "make", "like",
    "time", "just", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "other", "than",
    "then", "look", "only", "come", "over", "think", "also", "back", "after", "first", "well", "even", "want", "because",
    "these", "give", "most", "should", "very", "call", "many", "find", "long", "down", "need", "feel", "home", "life",
    "never", "same", "while", "might", "great", "still", "where", "leave", "mean", "keep", "help", "talk", "turn",
    "start", "show", "hear", "play", "move", "live", "bring", "write", "stand", "lose", "meet", "include", "continue",
    "learn", "change", "watch", "create", "speak", "spend", "grow", "open", "walk", "offer", "remember", "consider",
    "appear", "build", "expect", "stay", "believe", "happen", "include", "family", "animal", "number", "little",
    "letter", "mother", "father", "answer", "market", "reason","garden", "window", "summer", "winter", "autumn",
    "spring", "moment", "matter", "future", "past", "memory", "danger", "nation", "person", "friend", "travel",
    "danger", "energy", "result", "health", "effect", "system", "office", "silver", "random", "forest", "planet",
    "signal", "honest", "leader","artist", "choice", "beyond", "simple", "chance", "camera", "finger", "manage",
    "animal", "vision"
]


def display_sentence():
    return random.sample(common_words, 100)

def word_detection(word):
    if word in common_words:
        return True

    return False
