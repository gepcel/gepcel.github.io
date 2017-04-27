Title: pelican 中集成 notebook 博客貌似不是个好主意
Date: 2014-05-05
Tags: ipython notebook pelican blog
Category: python
Slug: stop-blogging-ipython-notebooks-for-now
Auther: gepcel
Summary: 折腾 notebook 博客折腾累了

# pelican 中发布 notebook 博客的方法

### 方法一： ipythonnb
[Daniel Rodriguez](http://danielfrg.com/pages/about.html)制作了一个 pelican 插件 [ipythonnb](https://github.com/danielfrg/pelican-ipythonnb)，可以直接将整个 .ipynb 文件当作一篇博客内容进行发布。这个其实是个不错的主意，运行效果也不错，经过小的修改，css 之间冲突也比较小。而且这个也比较符合 notebook 的使用方法：整篇文章在 notebook 中完成。

### 方法二：liquid-tags
用 pelican 的 [liquid-tags](https://github.com/jakevdp/pelican-plugins/tree/liquid_tags/liquid_tags) 插件，这个也不错。其宗旨是在 .md 文件中像正常写 pelican 一样写博客，而博客中可以插入 .ipynb 文件，而且可以以 
    
    {% literal notebook path/to/notebook.ipynb [cells[i:j]] %} 

的形式插入指定的行。保持了博客内容的独立和简洁。

# 问题
这两种方法都存在一个问题是 notebook 的样式问题，每种方法都要费好大的心思去调整 notebook 的样式和原本的样式之间的冲突。而在 ipython 升级之后，可能又要重新调整……

在努力的尝试之后，暂时还是放弃吧，不得不佩服前端设计人员，需要巨大的耐心啊！我等焦躁之人还是等等看有没有高手弄出一个成熟的解决方案吧。感觉 notebook 的样式设计的很糟糕，独自运行的时候没有问题，但是一涉及到整合的时候，各种冲突……