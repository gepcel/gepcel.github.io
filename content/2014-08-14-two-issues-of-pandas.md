Title: Two Issues of pandas Concerned with MultiIndex's Sort and stack
Date: 2014-08-14
Tags: python padas
Category: python
Slug: two-issues-of-pandas
Auther: gepcel
Latex:
Summary: 

There are two issues of pandas concerned with MultiIndex when sorting or stacking.

The first is when stacking multiple levels `df.stack([0, 1])`, couldn't get the expected result. `df.stack([0, 0])` worked. It's like to run `df.stack(0).stack(0)`. This might have been fixed, I just haven't upgrate yet. Haven't got time to check [this](https://github.com/pydata/pandas/pull/7770) yet.

The second issue is pretty frustrating. To show this, let's first construct some DataFrames.

```python
columns = pd.Index([u'12', u'16', u'20', u'8'], dtype='object')
index = pd.MultiIndex(levels=[[u'lb', u'sd', u'y'], [u'cumulative', u'growth', 
	       u'percentages'], [0.42, 1.25, 2.08, 2.91]],
           labels=[[0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 
           1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2, 
           0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 
           1, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 
           2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]],
           names=[u'a', u'b', u'c'])
values = np.array([['a', 'a', 'bc', 'a'],
       ['ab', 'ab', 'ab', 'a'],
       ['ab', 'bc', 'c', 'a'],
       [0.12, 0.46, 0.89, 0.15],
       [53.46, 15.88, 13.93, 28.87],
       [11.55, 20.82, 0.0, 11.55],
       [0.43, 1.13, 3.4, 0.17],
       [71.84, 60.42, 41.52, 49.52],
       [33.33, 66.67, 100.0, 13.33],
       ['a', 'a', 'c', 'a'],
       ['ab', 'ab', 'ab', 'a'],
       ['abc', 'bc', 'c', 'a'],
       [0.12, 0.53, 0.79, 0.15],
       [18.5, 20.39, 41.77, 25.43],
       [15.28, 17.32, 0.0, 5.77],
       [0.67, 1.2, 4.5, 0.13],
       [61.2, 66.5, 72.88, 58.11],
       [53.33, 70.0, 100.0, 6.67],
       ['a', 'a', 'c', 'a'],
       ['ab', 'ab', 'ab', 'a'],
       ['abc', 'bc', 'c', 'ab'],
       [0.15, 0.51, 1.03, 0.17],
       [11.01, 19.67, 23.65, 16.81],
       [20.82, 17.32, 0.0, 11.55],
       [0.97, 1.27, 4.93, 0.1],
       [54.8, 72.02, 79.5, 62.99],
       [63.33, 70.0, 100.0, 13.33],
       ['a', 'ab', 'c', 'a'],
       ['ab', 'ab', 'b', 'ab'],
       ['abc', 'bc', 'c', 'ab'],
       [0.17, 0.4, 1.04, 0.2],
       [21.88, 21.65, 64.59, 13.6],
       [15.28, 20.0, 0.0, 11.55],
       [1.1, 1.37, 6.33, 0.2],
       [41.9, 72.49, 139.61, 55.42],
       [76.67, 80.0, 100.0, 23.33]], dtype=object)
d = DataFrame(values, columns=columns, index=index)
```

So if I want a copy of d, with the index level 0 sorted by `['y', 'sd', 'lb']`, and level 1 sorted by `['growth', 'cumulative', 'percentages']`. My first thought was that it was easy to accomplish. `sortindex, sortlevel, set_index, reindex, reindex_axis, loc(or ix)`. Finally it turned out that none of above methods worked, at least not in the easyed way. 

When writing this article, I cann't put all of what has been tried here. Because most of them were done in ipython qtconsole, not the notebook. When it's done, it's gone. There have been some issues reported to [pandas](https://github.com/pydata/pandas), like [here 4088](https://github.com/pydata/pandas/issues/4088), and [here 6647](https://github.com/pydata/pandas/pull/6647), and [here 1864](http://github.com/pydata/pandas/issues/1864) ...

[Something](http://stackoverflow.com/questions/11194610/how-can-i-reorder-multi-indexed-dataframe-columns-at-a-specific-level) on [stackoverflow](http://stackoverflow.com/), gave me some instruction of a way to accomplish this. However it's not very intuitive. So I hope there will be an easier way to do this with pandas in the future version.

My way:

	:::python
	# primary_order
	po = ['y', 'sd', 'lb']
	# secondary_order
	so = ['growth', 'cumulative', 'percentages']
	order = lambda x: (po.index(x[0]), so.index(x[1]))
	ordered_index = sorted(d.index, key=order)
	result = d.reindex(ordered_index, axis=0)
