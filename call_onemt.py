from load_onemt import Translator
import sentencepiece as spm
from oneconfig import *
import random

print (SUBWORD_MODEL_PATH)
print (TRANSLATION_MODEL_FOLDER)

print (TRANSLATION_MODEL_PATH)


language_mapping = {
    "asm": "asm_Beng",
    "awa": "awa_Deva",
    "ben": "ben_Beng",
    "ban": "ben_Beng",
    "bho": "bho_Deva",
    "bra": "bra_Deva",
    "brx": "brx_Deva",
    "doi": "doi_Deva",
    "gom": "gom_Deva",
    "gon": "gon_Deva",
    "guj": "guj_Gujr",
    "hin": "hin_Deva",
    "hingh": "hingh_Deva",
    "hoc": "hoc_Wara",
    "kan": "kan_Knda",
    "kas_arab": "kas_Arab",
    "kas": "kas_Arab",
    "kas_deva": "kas_Deva",
    "kha": "kha_Latn",
    "lus": "lus_Latn",
    "mai": "mai_Deva",
    "mag": "mag_Deva",
    "mal": "mal_Mlym",
    "mar": "mar_Deva",
    "mni_beng": "mni_Beng",
    "mni": "mni_Beng",
    "mni_mtei": "mni_Mtei",
    "npi": "npi_Deva",
    "ory": "ory_Orya",
    "ori": "ory_Orya",
    "odi": "ory_Orya",
    "pan": "pan_Guru",
    "pun": "pan_Guru",
    "san": "san_Deva",
    "sat": "sat_Olck",
    "sin": "sin_Sinh",
    "snd_arab": "snd_Arab",
    "snd_deva": "snd_Deva",
    "snd": "snd_Arab",
    "tam": "tam_Taml",
    "tcy": "tcy_Knda",
    "tel": "tel_Telu",
    "urd_arab": "urd_Arab",
    "urd": "urd_Arab",
    "eng": "eng_Latn",
    "xnr": "xnr_Deva"
}

familymap = {"asm_Beng":"Magadhi","awa_Deva":"CentralIndic","ben_Beng":"Magadhi","bho_Deva":"Magadhi","bra_Deva":"CentralIndic","brx_Deva":"TibetoBurman","doi_Deva":"WesternIndic","eng_Latn":"WestGermanic","gom_Deva":"Maharashtri","gon_Deva":"Dravidian","guj_Gujr":"WesternIndic","hin_Deva":"CentralIndic","hingh_Deva":"CentralIndic","hoc_Wara":"AustroAsiatic","kan_Knda":"Dravidian","kas_Arab":"WesternIndic","kas_Deva":"WesternIndic","kha_Latn":"AustroAsiatic","lus_Latn":"TibetoBurman","mag_Deva":"Magadhi","mai_Deva":"Magadhi","mal_Mlym":"Dravidian","mar_Deva":"Maharashtri","mni_Beng":"TibetoBurman","mni_Mtei":"TibetoBurman","npi_Deva":"CentralIndic","ory_Orya":"Magadhi","pan_Guru":"WesternIndic","san_Deva":"Vedic","sat_Olck":"AustroAsiatic","sin_Sinh":"Maharashtri","snd_Arab":"WesternIndic","snd_Deva":"WesternIndic","tam_Taml":"Dravidian","tcy_Knda":"Dravidian","tel_Telu":"Dravidian","urd_Arab":"CentralIndic","xnr_Deva":"CentralIndic"}

def add_family(lang):
    return familymap[lang]+'+'+lang


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


def translate_onemtbck(task, domain, text, ttext, sl, tl):
    nsl = add_family(language_mapping[sl])
    ntl = add_family(language_mapping[tl])
    
    text = text.replace('।','.').replace('\u200c','')
    ttext = ttext.replace('।','.').replace('\u200c','')

    c=0
    outputs = []
    for part in text.split('\n'):
        part=part.strip()
        if part=='':
            outputs.append('')
            continue

        if task=='Translation':
            nsl = add_family(language_mapping[sl])
            ntl = add_family(language_mapping[tl])
            part = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: part }}
        elif task=='Grammar33':
            #nsl = add_family(language_mapping['eng'])
            #ntl = add_family(language_mapping['hin'])
            text = {'task': 'Correction$Incorrect'+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}

        elif task=='Translation quality estimation':
            #nsl = add_family(language_mapping['eng'])
            #ntl = add_family(language_mapping['hin'])
            text = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}
        elif task=='Translation post editing':
            text = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}
        elif task=='Translation error marking':
            text = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}
        #else:
        #    text = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}


        print ('1--->',part)
        soutput = s.encode(str(part), out_type=str)
        print ('2--->',soutput)
        out = translator.translate([" ".join(soutput)])
        print (out[0],'<----------OOO')
        if task=='Translation':
            output = eval(out[0].replace(' ','').replace('▁',' '))['output'][ntl]
        #elif task=='Translation quality estimation':
        #    output = str(eval(out[0].replace(' ','').replace('▁',' '))['output']).replace(' out of 100','')
        #elif task=='Translation post editing':
        #    output = str(eval(out[0].replace(' ','').replace('▁',' '))['output']['post edited '+ntl])
        #elif task=='Translation error marking':
        #    output = str(eval(out[0].replace(' ','').replace('▁',' '))['output'])
        #else:
        #    output = str(eval(out[0].replace(' ','').replace('▁',' '))['output'])
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
        output = output.replace('।','.')
        outputs.append(output)
        print (output, 'Before')
        c=c+1

    if task=='Translation':
        send = "\n".join(outputs)
    else:
        send = outputs[0]

    return send.strip().replace('\u200c','')



