import PyPDF2
import os
def between(num1,num2,num3):
    if num1 >= num2 and num1 <=num3:
        return True

def or_sec(rakam_el_gloos):
    
    if between(rakam_el_gloos,1,32):
        rkm_el_section=1
    elif between(rakam_el_gloos,33,64):
        rkm_el_section=2
    elif between(rakam_el_gloos,65,96):
        rkm_el_section=3
    elif between(rakam_el_gloos,97,128):
        rkm_el_section=4
    elif between(rakam_el_gloos,129,160):
        rkm_el_section=5
    elif between(rakam_el_gloos,161,192):
        rkm_el_section=6
    else:
        return False
    return rkm_el_section

def linear_alg_sec(rakam_el_gloos):
    
    if between(rakam_el_gloos,1,31):
        rkm_el_section=1
    elif between(rakam_el_gloos,32,62):
        rkm_el_section=2
    elif between(rakam_el_gloos,63,93):
        rkm_el_section=3
    elif between(rakam_el_gloos,94,124):
        rkm_el_section=4
    elif between(rakam_el_gloos,125,155):
        rkm_el_section=5
    elif between(rakam_el_gloos,156,186):
        rkm_el_section=6
    else:
        return False
    return rkm_el_section

path = "sections"
files = os.listdir(path)
name = input("Enter your name: ")
while not name:
    name = input("Enter your name: ")

for file in files:
    count_got=0
    pdf_file = open(path+"\\"+file, 'rb')    

    # creating a pdf reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)


    # extracting text from page


    count_names=0
    for el_saf7a in pdf_reader.pages:
        text = el_saf7a.extract_text()
        text = text.split('\n')
        gadwal_el_sacation = list()
        for i in text:
            if name in i:
                if count_names == 0:
                    print(i)
                count_names += 1
                
                rkm_gloos = i.split(" ")[0]
                rkm_gloos = int(rkm_gloos)
        if count_names == 1:
            text = pdf_reader.pages[0].extract_text().split('\n')
            for i in text:
                if "Sec " in i:
                    gadwal_el_sacation.append(i)
                    
            gadwal_el_sacation = ''.join(gadwal_el_sacation)
            each_Sec = gadwal_el_sacation.split("Sec")

            for i in each_Sec[1:]:
                range_arkam_elGloos = i.split(" ")[3:5]
                range_arkam_elGloos = [int(i) for i in range_arkam_elGloos]
                
                if file == "OR.pdf" and between(rkm_gloos,1,192):
                    rkm_el_section=or_sec(rkm_gloos)
                    if count_got==0:
                        print("section: ", rkm_el_section, " in ",file.strip("."))
                    count_got +=1
                elif file == "Linear Algebra.pdf" and between(rkm_gloos,1,186):
                    rkm_el_section=linear_alg_sec(rkm_gloos)
                    if count_got==0:
                        print("section: ", rkm_el_section, " in ",file.strip("."))
                    count_got +=1
                elif rkm_gloos >= range_arkam_elGloos[0] and rkm_gloos <= range_arkam_elGloos[1]:
                    if count_got==0:
                        rkm_el_section = i.split(" ")[1]
                        print("section: ", rkm_el_section, " in ",file.strip("."))
                    count_got +=1


            # closing the pdf file object
    if count_names >1: 
        print("more than one name specified in",file)
    elif count_names==0:
        print("no names specified in",file)
pdf_file.close()