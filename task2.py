def wordBreak(words, word, out=''):
    if not word:
        out_score = []
        seg_list.append(out)
        for i in out.split():
            out_score.append(len(i)**2)
        ss = sum(out_score)
        score_list.append(ss)
        return 
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix in words:
            wordBreak(words, word[i:], out + ' ' + prefix)
 
if __name__ == '__main__':
    with open(r'./additional_data/task2_words.txt') as f:
        words = f.read().split()
    seg_list = []
    score_list = []
    # word = 'buteeyorewassayingtohimselfthiswritingbusinesspencilsandwhatnotoverratedifyouaskmesillystuffnothinginit'
    # word = 'whenpoohsawwhatitwashenearlyfelldownhewassopleaseditwasaspecialpencilcasetherewerepencilsinitmarkedbforbearandpencilsmarkedhbforhelpingbearandpencilsmarkedbbforbravebeartherewasaknifeforsharpeningthepencilsandindiarubberforrubbingoutanythingwhichyouhadspeltwrongandarulerforrulinglinesforthewordstowalkonandinchesmarkedontherulerincaseyouwantedtoknowhowmanyinchesanythingwasandbluepencilsandredpencilsandgreenpencilsforsayingspecialthingsinblueandredandgreenandalltheselovelythingswereinlittlepocketsoftheirowninaspecialcasewhichshutwithaclickwhenyouclickeditandtheywereallforpooh'
    word = 'whenpoohsawwhatitwashenearlyfelldownhewassopleaseditwasaspecialpencilcasetherewerepencil'
    wordBreak(words, word)
    max_index = score_list.index(max(score_list))
    print('partition:',seg_list[max_index])
    print('max value(S):',score_list[max_index])

