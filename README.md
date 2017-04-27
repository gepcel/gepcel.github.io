# something about this for later use
1. There are three branches.
	* master  for static blog website
	* content  for all the content
	* pelican for all other things
2. And there are three folders. The parent folder **pelican**, which contains the config file, themes, layout, plugins, *et al*. And two children folder **content** with all the content files, and **output** with all the static files for a website.
3. To **generate**: run `>pelican content` in pelican folder
4. Be sure in the right **folder** and the right **branch**
	* check branch: `>git branch`
	* switch branch: `>git checkout master`
	* push pelican: `/pelican>git push blog pelican`
	* push content: `/pelican/content>git push blog content`
	* push output: `/pelican/output>git push blog master`
