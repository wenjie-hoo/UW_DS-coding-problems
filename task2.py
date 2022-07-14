def wordBreak(words, word, out=''):
    if not word:
        out_score = []
        seg_list.append(out)
        for i in out.split():
            out_score.append(len(i)**2)
        score_list.append(sum(out_score))
        return 
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix in words:
            wordBreak(words, word[i:], out + ' ' + prefix)

words_V = ['h', 'ca', 'go', 'lit', 'they', 'was', 'ant', 'there', 'in', 'now', 'pencil',
            'sand', 'licked', 'silly', 'do', 'us', 'sha', 'what', 'love', 'when', 'm', 'real',
            'at', 'itwhen', 'say', 'er', 'nearly', 'not', 'of', 'rated', 'out', 'man', 'writing',
            'fell', 'wanted', 'ran', 'soft', 'hb', 'any', 'here', 'we', 'hey', 'want', 'ear', 'ease',
            'knife', 'no', 'himself', 'whatnot', 'anything', 'ruling', 'bear', 'it', 'him', 'clicked',
            'marked', 'blue', 'an', 'earth', 'this', 'ruler', 'oo', 'pooh', 'their', 'to', 'wo', 'ee',
            'saying', 'line', 'v', 'his', 'me', 'business', 'if', 'how', 'wrong', 'lo', 'he', 'pin', 'o',
            'these', 'or', 'special', 'as', 'words', 'own', 'thing', 'on', 'help', 'walk', 'nothing', 
            'india', 'w', 'had', 'rubbing', 'hat', 'inch', 'inches', 'p', 'thin', 'near', 'please', 'were',
            'is', 'pencils', 'her', 'for', 'be', 'stuff', 'helping', 'sharpening', 'many', 'pockets', 'over', 
            'who', 'b', 'red', 'all', 'pleased', 'a', 'and', 'case', 'wash', 'know', 'things', 'hi', 'mark',
            'i', 'spelt', 'saw', 'word', 'eeyore', 'shut', 'poohs', 'you', 'set', 'ing', 'brave', 'sw', 
            'little', 'r', 'ask', 'ho', 'bb', 'ow', 'the', 'early', 'with', 'click', 'green', 'ate', 'so', 
            'down', 'which', 'pocket', 'rubber', 'lovely', 'ha', 'lick', 'she', 'lines', 'but', 'oh', 'tin', 'pen']
Text_A = 'buteeyorewassayingtohimselfthiswritingbusinesspencilsandwhatnotoverratedifyouaskmesillystuffnothinginit'
Text_B = 'whenpoohsawwhatitwashenearlyfelldownhewassopleaseditwasaspecialpencilcasetherewerepencilsinitmarkedbforbearandpencilsmarkedhbforhelpingbearandpencilsmarkedbbforbravebeartherewasaknifeforsharpeningthepencilsandindiarubberforrubbingoutanythingwhichyouhadspeltwrongandarulerforrulinglinesforthewordstowalkonandinchesmarkedontherulerincaseyouwantedtoknowhowmanyinchesanythingwasandbluepencilsandredpencilsandgreenpencilsforsayingspecialthingsinblueandredandgreenandalltheselovelythingswereinlittlepocketsoftheirowninaspecialcasewhichshutwithaclickwhenyouclickeditandtheywereallforpooh'
Text = [Text_A,Text_B[0:103],Text_B[103:220],Text_B[220:319],Text_B[319:432],Text_B[432:]]
res_text = []
max_values=[]
for i in range(len(Text)):
    seg_list = []
    score_list = []
    wordBreak(words_V,Text[i])
    max_index = score_list.index(max(score_list))
    res_text.append(seg_list[max_index])
    max_values.append(score_list[max_index])
print('Text A:',res_text[0])
print('Text A max value(S):',max_values[0])
print('Text B:',res_text[1]+res_text[2]+res_text[3]+res_text[4])
print('Text B max value(S):',max_values[1]+max_values[2]+max_values[3]+max_values[4])