from markdown import markdown 
import codecs
import formatting
from collections import defaultdict
import glob


# read page titles
titles = defaultdict(str)
for line in codecs.open("pages.titles","r","utf8"):
   line = line.strip()
   ttl,page = line.split("|",1)
   titles[page]=ttl

menu_title        = codecs.open("menu.title","r","utf8").read()
menu_file_content = codecs.open("menu.links","r","utf8").read()
for fname in glob.glob("*.txt"):
   if fname in ['groups.txt']: continue
   print(fname)
   fcontent = codecs.open(fname,"r","utf8").read()
   fname = fname.replace(".txt","")

   menu_html = formatting.do_menu(menu_file_content,menu_title,fname)
   content_html, meta_file = formatting.do_content(fcontent)

   page = formatting.do_page(menu_html, content_html, "style.css", titles[fname], meta_file=meta_file)

   fout = codecs.open(fname+".html","w","utf8")
   fout.write(page)
   fout.close()



#menu_html = formatting.do_menu(codecs.open("menu.links","r","utf8").read(),"adhd-child")
#content_html = formatting.do_content(codecs.open("adhd.txt","r","utf8").read())
#html_page = formatting.do_page(menu_html, content_html)
#html = markdown(codecs.open("adhd.txt","r","utf8").read())
#html = markdown(codecs.open("menu.links","r","utf8").read())
#html = markdown(codecs.open("adhd-and-learning.txt","r","cp1255").read())
#print html_page.encode("utf8")
