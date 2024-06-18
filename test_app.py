from app import predict
import wikipedia
wikipedia.set_lang("it")
import warnings
warnings.filterwarnings("ignore")


def test_predict():
    text = wikipedia.summary('Sardegna', sentences=10)
    summary = predict(text)
    assert len(text) > len(summary)
