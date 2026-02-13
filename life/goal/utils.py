import fitz

import random

#import random
from io import BytesIO
from django.http import FileResponse
def editor(file,list1,list2):
    print(type(file))
    og=file.name.split('.')[0]
    doc = fitz.open(stream=file.read(), filetype="pdf")
    pages=doc
    l=list1
    s=list2
    
    for page in pages:
        for i in range(len(l)):
            
            r1=page.search_for(l[i])
            #print(page.get_textbox(r1[0]))
            le=len(r1)
            if le==0:
                print("not found")
            else:
                #values=[page.get_textbox(r1[i])  for i in range(le) ]
                #print(values,'3')
                page.add_redact_annot(r1[0], fill=(1,1,1))
                page.apply_redactions()
                #m= pymupdf.Rect(r1[0])
                result = page.insert_text(r1[0][0:2],s[i],fontname="hebo", color=(0, 0, 0), fontsize=12)
                if result < 0:
                    
                    print(f"FAILED: The box at {m} is too small for the text.")
                else:
                    pass
    #ran=random.randint(1,100)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    doc.close()
    
    return FileResponse(buffer, as_attachment=True, filename=f"{og}_updated{random.randint(1,100)}.pdf")
#r'C:\Users\gcmad\Downloads\DOC-20260205-WA0010..pdf'
#l=['kalash gulati','00117702724']
#s=['manojssssss','00117232724']
#b=editor(r'C:\Users\gcmad\Downloads\DOC-20260205-WA0010..pdf','kalash gulati','00117702724','MANOJ Gulati','12345678')
#print(b)

