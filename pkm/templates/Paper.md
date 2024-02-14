<%*
  let title = tp.file.title
  if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
    await tp.file.rename(title);
  } 
  tR += "---"
%>
title:  <%* tR += title %>
created: <% tp.date.now("dddd Do MMMM YYYY HH:mm") %>
aliases: 
tags: 
---
- 

---