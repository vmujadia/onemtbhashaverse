from load_onemt import Translator
import sentencepiece as spm
from oneconfig import *
import random

print (SUBWORD_MODEL_PATH)
print (TRANSLATION_MODEL_FOLDER)

print (TRANSLATION_MODEL_PATH)



s = spm.SentencePieceProcessor(model_file=SUBWORD_MODEL_PATH)

translator = Translator(data_dir=TRANSLATION_MODEL_FOLDER, checkpoint_path=TRANSLATION_MODEL_PATH, batch_size=100)



def split_into_parts(text, num_words=100):
  """Splits text into parts of a given number of words.

  Args:
    text: The text to split.
    num_words: The number of words per part.

  Returns:
    A list of strings, where each string is a part of the text.
  """

  words = text.split()
  parts = []
  current_part = []
  for word in words:
    current_part.append(word)
    if len(current_part) == num_words:
      parts.append(' '.join(current_part))
      current_part = []
  if current_part:
    parts.append(' '.join(current_part))
  return parts


def translate_onemt(text, sl, tl):
    nsl = language_mapping[sl]
    ntl = language_mapping[tl]


    soutput = s.encode(text, out_type=str)
    out = translator.translate([" ".join(soutput)])
    output = out[0].replace(' ','').replace('▁',' ')


    '''
    if len(text.split())>200:
        otext = ''
        for p in split_into_parts(text):
            soutput = s.encode('###'+nsl+'-to-'+ntl+'### '+p, out_type=str)
            out = translator.translate([" ".join(soutput)])
            output = out[0].replace(' ','').replace('▁',' ')
            otext = otext + ' '+output
        return otext.strip()
    else:
        soutput = s.encode('###'+nsl+'-to-'+ntl+'### '+text, out_type=str)
        out = translator.translate([" ".join(soutput)])
        output = out[0].replace(' ','').replace('▁',' ')
    '''

    return output.strip()

_inp = "{'task': 'Translation$WesternIndic+guj_Gujr#WestGermanic+eng_Latn', 'domain': 'general', 'output': {'CentralIndic+hin_Deva': 'नई दिल्ली-केंद्र सरकार ने महंगाई भत्ते में वृद्धि की घोषणा की है। यह वृद्धि उन केंद्रीय कर्मचारियों और स्वायत्त संस्थानों के कर्मचारियों पर लागू होगी, जिन्हें 5वें और 6वें वेतन आयोग के अनुसार वेतन मिल रहा है। वित्त मंत्रालय में सार्वजनिक उद्यम विभाग ने इस संबंध में 7 नवंबर 2024 को एक कार्यालय ज्ञापन जारी किया है। }}}"

_inp = '{"task": "Translation quality estimation$CentralIndic+hin_Deva#WestGermanic+eng_Latn", "domain": "general", "input": {"CentralIndic+hin_Deva": "exe फ़ाइल चलाएँ और निर्देशों का पालन करें", "WestGermanic+eng_Latn": "Run the .exe file and follow the instructions."}}'

print (translate_onemt(_inp, "eng","hin"))
