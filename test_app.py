from app import summarize
import wikipedia
wikipedia.set_lang("it")
import warnings
warnings.filterwarnings("ignore")


def test_summarize():
    text = wikipedia.summary('Sardegna', sentences=10)
    summary = summarize(text)
    assert len(text) > len(summary)
