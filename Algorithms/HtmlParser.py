def HtmlParser(text):
    d ={"&quot;":'"',"&apos;":"'","&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
    Mode = False 
    Keywords, Outputs = [], []
    for char in text:
        if char == '&':
            Keywords.append(char)
            Mode = True 
        elif Mode:
            Keywords.append(char)
            if char == ';':
                Keywords = ''.join(Keywords)
                Outputs.append(d.get(Keywords, Keywords))
                Mode = False 
                Keywords = []
        else:
            Outputs.append(char)
    if Mode:
        Outputs.append(Keywords)
    return ''.join(Outputs)

text = "&amp; is an HTML entity but &ambassador; is not."
text_2 = "x &gt; y &amp;&amp; x &lt; y is always false"

print(HtmlParser(text))
print(HtmlParser(text_2))

