import nltk
from nltk.tokenize import word_tokenize
# nltk.download('punkt')

def test_fun(tokens_set1,tokens_set2):
    """
    Tests the split_tokens function with various assertions.

    Args:
    - tokens_set1: Set of tokens for testing.
    - tokens_set2: Another set of tokens for testing.
    """

    # Tests for tokens_set1 with n=3
    assert len(split_tokens(tokens_set1, n=3)) == 21
    assert split_tokens(tokens_set1,3)[0] == ('<BOS>', '<BOS>', 'It')
    assert split_tokens(tokens_set1, n=3)[10] == ('we', 'are', 'dealing')

    # Tests for tokens_set1 with n=2
    assert len(split_tokens(tokens_set1, n=2)) == 20
    assert split_tokens(tokens_set1, n=2)[0] == ('<BOS>', 'It')
    assert split_tokens(tokens_set1, n=2)[10] == ('are', 'dealing')

    # Tests for tokens_set2 with n=2
    assert len(split_tokens(tokens_set2, n=2)) == 10
    assert split_tokens(tokens_set2, n=2)[0] == ('<BOS>', 'How')
    assert split_tokens(tokens_set2, n=2)[9] == ('?', '<EOS>')


def tokenizer(phrase):
    """
    Tokenizes the input phrase using word_tokenize from NLTK.

    Args:
    - phrase: A string containing the text to be tokenized.

    Returns:
    - tokens: A list of tokens extracted from the input phrase.
    """
    tokens = word_tokenize(phrase)
    
    return tokens


def split_tokens(tokens, n=2):
    """
    Splits a list of tokens into n-grams.

    Args:
    - tokens: A list containing tokens to be split into n-grams.
    - n: An integer indicating the size of the n-grams. Default is 2.

    Returns:
    - split_tokens: A list of tuples representing the generated n-grams.
    """
    # Creating beginning-of-sentence and end-of-sentence tokens
    bos_list = ["<BOS>"] * (n - 1)
    eos_list = ["<EOS>"] * (n - 1)

    # Adding beginning and end tokens to the input tokens
    tokens = bos_list + tokens + eos_list


    k = len(tokens)
    split_tokens = []

    if n > k:
        print("Tokens too small for n value splits")
    elif n < k:
        # Generate n-grams from the tokens
        for i in range(k-n+1):
            j = i+n
            
            split_tokens.append(tuple(tokens[i:j]))

    elif n == k:
        print("Same size as tokens")

    
    return(split_tokens)


def main():
    """
    Main function to test tokenization and n-gram splitting.
    """

    # Sample portuguese sentences (commented out)
    # sentence1 = "Eu vou pousar a mão no teu quadril"
    # sentence2 = "Multiplicar-te os pés por muitos mil"
    
    # Sample English sentences
    sentence1 = "It shows, my dear Watson, that we are dealing with an exceptionally astude and dangerous man."
    sentence2 = "How would Lausanne do, my dear Watson?"

    # Tokenizing sentences
    tokens1 = tokenizer(sentence1)
    tokens2 = tokenizer(sentence2)

    # Testing tokenization and n-gram splitting
    test_fun(tokens1,tokens2)


main()



