<%*
  let title = tp.file.title
  if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
    await tp.file.rename(title);
  } 
  let titleSplited = title.split(".")
  let tags = ""
  for (var [index, cur] of titleSplited.entries()) 
  { 
	  var j = index + 1
	  if (titleSplited[titleSplited.length - 1] !== cur) {
		  tags += cur.toString() + "/"
	  } else {
		  tags += cur.toString()
	  }
  }
  
  tR += "---"
%>
title:  <%* tR += title %>
created: <% tp.date.now("dddd Do MMMM YYYY HH:mm") %>
aliases: 
tags: <%* tR += tags %>
---