def translate_onemt(task, domain, text, ttext, sl, tl):
    nsl = add_family(language_mapping[sl])
    ntl = add_family(language_mapping[tl])
    
    text = text.replace('।','.').replace('\u200c','')
    ttext = ttext.replace('।','.').replace('\u200c','')

    outputs = []
    if task=='Translation':
        for part in text.split('\n'):
            part=part.strip()
            if part=='':
                outputs.append('')
                continue

            nsl = add_family(language_mapping[sl])
            ntl = add_family(language_mapping[tl])
            
            if nsl==ntl:
                part = {'task': 'Correction$Incorrect'+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: part }}
            else:
                part = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: part }}
        
            print ('1--->',part)
            soutput = s.encode(str(part), out_type=str)
            print ('2--->',soutput)
            out = translator.translate([" ".join(soutput)])
            print (out[0],'<----------OOO')
            if nsl==ntl:
                output = eval(out[0].replace(' ','').replace('▁',' '))['output']['Corrected '+ntl]
            else:
                output = eval(out[0].replace(' ','').replace('▁',' '))['output'][ntl]

            output = output.replace('।','.')
            outputs.append(output)

    else:
        if nsl==ntl:
            #nsl = add_family(language_mapping['eng'])
            #ntl = add_family(language_mapping['hin'])
            text = {'task': 'Correction$Incorrect'+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}

        elif task=='Translation quality estimation':
            nsl = add_family(language_mapping['eng'])
            ntl = add_family(language_mapping['hin'])
            text = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}
        elif task=='Translation post editing':
            text = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}
        elif task=='Translation error marking':
            text = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}
        else:
            text = {'task': task+'$'+nsl+'#'+ntl, 'domain': domain, 'input': {nsl: text , ntl: ttext}}

        print ('1--->',text)
        soutput = s.encode(str(text), out_type=str)
        print ('2--->',soutput)
        out = translator.translate([" ".join(soutput)])
        print (out[0],'<----------OOO')
        if task=='Translation':
            output = eval(out[0].replace(' ','').replace('▁',' '))['output'][ntl]
        elif task=='Translation quality estimation':
            output = str(eval(out[0].replace(' ','').replace('▁',' '))['output']).replace(' out of 100','')
        elif task=='Translation post editing':
            output = str(eval(out[0].replace(' ','').replace('▁',' '))['output']['post edited '+ntl])
        elif task=='Translation error marking':
            output = str(eval(out[0].replace(' ','').replace('▁',' '))['output'])
        else:
            output = str(eval(out[0].replace(' ','').replace('▁',' '))['output'])
            pre_output = str(eval(out[0].replace(' ','').replace('▁',' '))['output']['post edited'+ntl])
            noutput = []
            for w in pre_output.split():
                if w not in ttext:
                    noutput.append('<c>'+w+'</c>')
                else:
                    noutput.append(w)
            pre_output1 = " ".join(noutput)
            output = output.replace(pre_output,pre_output1)
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
        output = output.replace('।','.')
        outputs.append(output)
        print (output, 'Before')

    if task=='Translation':
        send = "\n".join(outputs)
    else:
        send = outputs[0]

    return send.strip().replace('\u200c','')

#_inp = "{'task': 'Translation$WesternIndic+guj_Gujr#WestGermanic+eng_Latn', 'domain': 'general', 'output': {'CentralIndic+hin_Deva': 'नई दिल्ली-केंद्र सरकार ने महंगाई भत्ते में वृद्धि की घोषणा की है। यह वृद्धि उन केंद्रीय कर्मचारियों और स्वायत्त संस्थानों के कर्मचारियों पर लागू होगी, जिन्हें 5वें और 6वें वेतन आयोग के अनुसार वेतन मिल रहा है। वित्त मंत्रालय में सार्वजनिक उद्यम विभाग ने इस संबंध में 7 नवंबर 2024 को एक कार्यालय ज्ञापन जारी किया है। }}}"

#_inp = '{"task": "Translation quality estimation$CentralIndic+hin_Deva#WestGermanic+eng_Latn", "domain": "general", "input": {"CentralIndic+hin_Deva": "exe फ़ाइल चलाएँ और निर्देशों का पालन करें", "WestGermanic+eng_Latn": "Run the .exe file and follow the instructions."}}'

#print (translate_onemt(_inp, "eng","hin"))
