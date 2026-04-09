def main():
    emoticon = input()
    emoticon = convertEmoticon(emoticon)
    print(emoticon)

def convertEmoticon(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon

main()
