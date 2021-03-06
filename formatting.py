from markdown import markdown

DOTS_MENU=False

def do_menu(txt, title=None, fname=None):
   res = []
   if title:
      print title
      title_lines = title.strip().split("\n")
      res.append("<div class=topbar><a href=index.html id=mtitle1>%s</a><a href=index.html id=mtitle2>%s</a></div>" % (title_lines[0],title_lines[1]))

   res.append("<div dir='rtl' class=menu>")
   if DOTS_MENU:
      res.append("""
      <object width=100%%>  
      <param name="movie" value="dots.swf">
      <embed src="dots.swf" width=100%%>
      </embed>
      </object>
      """)
      
   lines = txt.strip().split("\n")
   last_indent = 0
   for line in lines:
      if line.strip() and line.strip()[0] == "#": continue
      indent = line.count("*")
      if indent > last_indent:
         while (last_indent != indent):
            res.append("<ul dir=rtl>")
            last_indent+=1
      if indent < last_indent:
            res.append("</ul>")
            last_indent-=1
      line = line.strip().replace("*","")
      try:
         line,link = line.strip().split("|")
         if link == fname:
            lstyle="citem"
         else: lstyle="item"
         if link.startswith("http") or "." in link: # don't add .html
            res.append("<li class=%s><a href=%s>%s</a></li>" % (lstyle,link,line))
         else:                                       # add .html
            res.append("<li class=%s><a href=%s.html>%s</a></li>" % (lstyle,link,line))
      except ValueError:
         res.append("<li class=category>%s</li>" % line)
   res.append("</div>")
   return "\n".join(res)

def do_content(txt,dir='rtl'):
   if txt.startswith("ltr"):
       dir='ltr'
       txt = txt[3:]
   txt = txt.replace("_S_","<b>").replace("_E_","</b>")
   html = markdown(txt)
   return "<div dir=%s class=content>%s</div>" % (dir,html)

def do_page(html_menu, html_content, STYLE_FILE="style.css", title="",dir="rtl"):
   return """
<?xml version="1.0" encoding="UTF-8"?>
<html>
<head>
<META http-equiv="Content-Type" Content="text/html; charset=utf-8">

<LINK REL=StyleSheet HREF="%s" TYPE="text/css" MEDIA=screen>
</style>
<title>%s</title>
</head>
<body dir=%s>
<!--<object width=100%%>  
<param name="movie" value="topBanner3.swf">
<embed src="topBanner3.swf" width=100%%>
</embed>
</object>-->
%s
</body>
</html>
   
   """ % (STYLE_FILE, title, dir, " ".join([html_menu, html_content]))

