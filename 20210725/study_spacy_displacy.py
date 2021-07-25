import spacy
from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp("Bill Gates is the CEO of Microsoft")

#displacy.serve(doc, style = "dep", port=5005)
# dependency parse를 시각화

displacy.serve(doc, style='ent')
# entity parse 시각화