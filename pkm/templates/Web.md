<%*
  let title = tp.file.title
  if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
    await tp.file.rename(title);
  } 
  const types = ["article", "tutorial", "reference", "repo", "qa"];
  const type = await tp.system.suggester(types, types, false, "Type of page");
  tR += "---"
%>
title:  <%* tR += title %>
created: <% tp.date.now("dddd Do MMMM YYYY HH:mm") %>
aliases: 
tags: 
---
- 
- Type: <%* tR += (type || "article") %>
- Source: 

---

# TL;DR

# Summary

# Key takeaways

1. 

# Tools and concepts

| Item | Role in the page |
|---|---|
|  |  |

# When to use

1. 

# Caveats

- 

---
